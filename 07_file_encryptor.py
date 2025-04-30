import base64

choice = input("Encrypt or Decrypt (e/d)? ").lower()
file_name = input("Enter filename: ")

if choice == 'e':
    with open(file_name, 'rb') as file:
        encoded = base64.b64encode(file.read())
    with open(file_name + '.enc', 'wb') as file:
        file.write(encoded)
    print("File encrypted as", file_name + '.enc')
elif choice == 'd':
    with open(file_name, 'rb') as file:
        decoded = base64.b64decode(file.read())
    with open("decrypted_" + file_name, 'wb') as file:
        file.write(decoded)
    print("File decrypted as", "decrypted_" + file_name)
