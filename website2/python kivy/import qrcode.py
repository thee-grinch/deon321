import qrcode

def create_whatsapp_qr_code(phone_number):
    # Format the URL for the WhatsApp contact
    whatsapp_url = f'https://wa.me/{+254702248984}'

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(whatsapp_url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save or display the QR code image
    img.save("whatsapp_qr_code.png")
    img.show()

if __name__ == '__main__':
    # Replace '1234567890' with the desired phone number
    create_whatsapp_qr_code('+2540702248984')
