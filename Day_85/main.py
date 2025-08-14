import tkinter as tk
from tkinter import ttk, filedialog, messagebox, colorchooser
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermark Studio")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Variables to store our data
        self.original_image = None
        self.watermarked_image = None
        self.preview_image = None
        self.watermark_text = tk.StringVar(value="© Your Watermark")
        self.font_size = tk.IntVar(value=36)
        self.opacity = tk.IntVar(value=128)  # 0-255 scale
        self.text_color = "#FFFFFF"  # White by default
        
        self.setup_gui()
    
    def setup_gui(self):
        """Create all the buttons, labels, and layout"""
        # Title
        title_label = tk.Label(self.root, text="🖼️ Image Watermark Studio", 
                              font=("Arial", 16, "bold"), bg='#f0f0f0')
        title_label.pack(pady=10)
        
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Left side - Controls
        controls_frame = ttk.LabelFrame(main_frame, text="Watermark Controls", padding=10)
        controls_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        # Upload button
        upload_btn = ttk.Button(controls_frame, text="📁 Upload Image", 
                               command=self.upload_image, width=20)
        upload_btn.pack(pady=5)
        
        # Watermark text input
        ttk.Label(controls_frame, text="Watermark Text:").pack(pady=(10, 2))
        text_entry = ttk.Entry(controls_frame, textvariable=self.watermark_text, width=25)
        text_entry.pack(pady=2)
        
        # Font size slider
        ttk.Label(controls_frame, text="Font Size:").pack(pady=(10, 2))
        font_slider = ttk.Scale(controls_frame, from_=12, to=72, 
                               variable=self.font_size, orient=tk.HORIZONTAL)
        font_slider.pack(fill=tk.X, pady=2)
        ttk.Label(controls_frame, textvariable=self.font_size).pack()
        
        # Opacity slider
        ttk.Label(controls_frame, text="Opacity (Transparency):").pack(pady=(10, 2))
        opacity_slider = ttk.Scale(controls_frame, from_=50, to=255, 
                                  variable=self.opacity, orient=tk.HORIZONTAL)
        opacity_slider.pack(fill=tk.X, pady=2)
        ttk.Label(controls_frame, textvariable=self.opacity).pack()
        
        # Color picker button
        color_btn = ttk.Button(controls_frame, text="🎨 Choose Text Color", 
                              command=self.choose_color, width=20)
        color_btn.pack(pady=10)
        
        # Preview button
        preview_btn = ttk.Button(controls_frame, text="👁️ Preview Watermark", 
                                command=self.preview_watermark, width=20)
        preview_btn.pack(pady=5)
        
        # Save button
        save_btn = ttk.Button(controls_frame, text="💾 Save Image", 
                             command=self.save_image, width=20)
        save_btn.pack(pady=5)
        
        # Right side - Image preview
        self.preview_frame = ttk.LabelFrame(main_frame, text="Image Preview", padding=10)
        self.preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Canvas for image display
        self.canvas = tk.Canvas(self.preview_frame, bg='white', width=400, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Instructions label
        self.info_label = ttk.Label(self.preview_frame, 
                                   text="Upload an image to get started!", 
                                   foreground='gray')
        self.info_label.pack(pady=10)
    
    def upload_image(self):
        """Let user select an image file"""
        file_types = [
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff"),
            ("All files", "*.*")
        ]
        
        filename = filedialog.askopenfilename(
            title="Select an image",
            filetypes=file_types
        )
        
        if filename:
            try:
                # Load the image
                self.original_image = Image.open(filename)
                self.display_image(self.original_image)
                self.info_label.config(text=f"Loaded: {os.path.basename(filename)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open image: {str(e)}")
    
    def display_image(self, image):
        """Show image in the canvas, resized to fit"""
        if not image:
            return
            
        # Calculate size to fit in canvas while keeping aspect ratio
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # If canvas isn't ready, use default size
        if canvas_width <= 1:
            canvas_width = 400
            canvas_height = 400
        
        # Calculate the scaling factor
        img_width, img_height = image.size
        scale_x = canvas_width / img_width
        scale_y = canvas_height / img_height
        scale = min(scale_x, scale_y, 1.0)  # Don't scale up
        
        # Resize image
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        display_img = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage for tkinter
        self.preview_image = ImageTk.PhotoImage(display_img)
        
        # Clear canvas and show image
        self.canvas.delete("all")
        self.canvas.create_image(canvas_width//2, canvas_height//2, 
                               image=self.preview_image, anchor=tk.CENTER)
    
    def choose_color(self):
        """Open color picker for text color"""
        color = colorchooser.askcolor(title="Choose watermark color")
        if color[1]:  # color[1] is the hex value
            self.text_color = color[1]
    
    def preview_watermark(self):
        """Create and show watermarked image"""
        if not self.original_image:
            messagebox.showwarning("Warning", "Please upload an image first!")
            return
        
        try:
            # Create a copy of the original image
            watermarked = self.original_image.copy()
            
            # Create a transparent overlay for the text
            overlay = Image.new('RGBA', watermarked.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(overlay)
            
            # Try to load a font, fall back to default if not available
            try:
                font = ImageFont.truetype("arial.ttf", self.font_size.get())
            except:
                try:
                    font = ImageFont.load_default()
                except:
                    font = ImageFont.load_default()
            
            # Get text size for positioning
            text = self.watermark_text.get()
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            # Position text in bottom right corner
            x = watermarked.size[0] - text_width - 20
            y = watermarked.size[1] - text_height - 20
            
            # Convert hex color to RGB
            hex_color = self.text_color.lstrip('#')
            rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            text_color = rgb_color + (self.opacity.get(),)  # Add alpha
            
            # Draw the text on overlay
            draw.text((x, y), text, fill=text_color, font=font)
            
            # Combine original image with overlay
            if watermarked.mode != 'RGBA':
                watermarked = watermarked.convert('RGBA')
            
            self.watermarked_image = Image.alpha_composite(watermarked, overlay)
            
            # Display the watermarked image
            self.display_image(self.watermarked_image)
            self.info_label.config(text="Preview ready! You can now save the image.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not create watermark: {str(e)}")
    
    def save_image(self):
        """Save the watermarked image"""
        if not self.watermarked_image:
            messagebox.showwarning("Warning", "Please preview the watermark first!")
            return
        
        # Ask user where to save
        filename = filedialog.asksaveasfilename(
            title="Save watermarked image",
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            try:
                # Convert back to RGB if saving as JPEG
                if filename.lower().endswith(('.jpg', '.jpeg')):
                    # Create white background for JPEG
                    rgb_image = Image.new('RGB', self.watermarked_image.size, (255, 255, 255))
                    rgb_image.paste(self.watermarked_image, mask=self.watermarked_image.split()[-1])
                    rgb_image.save(filename, quality=95)
                else:
                    self.watermarked_image.save(filename)
                
                messagebox.showinfo("Success", f"Image saved as: {filename}")
                self.info_label.config(text=f"Saved: {os.path.basename(filename)}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not save image: {str(e)}")

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()