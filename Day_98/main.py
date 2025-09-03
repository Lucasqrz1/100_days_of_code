import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import datetime
import os
import json
import gspread
from google.oauth2.service_account import Credentials

# --- CONFIGURATION ---
URL = "https://www.amazon.com/dp/PRODUCT_ID"  # Replace with your product URL
TARGET_PRICE = 200.00  # Alert threshold

# Twilio
TWILIO_SID = "YOUR_TWILIO_SID"
TWILIO_AUTH = "YOUR_TWILIO_AUTH_TOKEN"
FROM_NUMBER = "+1234567890"
TO_NUMBER = "+19876543210"

# Google Sheets (optional)
USE_SHEETS = True
SPREADSHEET_NAME = "Amazon Price Tracker"
CREDENTIALS_FILE = "credentials.json"

# Last sent price file
STATE_FILE = "last_price.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9"
}

# --- FUNCTION: Get current price ---
def get_price():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    price_tag = soup.find("span", {"id": "priceblock_ourprice"})
    if not price_tag:
        price_tag = soup.find("span", {"id": "priceblock_dealprice"})
    if not price_tag:
        raise ValueError("Price not found on the page")
    price = float(price_tag.get_text().replace("$","").replace(",","").strip())
    return price

# --- FUNCTION: Load last sent price ---
def load_last_price():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f).get("last_price", None)
    return None

# --- FUNCTION: Save last sent price ---
def save_last_price(price):
    with open(STATE_FILE, "w") as f:
        json.dump({"last_price": price}, f)

# --- FUNCTION: Send SMS ---
def send_sms(price):
    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages.create(
        body=f"Amazon price dropped! Current price: ${price}\n{URL}",
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )
    print("SMS sent:", message.sid)

# --- FUNCTION: Log to Google Sheets ---
def log_to_sheet(price):
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    gc = gspread.authorize(creds)
    sheet = gc.open(SPREADSHEET_NAME).sheet1
    today = datetime.date.today().isoformat()
    sheet.append_row([today, price])
    print("Logged to sheet")

# --- MAIN ---
try:
    current_price = get_price()
    print("Current price:", current_price)
    last_sent = load_last_price()

    if current_price < TARGET_PRICE and (last_sent is None or current_price < last_sent):
        send_sms(current_price)
        save_last_price(current_price)
    else:
        print("No alert sent.")

    if USE_SHEETS:
        log_to_sheet(current_price)

except Exception as e:
    print("Error:", e)
