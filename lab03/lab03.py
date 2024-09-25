class Caesar:
    def __init__(self, key=0):
        self.__key = key


    def get_key(self):
        return self.__key


    def set_key(self, key):
        self.__key = key

    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                shifted = chr(((ord(char.lower()) - ord('a') + self.__key) % 26) + ord('a'))
                ciphertext += shifted
            elif char.isspace():
                ciphertext += char
            else:
                shifted = ord(char) + self.__key
                if shifted > 126:
                    shifted = 32 + (shifted - 127)
                elif shifted < 32:
                    shifted = 126 - (31 - shifted)
                ciphertext += chr(shifted)
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                shifted = chr(((ord(char.lower()) - ord('a') - self.__key) % 26) + ord('a'))
                plaintext += shifted
            elif char.isspace():
                plaintext += char
            else:
                shifted = ord(char) - self.__key
                if shifted > 126:
                    shifted = 32 + (shifted - 127)
                elif shifted < 32:
                    shifted = 126 - (31 - shifted)
                plaintext += chr(shifted)
        return plaintext




cipher = Caesar()
cipher.set_key(3)
print(cipher.encrypt("hello WORLD!"))
print(cipher.decrypt("KHOOR zruog$"))

cipher.set_key(6)
print(cipher.encrypt("zzz"))
print(cipher.decrypt("FFF"))
cipher.set_key(-6)
print(cipher.encrypt("FFF"))
