import qrcode

def generate_qr_code(data, file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file)

# Example usage
data = input("Enter website or text for QR code: ")
filepath = "" 
filename = input("Enter the filename for the QR code: ")
file = f"{filepath}/{filename}.png"
generate_qr_code(data, file)
print(f"QR code saved as {filename} in {filepath}")
