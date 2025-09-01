import PyPDF2
import pyttsx3
import re
import os
import sys
from pathlib import Path

class PDFToSpeech:
    def __init__(self):
        # Initialize the text-to-speech engine
        self.tts_engine = pyttsx3.init()
        self.setup_voice_settings()
        
    def setup_voice_settings(self):
        """Configure the voice settings for better speech quality"""
        # Get available voices
        voices = self.tts_engine.getProperty('voices')
        
        # Try to set a nice voice (prefer female voices as they're often clearer)
        for voice in voices:
            if 'female' in voice.name.lower() or 'woman' in voice.name.lower():
                self.tts_engine.setProperty('voice', voice.id)
                break
        
        # Set speech rate (words per minute) - slower is easier to follow
        self.tts_engine.setProperty('rate', 180)  # Default is usually 200
        
        # Set volume (0.0 to 1.0)
        self.tts_engine.setProperty('volume', 0.9)
        
    def extract_text_from_pdf(self, pdf_path):
        """
        Extract text from PDF file
        Like carefully copying every word from a book page by page
        """
        try:
            text = ""
            
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                total_pages = len(pdf_reader.pages)
                
                print(f"📖 Found {total_pages} pages in the PDF")
                
                # Go through each page
                for page_num in range(total_pages):
                    print(f"📄 Reading page {page_num + 1}/{total_pages}")
                    page = pdf_reader.pages[page_num]
                    page_text = page.extract_text()
                    text += page_text + "\n"
                    
            return text
            
        except Exception as e:
            print(f"❌ Error reading PDF: {e}")
            return None
    
    def clean_text(self, text):
        """
        Clean up the extracted text to make it more speech-friendly
        Like editing a rough draft to make it flow better when read aloud
        """
        if not text:
            return ""
        
        # Remove excessive whitespace and newlines
        text = re.sub(r'\n+', ' ', text)  # Replace multiple newlines with space
        text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
        
        # Remove common PDF artifacts
        text = re.sub(r'[^\w\s\.,!?;:\'"-]', '', text)  # Keep only common punctuation
        
        # Fix common issues
        text = text.replace('â€™', "'")  # Fix apostrophes
        text = text.replace('â€œ', '"')  # Fix opening quotes
        text = text.replace('â€', '"')   # Fix closing quotes
        
        # Remove page numbers that are standalone
        text = re.sub(r'\b\d+\b(?=\s|$)', '', text)
        
        return text.strip()
    
    def speak_text(self, text, save_audio=False, audio_filename=None):
        """
        Convert text to speech and either play it or save it
        Like having a professional narrator read your document
        """
        if not text.strip():
            print("❌ No text to speak!")
            return False
        
        try:
            if save_audio and audio_filename:
                print(f"🎵 Saving speech to {audio_filename}")
                self.tts_engine.save_to_file(text, audio_filename)
                self.tts_engine.runAndWait()
                print(f"✅ Audio saved successfully!")
            else:
                print("🔊 Starting to speak... (Press Ctrl+C to stop)")
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
                print("✅ Finished speaking!")
                
            return True
            
        except KeyboardInterrupt:
            print("\n⏹️  Speech stopped by user")
            self.tts_engine.stop()
            return False
        except Exception as e:
            print(f"❌ Error during speech: {e}")
            return False
    
    def get_voice_info(self):
        """Display information about available voices"""
        voices = self.tts_engine.getProperty('voices')
        current_voice_id = self.tts_engine.getProperty('voice')
        
        print("\n🎤 Available Voices:")
        for i, voice in enumerate(voices):
            marker = "👉 " if voice.id == current_voice_id else "   "
            print(f"{marker}{i}: {voice.name} - {voice.languages}")
    
    def change_voice(self, voice_index):
        """Change the voice used for speech"""
        voices = self.tts_engine.getProperty('voices')
        if 0 <= voice_index < len(voices):
            self.tts_engine.setProperty('voice', voices[voice_index].id)
            print(f"✅ Voice changed to: {voices[voice_index].name}")
        else:
            print("❌ Invalid voice index!")
    
    def change_speed(self, rate):
        """Change the speech rate (words per minute)"""
        if 50 <= rate <= 400:  # Reasonable range
            self.tts_engine.setProperty('rate', rate)
            print(f"✅ Speech rate changed to {rate} words per minute")
        else:
            print("❌ Rate should be between 50 and 400 words per minute")
    
    def process_pdf(self, pdf_path, save_audio=False, audio_path=None):
        """
        Main method to convert PDF to speech
        The conductor that coordinates the whole orchestra
        """
        print(f"🚀 Starting PDF to Speech conversion...")
        print(f"📁 PDF File: {pdf_path}")
        
        # Check if PDF exists
        if not os.path.exists(pdf_path):
            print(f"❌ PDF file not found: {pdf_path}")
            return False
        
        # Step 1: Extract text
        print("\n📖 Step 1: Extracting text from PDF...")
        text = self.extract_text_from_pdf(pdf_path)
        
        if not text:
            print("❌ Could not extract text from PDF")
            return False
        
        # Step 2: Clean text
        print("\n🧹 Step 2: Cleaning text...")
        clean_text = self.clean_text(text)
        
        word_count = len(clean_text.split())
        print(f"📊 Extracted {word_count} words")
        
        if word_count == 0:
            print("❌ No readable text found in PDF")
            return False
        
        # Show preview
        preview = clean_text[:200] + "..." if len(clean_text) > 200 else clean_text
        print(f"\n👀 Preview: {preview}")
        
        # Step 3: Convert to speech
        print(f"\n🎵 Step 3: Converting to speech...")
        estimated_time = word_count / 180  # Assuming 180 words per minute
        print(f"⏱️  Estimated duration: {estimated_time:.1f} minutes")
        
        success = self.speak_text(clean_text, save_audio, audio_path)
        return success

def main():
    """Main function - like the script's director"""
    print("🎤 PDF to Speech Converter")
    print("=" * 50)
    
    # Create converter
    converter = PDFToSpeech()
    
    # Get PDF file path
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = input("📁 Enter PDF file path: ").strip().strip('"')
    
    # Check if file exists
    if not pdf_path or not os.path.exists(pdf_path):
        print("❌ Please provide a valid PDF file path")
        return
    
    # Ask user preferences
    print("\n⚙️  Settings:")
    
    # Voice selection
    converter.get_voice_info()
    try:
        voice_choice = input("\n🎤 Choose voice number (press Enter for current): ").strip()
        if voice_choice:
            converter.change_voice(int(voice_choice))
    except (ValueError, IndexError):
        print("Using current voice...")
    
    # Speed selection
    try:
        speed = input("🏃 Speech speed (50-400, press Enter for 180): ").strip()
        if speed:
            converter.change_speed(int(speed))
    except ValueError:
        print("Using default speed...")
    
    # Audio saving option
    save_audio = input("\n💾 Save as audio file? (y/n): ").strip().lower() == 'y'
    audio_path = None
    
    if save_audio:
        pdf_name = Path(pdf_path).stem
        audio_path = f"{pdf_name}_speech.wav"
        custom_path = input(f"💾 Audio filename (Enter for '{audio_path}'): ").strip()
        if custom_path:
            audio_path = custom_path
    
    # Process the PDF
    print("\n" + "=" * 50)
    success = converter.process_pdf(pdf_path, save_audio, audio_path)
    
    if success:
        print("\n🎉 Conversion completed successfully!")
        if save_audio:
            print(f"🎵 Audio saved to: {audio_path}")
    else:
        print("\n❌ Conversion failed!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("💡 Make sure you have installed: pip install PyPDF2 pyttsx3")