from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    img_array = np.array(image)

    encrypted_array = (img_array + key) % 256

    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully!")


def decrypt_image(image_path, key):
    image = Image.open(image_path)
    img_array = np.array(image)

    decrypted_array = (img_array - key) % 256

    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully!")


choice = input("Enter 'encrypt' or 'decrypt': ").lower()
image_path = input("Enter image path: ")
key = int(input("Enter key value (0–255): "))

if choice == "encrypt":
    encrypt_image(image_path, key)
elif choice == "decrypt":
    decrypt_image(image_path, key)
else:
    print("Invalid choice!")
