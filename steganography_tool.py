import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import tkinter.font as tkFont

# Enable DPI Awareness for Windows
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Helper Functions for Encoding and Decoding
def text_to_bin(text):
    return ''.join(format(ord(char), '08b') for char in text)

def bin_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def encode_image(image_path, message, output_path):
    try:
        image = Image.open(image_path)
        encoded_image = image.copy()

        width, height = image.size
        total_pixels = width * height

        binary_message = text_to_bin(message) + '1111111111111110'

        # Check if the message is too long for the image's capacity
        if len(binary_message) > total_pixels * 3:
            messagebox.showerror("Error", "Message is too long to be hidden in this image.")
            return

        data_index = 0
        for y in range(height):
            for x in range(width):
                pixel = list(image.getpixel((x, y)))
                for n in range(3):  # Iterate over R, G, B channels
                    if data_index < len(binary_message):
                        pixel[n] = (pixel[n] & ~1) | int(binary_message[data_index])
                        data_index += 1
                encoded_image.putpixel((x, y), tuple(pixel))

        encoded_image.save(output_path, format='PNG')
        messagebox.showinfo("Success", f"Message encoded and saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to encode image: {str(e)}")

def decode_image(encoded_image_path):
    try:
        image = Image.open(encoded_image_path)

        width, height = image.size
        binary_message = ""

        for y in range(height):
            for x in range(width):
                pixel = list(image.getpixel((x, y)))
                for n in range(3):  # Iterate over R, G, B channels
                    binary_message += str(pixel[n] & 1)

        delimiter = '1111111111111110'
        end_index = binary_message.find(delimiter)

        if end_index != -1:
            binary_message = binary_message[:end_index]
        else:
            raise ValueError("No hidden message found in the image.")

        message = bin_to_text(binary_message)
        return message
    except Exception as e:
        messagebox.showerror("Error", f"Failed to decode image: {str(e)}")
        return ""

# GUI Implementation
class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Encoder/Decoder")
        self.root.geometry("700x400")  # Increase the size of the window
        self.root.resizable(False, False)

        # Define a custom font for better clarity
        self.custom_font = tkFont.Font(family="Helvetica", size=11, weight="bold")

        # Encode Frame
        self.encode_frame = tk.LabelFrame(root, text="Encode Message", padx=10, pady=10, font=self.custom_font)
        self.encode_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.select_image_button = tk.Button(self.encode_frame, text="Select Image", command=self.select_image, font=self.custom_font)
        self.select_image_button.grid(row=0, column=0, pady=5, padx=5, sticky="w")

        self.selected_image_label = tk.Label(self.encode_frame, text="No image selected", font=self.custom_font)
        self.selected_image_label.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        self.message_label = tk.Label(self.encode_frame, text="Message to Hide:", font=self.custom_font)
        self.message_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")

        self.message_entry = tk.Entry(self.encode_frame, width=45, font=self.custom_font)
        self.message_entry.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

        self.output_path_label = tk.Label(self.encode_frame, text="Output Path:", font=self.custom_font)
        self.output_path_label.grid(row=2, column=0, pady=5, padx=5, sticky="w")

        self.output_entry = tk.Entry(self.encode_frame, width=30, font=self.custom_font)
        self.output_entry.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        self.browse_output_button = tk.Button(self.encode_frame, text="Browse", command=self.browse_output_path, font=self.custom_font)
        self.browse_output_button.grid(row=2, column=2, pady=5, padx=5, sticky="w")

        self.encode_button = tk.Button(self.encode_frame, text="Encode", command=self.encode_message, font=self.custom_font)
        self.encode_button.grid(row=3, columnspan=3, pady=10)

        # Decode Frame
        self.decode_frame = tk.LabelFrame(root, text="Decode Message", padx=10, pady=10, font=self.custom_font)
        self.decode_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.decode_image_button = tk.Button(self.decode_frame, text="Select Encoded Image", command=self.select_encoded_image, font=self.custom_font)
        self.decode_image_button.grid(row=0, column=0, pady=5, padx=5, sticky="w")

        self.encoded_image_label = tk.Label(self.decode_frame, text="No encoded image selected", font=self.custom_font)
        self.encoded_image_label.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        self.decode_button = tk.Button(self.decode_frame, text="Decode", command=self.decode_message, font=self.custom_font)
        self.decode_button.grid(row=1, columnspan=2, pady=10)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if self.image_path:
            self.selected_image_label.config(text=os.path.basename(self.image_path))

    def browse_output_path(self):
        output_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            title="Save Encoded Image"
        )
        if output_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, output_path)

    def select_encoded_image(self):
        self.encoded_image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png")])
        if self.encoded_image_path:
            self.encoded_image_label.config(text=os.path.basename(self.encoded_image_path))

    def encode_message(self):
        if hasattr(self, 'image_path') and self.message_entry.get() and self.output_entry.get():
            encode_image(self.image_path, self.message_entry.get(), self.output_entry.get())
        else:
            messagebox.showerror("Error", "Please fill all fields and select an image.")

    def decode_message(self):
        if hasattr(self, 'encoded_image_path'):
            message = decode_image(self.encoded_image_path)
            if message:
                messagebox.showinfo("Decoded Message", message)
        else:
            messagebox.showerror("Error", "Please select an encoded image.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
