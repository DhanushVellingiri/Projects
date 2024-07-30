import qrcode

def generate_qr_code(data, filename="qrcode.png"):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)
    print(f"QR Code generated and saved as {filename}")

# Example usage
if __name__ == "__main__":
    data = input("Enter the data to encode in the QR code: ")
    filename = input("Enter the filename to save the QR code (with .png extension): ")
    generate_qr_code(data, filename)
