import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import time

class DisappearingWriter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Write or Die - Keep Typing!")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Settings
        self.timeout_seconds = 5  # How long before text starts disappearing
        self.last_keypress = time.time()
        self.is_writing = False
        self.timer_thread = None
        
        self.setup_ui()
        self.start_timer()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="🔥 WRITE OR DIE 🔥", 
            font=("Arial", 24, "bold"),
            fg='#e74c3c',
            bg='#2c3e50'
        )
        title_label.pack(pady=10)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Keep typing or your words will disappear! You have 5 seconds between keystrokes.",
            font=("Arial", 12),
            fg='#ecf0f1',
            bg='#2c3e50',
            wraplength=700
        )
        instructions.pack(pady=5)
        
        # Timer display
        self.timer_label = tk.Label(
            self.root,
            text="Timer: 5.0s",
            font=("Arial", 14, "bold"),
            fg='#2ecc71',
            bg='#2c3e50'
        )
        self.timer_label.pack(pady=5)
        
        # Text area frame
        text_frame = tk.Frame(self.root, bg='#2c3e50')
        text_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Text area
        self.text_area = tk.Text(
            text_frame,
            font=("Arial", 14),
            bg='#ecf0f1',
            fg='#2c3e50',
            insertbackground='#e74c3c',
            wrap='word',
            padx=10,
            pady=10
        )
        self.text_area.pack(side='left', expand=True, fill='both')
        
        # Scrollbar
        scrollbar = tk.Scrollbar(text_frame, command=self.text_area.yview)
        scrollbar.pack(side='right', fill='y')
        self.text_area.config(yscrollcommand=scrollbar.set)
        
        # Bind keypress events
        self.text_area.bind('<KeyPress>', self.on_keypress)
        self.text_area.bind('<Button-1>', self.on_click)
        
        # Control buttons frame
        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.pack(pady=10)
        
        # Save button
        save_btn = tk.Button(
            button_frame,
            text="💾 Save Work",
            font=("Arial", 12),
            bg='#27ae60',
            fg='white',
            command=self.save_work,
            padx=20
        )
        save_btn.pack(side='left', padx=5)
        
        # Settings button
        settings_btn = tk.Button(
            button_frame,
            text="⚙️ Settings",
            font=("Arial", 12),
            bg='#3498db',
            fg='white',
            command=self.show_settings,
            padx=20
        )
        settings_btn.pack(side='left', padx=5)
        
        # Word count
        self.word_count_label = tk.Label(
            self.root,
            text="Words: 0",
            font=("Arial", 10),
            fg='#bdc3c7',
            bg='#2c3e50'
        )
        self.word_count_label.pack(pady=5)
        
        # Focus on text area
        self.text_area.focus_set()
    
    def on_keypress(self, event):
        """Called when user types"""
        self.last_keypress = time.time()
        if not self.is_writing:
            self.is_writing = True
        
        # Update word count after a short delay
        self.root.after(100, self.update_word_count)
    
    def on_click(self, event):
        """Called when user clicks in text area"""
        self.last_keypress = time.time()
    
    def update_word_count(self):
        """Update the word count display"""
        content = self.text_area.get('1.0', 'end-1c')
        word_count = len(content.split()) if content.strip() else 0
        self.word_count_label.config(text=f"Words: {word_count}")
    
    def start_timer(self):
        """Start the countdown timer"""
        if self.timer_thread and self.timer_thread.is_alive():
            return
            
        self.timer_thread = threading.Thread(target=self.timer_loop, daemon=True)
        self.timer_thread.start()
    
    def timer_loop(self):
        """Main timer loop that runs in background"""
        while True:
            try:
                time_since_keypress = time.time() - self.last_keypress
                remaining_time = max(0, self.timeout_seconds - time_since_keypress)
                
                # Update timer display
                self.root.after(0, lambda: self.update_timer_display(remaining_time))
                
                # Check if we should start deleting
                if remaining_time <= 0 and self.is_writing:
                    content = self.text_area.get('1.0', 'end-1c')
                    if content.strip():  # Only delete if there's content
                        self.root.after(0, self.delete_character)
                
                time.sleep(0.1)  # Update 10 times per second
                
            except Exception as e:
                print(f"Timer error: {e}")
                break
    
    def update_timer_display(self, remaining_time):
        """Update the timer display"""
        if remaining_time > 2:
            color = '#2ecc71'  # Green
        elif remaining_time > 1:
            color = '#f39c12'  # Orange
        else:
            color = '#e74c3c'  # Red
            
        self.timer_label.config(
            text=f"Timer: {remaining_time:.1f}s",
            fg=color
        )
    
    def delete_character(self):
        """Delete one character from the end"""
        try:
            content = self.text_area.get('1.0', 'end-1c')
            if content:
                # Delete last character
                self.text_area.delete('end-2c', 'end-1c')
                
                # Flash the background red briefly
                original_bg = self.text_area.cget('bg')
                self.text_area.config(bg='#ffebee')
                self.root.after(100, lambda: self.text_area.config(bg=original_bg))
                
                # Update word count
                self.update_word_count()
                
        except tk.TclError:
            pass  # Text widget might be destroyed
    
    def save_work(self):
        """Save the current work to a file"""
        content = self.text_area.get('1.0', 'end-1c')
        if not content.strip():
            messagebox.showwarning("Nothing to Save", "There's no text to save!")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                messagebox.showinfo("Saved!", f"Your work has been saved to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")
    
    def show_settings(self):
        """Show settings dialog"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("300x150")
        settings_window.configure(bg='#2c3e50')
        settings_window.transient(self.root)
        
        # Timeout setting
        tk.Label(
            settings_window,
            text="Seconds before deletion:",
            fg='white',
            bg='#2c3e50'
        ).pack(pady=10)
        
        timeout_var = tk.IntVar(value=self.timeout_seconds)
        timeout_scale = tk.Scale(
            settings_window,
            from_=1,
            to=10,
            orient='horizontal',
            variable=timeout_var,
            bg='#34495e',
            fg='white',
            highlightbackground='#2c3e50'
        )
        timeout_scale.pack(pady=10)
        
        def apply_settings():
            self.timeout_seconds = timeout_var.get()
            settings_window.destroy()
        
        apply_btn = tk.Button(
            settings_window,
            text="Apply",
            command=apply_settings,
            bg='#27ae60',
            fg='white'
        )
        apply_btn.pack(pady=10)
    
    def run(self):
        """Start the application"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("Application closed.")

if __name__ == "__main__":
    print("Starting Write or Die application...")
    print("Remember: Keep typing or your words will disappear!")
    
    app = DisappearingWriter()
    app.run()