class decryp_passwd:
    def run(self):
        def caesar_decipher(password, shift):
            # Funkcja odwracająca szyfr Cezara
            deciphered = ""
            for char in password:
                if char.isupper():
                    deciphered += chr((ord(char) - shift - 65) % 26 + 65)
                elif char.islower():
                    deciphered += chr((ord(char) - shift - 97) % 26 + 97)
                else:
                    deciphered += char
            return deciphered

        print("Podaj hasło do odszyfrowania:")
        password = input("Hasło: ")

        print("Algorytmem szyfrująącem jest: 'Szyfr Cezara'")

        shift = int(input("Podaj przesunięcie dla szyfru Cezara: "))
        decrypted_password = caesar_decipher(password, shift)
        
        if decrypted_password is not None:
            print("Odszyfrowane hasło:", decrypted_password)

        input("Naciśnij Enter, aby kontynuować")