def read_image(image_path):
    with open(image_path, 'rb') as f:
        return f.read()

def write_image(image_data, output_path):
    with open(output_path, 'wb') as f:
        f.write(image_data)

def encrypt_image(image_path, output_path):
    image_data = read_image(image_path)
    encrypted_data = bytearray(image_data)
    for i in range(0, len(encrypted_data), 3):
        if i + 1 < len(encrypted_data):
            encrypted_data[i], encrypted_data[i + 1] = encrypted_data[i + 1], encrypted_data[i]
    write_image(encrypted_data, output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path):
    image_data = read_image(image_path)
    decrypted_data = bytearray(image_data)
    for i in range(0, len(decrypted_data), 3):
        if i + 1 < len(decrypted_data):
            decrypted_data[i], decrypted_data[i + 1] = decrypted_data[i + 1], decrypted_data[i]
    write_image(decrypted_data, output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    while True:
        mode = input("Do you want to encrypt or decrypt an image? (enter 'encrypt', 'decrypt', or 'exit' to quit): ").lower()
        if mode not in ['encrypt', 'decrypt', 'exit']:
            print("Invalid choice. Please enter 'encrypt', 'decrypt', or 'exit'.")
            continue
        if mode == 'exit':
            break

        image_path = input("Enter the path to the image: ")
        output_path = input(f"Enter the output path for the {mode}ed image: ")

        if mode == 'encrypt':
            encrypt_image(image_path, output_path)
        elif mode == 'decrypt':
            decrypt_image(image_path, output_path)

if __name__ == "__main__":
    main()
