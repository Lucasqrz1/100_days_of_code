import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Test sentences - like a menu of challenges
        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Python is a powerful programming language that is easy to learn.",
            "Practice makes perfect when it comes to typing speed.",
            "A journey of a thousand miles begins with a single step.",
            "The best time to plant a tree was 20 years ago. The second best time is now.",
            "In the middle of difficulty lies opportunity.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "The only way to do great work is to love what you do.",
            "Innovation distinguishes between a leader and a follower.",
            "Life is what happens when you're busy making other plans."
        ]
        
        # Game state variables - like keeping score in a game
        self.current_sentence = ""
        self.start_time = None
        self.is_testing = False
        self.correct_chars = 0
        self.total_chars = 0
        
        self.setup_ui()
        self.new_test()
    
    def setup_ui(self):
        # Main title - like a sign at the top of a shop
        title_label = tk.Label(
            self.root, 
            text="⚡ Typing Speed Test ⚡", 
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        title_label.pack(pady=20)
        
        # Instructions - like a recipe card
        instructions = tk.Label(
            self.root,
            text="Type the text below as quickly and accurately as possible!\nClick 'New Test' to start with a fresh sentence.",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#34495e"
        )
        instructions.pack(pady=10)
        
        # Text to type frame - like a display window
        text_frame = tk.Frame(self.root, bg="#ffffff", relief="solid", bd=2)
        text_frame.pack(pady=20, padx=40, fill="x")
        
        self.text_display = tk.Label(
            text_frame,
            text="",
            font=("Courier", 14),
            bg="#ffffff",
            fg="#2c3e50",
            wraplength=700,
            justify="left",
            pady=20,
            padx=20
        )
        self.text_display.pack()
        
        # Input field - like a typewriter
        input_frame = tk.Frame(self.root, bg="#f0f0f0")
        input_frame.pack(pady=20, padx=40, fill="x")
        
        tk.Label(
            input_frame,
            text="Your typing:",
            font=("Arial", 12, "bold"),
            bg="#f0f0f0"
        ).pack(anchor="w")
        
        self.input_text = tk.Text(
            input_frame,
            height=4,
            font=("Courier", 12),
            bg="#ffffff",
            fg="#2c3e50",
            relief="solid",
            bd=2,
            wrap="word"
        )
        self.input_text.pack(fill="x", pady=5)
        self.input_text.bind('<KeyPress>', self.on_key_press)
        self.input_text.bind('<KeyRelease>', self.on_key_release)
        
        # Buttons frame - like a control panel
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)
        
        self.new_test_btn = tk.Button(
            button_frame,
            text="🔄 New Test",
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10,
            command=self.new_test,
            relief="raised",
            bd=3
        )
        self.new_test_btn.pack(side="left", padx=10)
        
        self.reset_btn = tk.Button(
            button_frame,
            text="🗑️ Reset",
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=20,
            pady=10,
            command=self.reset_test,
            relief="raised",
            bd=3
        )
        self.reset_btn.pack(side="left", padx=10)
        
        # Results frame - like a scoreboard
        results_frame = tk.Frame(self.root, bg="#ecf0f1", relief="solid", bd=2)
        results_frame.pack(pady=20, padx=40, fill="x")
        
        tk.Label(
            results_frame,
            text="📊 Results",
            font=("Arial", 14, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50"
        ).pack(pady=(10, 5))
        
        # Results display - like a dashboard
        self.results_display = tk.Label(
            results_frame,
            text="Start typing to see your results!",
            font=("Arial", 12),
            bg="#ecf0f1",
            fg="#34495e",
            justify="center"
        )
        self.results_display.pack(pady=10)
    
    def new_test(self):
        """Start a new typing test - like shuffling cards for a new game"""
        self.current_sentence = random.choice(self.sentences)
        self.text_display.config(text=self.current_sentence)
        self.reset_test()
    
    def reset_test(self):
        """Reset the current test - like clearing the board"""
        self.input_text.delete(1.0, tk.END)
        self.start_time = None
        self.is_testing = False
        self.correct_chars = 0
        self.total_chars = 0
        self.results_display.config(text="Start typing to see your results!")
        self.input_text.focus()
    
    def on_key_press(self, event):
        """Handle when a key is pressed - like starting a stopwatch"""
        if not self.is_testing and event.char.isprintable():
            self.start_time = time.time()
            self.is_testing = True
    
    def on_key_release(self, event):
        """Handle when a key is released - like checking your work"""
        if not self.is_testing:
            return
        
        # Get what the user has typed so far
        user_text = self.input_text.get(1.0, tk.END).rstrip('\n')
        
        # Calculate accuracy - like grading a test
        self.total_chars = len(user_text)
        self.correct_chars = 0
        
        # Compare character by character - like checking each answer
        for i, char in enumerate(user_text):
            if i < len(self.current_sentence) and char == self.current_sentence[i]:
                self.correct_chars += 1
        
        # Calculate and display results - like showing the score
        self.update_results()
        
        # Check if test is complete
        if user_text == self.current_sentence:
            self.complete_test()
    
    def update_results(self):
        """Update the results display - like updating a scoreboard"""
        if not self.start_time:
            return
        
        # Calculate time elapsed - like checking a timer
        time_elapsed = time.time() - self.start_time
        minutes = time_elapsed / 60
        
        # Calculate WPM (Words Per Minute) - standard typing measurement
        # We divide by 5 because average word length is 5 characters
        words_typed = self.correct_chars / 5
        wpm = words_typed / minutes if minutes > 0 else 0
        
        # Calculate accuracy - like a percentage grade
        accuracy = (self.correct_chars / self.total_chars * 100) if self.total_chars > 0 else 100
        
        # Update display - like updating a digital scoreboard
        results_text = f"🚀 Speed: {wpm:.1f} WPM  |  🎯 Accuracy: {accuracy:.1f}%  |  ⏱️ Time: {time_elapsed:.1f}s"
        self.results_display.config(text=results_text)
    
    def complete_test(self):
        """Handle test completion - like crossing the finish line"""
        self.is_testing = False
        
        # Calculate final results
        time_elapsed = time.time() - self.start_time
        minutes = time_elapsed / 60
        words_typed = len(self.current_sentence.split())
        wpm = words_typed / minutes if minutes > 0 else 0
        
        # Show completion message - like a victory celebration
        messagebox.showinfo(
            "Test Complete! 🎉",
            f"Congratulations! You completed the test!\n\n"
            f"⚡ Final Speed: {wpm:.1f} WPM\n"
            f"🎯 Accuracy: 100%\n"
            f"⏱️ Time: {time_elapsed:.1f} seconds\n\n"
            f"Click 'New Test' to try another challenge!"
        )

def main():
    # Create the main window - like opening a new application
    root = tk.Tk()
    app = TypingSpeedTest(root)
    
    # Start the application - like turning on a machine
    root.mainloop()

if __name__ == "__main__":
    main()