from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)
    
    
    encrypted_pixels = (pixels + key) % 50
    
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(encrypted_image_path, output_path, key):
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_pixels = np.array(encrypted_image)
    
    
    decrypted_pixels = (encrypted_pixels - key) % 100
    
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")


encrypt_image('input_image.png', 'encrypted_image.png', 50)
decrypt_image('encrypted_image.png', 'decrypted_image.png', 100)