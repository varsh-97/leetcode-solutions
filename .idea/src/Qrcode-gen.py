# Reimport necessary library and regenerate the QR code after state reset
import qrcode

# Google Drive link provided by the user
google_drive_link = "<<your drive link>>"

# Generating the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(google_drive_link)
qr.make(fit=True)

# Save the QR code as an image
qr_image_path = "/mnt/data/google_drive_qr.png"
qr_image = qr.make_image(fill_color="black", back_color="white")
qr_image.save(qr_image_path)

qr_image_path
