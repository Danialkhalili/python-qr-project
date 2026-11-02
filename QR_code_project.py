
import qrcode
import os

# GitHub repository link
repository_link = "https://github.com/Danialkhalili/python-qr-project.git"

# Folder and image name
folder_name = "generated_qrcodes"
file_name = "github_repository_qr.png"

# Create the full path
full_path = os.path.join(folder_name, file_name)

# Create the folder if it does not exist
os.makedirs(folder_name, exist_ok=True)

# Create QR Code
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Add repository link
qr.add_data(repository_link)
qr.make(fit=True)

# Create QR Code image
img = qr.make_image(
    fill_color="black",
    back_color="white"
)

# Save the image
img.save(full_path)

# Display success message
print("QR Code created successfully!")
print(f"Saved at: {os.path.abspath(full_path)}")
