# 🖼️ PRODIGY_CS_02 - Image Encryption Tool

A simple yet powerful image encryption tool using pixel-level transformations, developed for **Cybersecurity Task 2** of the Prodigy Infotech Internship program.

## 🔐 Overview

This project demonstrates fundamental image encryption/decryption through RGB pixel manipulation. The tool performs reversible transformations on image pixels, serving as an educational introduction to image processing and basic cryptographic concepts.

## ✨ Features

- **Symmetric Encryption**: Uses the same operation for both encryption and decryption
- **Pixel-level Security**: Manipulates individual RGB values for transformation
- **Format Support**: Works with JPEG, PNG, and other common formats
- **Lightweight**: Minimal dependencies (only Pillow required)
- **Educational**: Demonstrates core image processing concepts

## 🛠️ Technical Implementation

The encryption applies the following reversible transformation to each pixel:

```math
(R, G, B) → (255 - R, 255 - G, 255 - B)

Installation
git clone https://github.com/Akshay-kallada/PRODIGY_CS_02.git
cd PRODIGY_CS_02

Install dependencies:
pip install pillow

🚀 Usage

Command Line Interface:
# Encrypt an image
python image_encryptor.py encrypt input.jpg encrypted.jpg

# Decrypt an image
python image_encryptor.py decrypt encrypted.jpg decrypted.jpg

As a Python Module:
from image_encryptor import invert_rgb

# Encrypt/decrypt an image
invert_rgb('input.jpg', 'output.jpg')

📂 File Structure
PRODIGY_CS_02/
├── image_encryptor.py     # Main encryption/decryption script
├── input.jpg              # Sample input image
├── encrypted.jpg          # Encrypted output
├── decrypted.jpg          # Result after decryption
├── requirements.txt       # Dependencies file
└── README.md              # Project documentation

🎯 Learning Outcomes
Understand how pixel data is stored and manipulated
Learn basic image processing with Python
Practice building symmetrical encryption logic
Improve GitHub collaboration and documentation skills

🛡️ Disclaimer
This project is meant for educational purposes only and should not be used in production environments. It does not offer cryptographic security.
