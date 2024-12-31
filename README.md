
# 🖼️ Image-Based Steganography Encoder/Decoder

A Python-based project implementing **image steganography** using the **Least Significant Bit (LSB)** technique. Hide and retrieve secret messages within images without significantly altering their visual quality!

---

## 🚀 Features
- **Encode messages:** Hide secret messages in images securely.
- **Decode messages:** Retrieve hidden messages from encoded images.
- **Error handling:** Prevents encoding if the message exceeds image capacity.
- **User-friendly GUI:** Simple interface for selecting images, encoding messages, and decoding them.
- **Preserves image quality:** Ensures minimal visual distortion when encoding.

---

## 🛠️ Technologies Used
- **Python 3.8+**
- **Pillow (PIL):** For image manipulation.
- **Tkinter:** For creating the graphical user interface.

---

## 📁 File Structure
- `steganography_tool.py` - Main application script.
- `requirements.txt` - Dependencies for the project.

---

## 🖥️ GUI Overview
1. **Encode Tab**:
   - Select an image to encode.
   - Add a secret message.
   - Specify an output path.
2. **Decode Tab**:
   - Select an encoded image.
   - Retrieve and display the hidden message.

---

## 📖 How It Works
### Encoding
1. Converts the message into binary.
2. Modifies the least significant bit of each pixel channel (R, G, B) to store the binary message.
3. Stops encoding when the message is fully stored.

### Decoding
1. Extracts the least significant bit of each pixel channel.
2. Combines these bits to reconstruct the binary message.
3. Stops decoding when the delimiter (`1111111111111110`) is found.

---

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Rohan-Patalay/Steganography-tool.git
   ```
2. Navigate to the directory:
   ```bash
   cd Steganography-tool
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python steganography_tool.py
   ```

---

## 🎨 Screenshots

-**Main Application Interface**

  ![interface_main](https://github.com/user-attachments/assets/d14b5e99-c468-408c-a097-8f002775ae3d)

-**Image Selection**

  ![image_selection](https://github.com/user-attachments/assets/d24bcb47-0531-4310-9f92-81a9738545ae)

-**Demonstration**

  ![test_execution](https://github.com/user-attachments/assets/259ad2a7-4fed-45bc-b279-d971c01cb3ea)

  ![encoding_success_msg](https://github.com/user-attachments/assets/26ef0e34-d79b-4d02-8020-6e053811a832)

  ![decoding_success_msg](https://github.com/user-attachments/assets/46d189ad-b4f4-4583-8593-d764f2f76dd6)


## 🛡️ Error Handling
- Ensures the message size does not exceed the encoding capacity of the image.
- Provides meaningful error messages for unsupported formats or incorrect operations.

---

## 🛠️ Future Enhancements
- Add support for other file formats (e.g., `.bmp`, `.gif`).
- Implement password-protected encoding/decoding.
- Add a feature to hide other file types (e.g., PDFs or text files).

---

## 👨‍💻 Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

---

## ⚠️ Disclaimer
This project is for educational purposes only. Please use responsibly.

---

## 🌟 Acknowledgments
Special thanks to open-source libraries like Pillow and Tkinter that made this project possible.

