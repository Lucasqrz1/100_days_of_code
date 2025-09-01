# 🏀 Jaylen Brown NBA Stats Scraper

A simple **NBA data scraping simulation app** built with **HTML, CSS, and JavaScript**.  
It allows you to view **Jaylen Brown's career stats, current season stats, and recent game logs** in an interactive web interface, with the option to **export data to CSV**.

---

## 🚀 Features
- View player bio and team info.
- Scrape (simulate) different datasets:
  - 📊 **Career Statistics**  
  - 📈 **Current Season Statistics**  
  - 🎮 **Recent Game Logs**  
- Interactive data tables with hover effects.
- CSV export with preview.
- Clean UI with responsive design.

---

## 📂 Project Structure
jaylen-brown-scraper/
│── index.html # Main app file (HTML, CSS, JS inline)


---

## ⚙️ How It Works
- All data is **hardcoded** in the script (no live API calls).  
- When a button is clicked, the app:
  1. Shows a loading spinner.
  2. Displays the requested dataset (career, season, or games).
  3. Enables the CSV export option.
- Data preview is displayed in a styled table.
- CSV can be downloaded directly from the browser.

---

## 📦 Installation
1. Clone or download this repository.  
2. Open `index.html` in any modern web browser.  
3. No dependencies required.

---

## 🖥️ Usage
- **Scrape Career Stats** → Loads full career stats.  
- **Scrape Current Season Stats** → Loads latest season data.  
- **Scrape Game Logs** → Loads recent games.  
- **Export to CSV** → Downloads the current dataset.  


---

## 📝 Notes
- Data shown is **simulated**, not live-scraped.  
- Intended as a **front-end demo project** for scraping UI concepts.  
- To integrate with real data, replace the `jaylenBrownData` object with an API or scraping backend.

---

## 📜 License
MIT License. Free to use and modify.
