import os
import subprocess
import time
import sys
import pyfiglet
from colorama import Fore, Style
from Programs.generowanie_hasel import gen_passwd
from Programs.Odszyfrowywanie_hasel import decryp_passwd
from Programs.sprawdzanie_hasla import passwd
from Programs.skaner import scanner
from Programs.Sniffer import sniffer
from Programs.Bandwith_Monitor import bandwith



def ASCII_art():
    Banners = "AIO SOC"
    Subscript = "                                              Powered by Python©"
    ASCII_art_1 = pyfiglet.figlet_format(Banners, font='colossal')
    for col in [
        Fore.RED, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.YELLOW
    ] * 10 + [Fore.WHITE]:
        print(col + ASCII_art_1 + Subscript)
        time.sleep(0.05)
        os.system("clear")
    print(Fore.WHITE + ASCII_art_1 + Subscript)

def run_script_in_new_terminal(script_name):

    subprocess.Popen(["gnome-terminal", "--", "python3", script_name])

ASCII_art()


def print_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    Banners = "AIO SOC"
    Subscript = "                                              Powered by Python©"
    ASCII_art_2 = pyfiglet.figlet_format(Banners, font='colossal')
    print(ASCII_art_2 + Subscript)
    print("")
    print("       AIO SOC - All-In-One Security Operations Center")
    print("            Twórcy: Jakub 72903 oraz Kacper 72899")
    print("\nWitaj w menu głównym!\n")

def run_script(script_name):
    if os.name == 'nt':  # dla Windows
        os.system(f'start cmd /c python {script_name}')
    else:  #Linux
        os.system(f'gnome-terminal -e "python {script_name}"')

def main_menu():
    while True:
        print_header()
        print("1. Zarządzanie Hasłami")
        print("2. Bezpieczeństwo Sieci")
        print("3. Wyjście\n")
        choice = input("Wybierz kategorię: ")
        if choice == '1':
            passwords_menu()
        elif choice == '2':
            network_security_menu()
        elif choice == '3':
            print("Dziękujemy za skorzystanie z programu AIO SOC")
            time.sleep(3)
            os.system("clear")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
    
#print("Program stworzony przez Jakub 72903 oraz Kacper 72899")

def passwords_menu():
    while True:
        print_header()
        print("Kategoria Hasła:\n")
        print("1. Odszyfrowywanie haseł")
        print("2. Generowanie haseł")
        print("3. Sprawdzanie hasła")
        print("4. Powrót do menu głównego\n")
        choice = input("Wybierz opcję: ")
        
        if choice == '1':
            decryp_instance  = decryp_passwd()
            decryp_instance.run()
        elif choice == '2':
            gen_instance = gen_passwd()
            gen_instance.run()
        elif choice == '3':
            passwd_instance = passwd()
            passwd_instance.run()
        elif choice == '4':
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def network_security_menu():
    while True:
        print_header()
        print("Bezpieczeństwo Sieci:\n")
        print("1. Skaner")
        print("2. Sniffer")
        print("3. Test szybkości łącza")
        print("4. Powrót do menu głównego\n")
        choice = input("Wybierz opcję: ")
        if choice == '1':
            scanner_instance = scanner()
            scanner_instance.run()
        elif choice == '2':
            sniffer_instance = sniffer()
            sniffer_instance.run()
        elif choice == '3':
            bandwith_instance = bandwith()
            bandwith_instance.run()
        elif choice == '4':
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main_menu()

