import qrcode

# Create a QR code with a specific URL or text
data = "https://rumble.com/v5em78d-after-hours-w-hangingwithken.html?e9s=src_v1_ucp"  # Replace with your data
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code, 1 is the smallest
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box (pixel size)
    border=4,  # thickness of the border
)

qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("qr_code.png")
