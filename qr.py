import qrcode

# Creating a QR Code for an example URL
url = "https://cram-7tks.onrender.com/"

# Generate QR Code
qr = qrcode.QRCode(
    version=1,  # version 1: 21x21 matrix
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # L: 7% error correction
    box_size=10,  # size of each box in pixels
    border=4,  # border size in boxes
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("qr_code_example.png")