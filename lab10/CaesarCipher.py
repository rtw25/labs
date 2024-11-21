
# function to encrypt text
def encrypt(plaintext, key):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            shifted = chr(((ord(char.lower()) - ord('a') + key) % 26) + ord('a'))
            ciphertext += shifted
        elif char.isspace():
            ciphertext += char
        else:
            shifted = ord(char) + key
            if shifted > 126:
                shifted = 32 + (shifted - 127)
            elif shifted < 32:
                shifted = 126 - (31 - shifted)
            ciphertext += chr(shifted)
    return ciphertext

# function to decrypt text
def decrypt(ciphertext, key):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            shifted = chr(((ord(char.lower()) - ord('a') - key) % 26) + ord('a'))
            plaintext += shifted
        elif char.isspace():
            plaintext += char
        else:
            shifted = ord(char) - key
            if shifted > 126:
                shifted = 32 + (shifted - 127)
            elif shifted < 32:
                shifted = 126 - (31 - shifted)
            plaintext += chr(shifted)
    return plaintext

# example usage
if __name__ == "__main__":
    # test the functions
    key = 3
    encrypted_text = encrypt("hello WORLD!", key)
    decrypted_text = decrypt(encrypted_text, key)


    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")

    key = 6
    encrypted_text = encrypt("zzz", key)
    decrypted_text = decrypt(encrypted_text, key)

    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")

    key = -6
    encrypted_text = encrypt("FFF", key)
    decrypted_text = decrypt(encrypted_text, key)

    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")
