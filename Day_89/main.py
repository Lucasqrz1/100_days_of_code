import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("500x600")
        self.root.configure(bg='#f0f0f0')
        
        # Data storage
        self.todos = []
        self.data_file = "todos.json"
        
        # Load existing todos
        self.load_todos()
        
        # Create UI
        self.create_widgets()
        self.refresh_display()
        
        # Bind events
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="📋 Todo List", 
            font=("Arial", 20, "bold"),
            bg='#f0f0f0',
            fg='#333'
        )
        title_label.pack(pady=20)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(fill='x', padx=20, pady=10)
        
        self.task_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            relief='flat',
            bd=5,
            bg='white'
        )
        self.task_entry.pack(side='left', fill='x', expand=True, ipady=8)
        self.task_entry.bind('<Return>', lambda e: self.add_task())
        
        add_button = tk.Button(
            input_frame,
            text="Add Task",
            font=("Arial", 10, "bold"),
            bg='#4CAF50',
            fg='white',
            relief='flat',
            padx=20,
            command=self.add_task
        )
        add_button.pack(side='right', padx=(10, 0))
        
        # Stats frame
        stats_frame = tk.Frame(self.root, bg='#f0f0f0')
        stats_frame.pack(fill='x', padx=20, pady=10)
        
        self.stats_label = tk.Label(
            stats_frame,
            text="Total: 0 | Completed: 0 | Remaining: 0",
            font=("Arial", 10),
            bg='#f0f0f0',
            fg='#666'
        )
        self.stats_label.pack()
        
        # Scrollable frame for todos
        canvas_frame = tk.Frame(self.root, bg='#f0f0f0')
        canvas_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.canvas = tk.Canvas(canvas_frame, bg='#f0f0f0', highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient='vertical', command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg='#f0f0f0')
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind mousewheel to canvas
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        
        # Clear completed button
        clear_button = tk.Button(
            self.root,
            text="Clear Completed Tasks",
            font=("Arial", 10),
            bg='#ff6b6b',
            fg='white',
            relief='flat',
            pady=8,
            command=self.clear_completed
        )
        clear_button.pack(pady=10)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Warning", "Please enter a task!")
            return
        
        if len(task_text) > 100:
            messagebox.showwarning("Warning", "Task is too long! Maximum 100 characters.")
            return
        
        new_task = {
            'id': len(self.todos) + 1,
            'text': task_text,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.todos.append(new_task)
        self.task_entry.delete(0, tk.END)
        self.refresh_display()
        self.save_todos()

    def toggle_task(self, task_id):
        for todo in self.todos:
            if todo['id'] == task_id:
                todo['completed'] = not todo['completed']
                break
        self.refresh_display()
        self.save_todos()

    def delete_task(self, task_id):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?"):
            self.todos = [todo for todo in self.todos if todo['id'] != task_id]
            self.refresh_display()
            self.save_todos()

    def clear_completed(self):
        completed_count = sum(1 for todo in self.todos if todo['completed'])
        if completed_count == 0:
            messagebox.showinfo("Info", "No completed tasks to clear!")
            return
        
        if messagebox.askyesno("Confirm Clear", f"Delete {completed_count} completed task(s)?"):
            self.todos = [todo for todo in self.todos if not todo['completed']]
            self.refresh_display()
            self.save_todos()

    def refresh_display(self):
        # Clear existing widgets
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        if not self.todos:
            empty_label = tk.Label(
                self.scrollable_frame,
                text="📝 No tasks yet!\nAdd one above to get started.",
                font=("Arial", 12),
                fg='#888',
                bg='#f0f0f0',
                justify='center'
            )
            empty_label.pack(pady=50)
        else:
            for todo in self.todos:
                self.create_todo_item(todo)
        
        self.update_stats()

    def create_todo_item(self, todo):
        # Main task frame
        task_frame = tk.Frame(
            self.scrollable_frame,
            bg='white',
            relief='raised',
            bd=1
        )
        task_frame.pack(fill='x', pady=5, padx=10)
        
        # Checkbox
        var = tk.BooleanVar(value=todo['completed'])
        checkbox = tk.Checkbutton(
            task_frame,
            variable=var,
            command=lambda: self.toggle_task(todo['id']),
            bg='white',
            activebackground='white',
            font=("Arial", 12)
        )
        checkbox.pack(side='left', padx=10, pady=10)
        
        # Task text
        text_color = '#888' if todo['completed'] else '#333'
        font_style = ("Arial", 11, "overstrike") if todo['completed'] else ("Arial", 11)
        
        task_label = tk.Label(
            task_frame,
            text=todo['text'],
            font=font_style,
            fg=text_color,
            bg='white',
            anchor='w',
            justify='left',
            wraplength=300
        )
        task_label.pack(side='left', fill='x', expand=True, padx=5, pady=10)
        
        # Date label
        date_label = tk.Label(
            task_frame,
            text=todo['created_at'],
            font=("Arial", 8),
            fg='#999',
            bg='white'
        )
        date_label.pack(side='right', padx=5, pady=5)
        
        # Delete button
        delete_btn = tk.Button(
            task_frame,
            text="×",
            font=("Arial", 14, "bold"),
            fg='white',
            bg='#ff6b6b',
            width=3,
            relief='flat',
            command=lambda: self.delete_task(todo['id'])
        )
        delete_btn.pack(side='right', padx=10, pady=10)

    def update_stats(self):
        total = len(self.todos)
        completed = sum(1 for todo in self.todos if todo['completed'])
        remaining = total - completed
        
        self.stats_label.config(
            text=f"Total: {total} | Completed: {completed} | Remaining: {remaining}"
        )

    def save_todos(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.todos, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save todos: {str(e)}")

    def load_todos(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    self.todos = json.load(f)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load todos: {str(e)}")
            self.todos = []

    def on_closing(self):
        self.save_todos()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()