import qrcode

def generate_qr():
    print("🔳 QR Code Generator 🔳")
    data = input("Enter the text or link to generate QR code: ").strip()
    if not data:
        print("⚠️ Input cannot be empty!")
        return

    filename = input("Enter output file name (without extension): ").strip() or "my_qr_code"
    img = qrcode.make(data)
    img.save(f"{filename}.png")

    print(f"✅ QR code generated and saved as '{filename}.png'")

if __name__ == "__main__":
    generate_qr()
