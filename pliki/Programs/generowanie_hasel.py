import string
import random

class gen_passwd:
    def run(self):
        def generate_password():
            while True:
                try:
                    length = int(input("Podaj długość hasła: "))
                    if length < 8:
                        print("Minimalna długość hasła to 8.")
                    else:
                        break
                except ValueError:
                    print("Proszę podać liczbę.")
            characters = string.ascii_letters + string.digits
            return ''.join(random.choice(characters) for i in range(length))
        
        def cezar(password, shift):
            result = ""
            for char in password:
                if char.isalpha():
                    start = 65 if char.isupper() else 97
                    result += chr((ord(char) + shift - start) % 26 + start)
                else:
                    result += char
            return result
      
        def main():
            password = generate_password()
            print("Wygenerowane hasło:", password)
        
            print("Wybierz algorytm:\n1. Szyfr Cezara\n2. Brak")
            algorithm_choice = input("Wybór (1 lub 2): ")
        
            if algorithm_choice == '1':
                shift = int(input("Podaj przesunięcie dla szyfru Cezara: "))
                processed_password = cezar(password, shift)
            elif algorithm_choice == '2':
                processed_password = password
        
            if algorithm_choice in ['1']:
                print("Zaszyfrowane hasło:", processed_password)
            if algorithm_choice == '2':
                print("Hasło",password)
        
            input("Naciśnij Enter, aby kontynuować")
        
        main()
        
