# <img src="pliki/python_logo.png" alt="Balancer" height="128px">

## Program został przetestowany na:

| System operacyjny              | Wspierane |
| ------------------------------ | --------- |
| Ubuntu 22.04.3 LTS             | ✅        |
| Debian - Parrot OS 5.0         | ✅        |

*Program został przetestowany i zweryfikowany na systemach operacyjnych wymienionych powyżej. Nie gwarantujemy pełnej kompatybilności działania na innych dystrybucjach Linuxa, które nie zostały wyraźnie wskazane jako wspierane.*

# AIO SOC 
Struktura programu obejmuje kilka elementów:

**Główny katalog**: zawiera program.sh i README.md.\
**Katalog pliki**: Zawiera skrypt INSTALL i menu.py.\
Dodatkowo, w podkatalogu Programs znajdują się różne skrypty Pythona, takie jak:\
***Bandwith_Monitor.py, generowanie_hasel.py, Odszyfrowywanie_hasel.py, skaner.py, Sniffer.py, sprawdzanie_hasla.py***.

*Aby uruchomić program musimy nadać uprawnienia wykonywania "chmod +x" na program.sh*

### Główny program - $\color{orange}{\textsf{menu.py}}$ : Jest to główny skrypt, który służy jako punkt wejścia do aplikacji

### Klasy:
***Bandwith_Monitor.py***: Moduł do monitorowania przepustowości sieci.\
***generowanie_hasel.py***: Moduł do generowania haseł.\
***Odszyfrowywanie_hasel.py***: Moduł do odszyfrowywania haseł.\
***skaner.py***: Moduł do skanowania sieci.\
***Sniffer.py***: Moduł sniffera sieciowego.\
***sprawdzanie_hasla.py***: Moduł do sprawdzania siły hasła.

## Meny.py
**Ten program to kompleksowe narzędzie typu Wszystko-w-Jednym Centrum Operacji Bezpieczeństwa (AIO SOC), opracowane przez Jakuba i Kacpra, które oferuje szereg narzędzi do zarządzania bezpieczeństwem i siecią. Zostało zbudowane przy użyciu Pythona i wykorzystuje kilka zewnętrznych bibliotek.**

```python
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
```
Program zawiera kilka funkcji:\
***ASCII_art:*** Funkcja ta generuje kolorowe banery ASCII z nazwą "AIO SOC", które są wyświetlane w konsoli. Banery te zmieniają kolory i są czyszczone z ekranu co pewien czas, co dodaje dynamicznego efektu wizualnego.\
***run_script_in_new_terminal:*** Ta funkcja uruchamia określony skrypt Pythona w nowym terminalu, co pozwala na równoległe wykonywanie różnych zadań bez przerywania pracy głównego interfejsu programu.\
***print_header:*** Funkcja ta czyści konsolę i wyświetla nagłówek programu wraz z nazwą "AIO SOC" oraz informacjami o twórcach. Jest to przygotowanie do prezentacji menu głównego programu.\
***main_menu:*** Prezentuje główne menu programu, pozwalając użytkownikowi na wybór między zarządzaniem hasłami, bezpieczeństwem sieci lub wyjściem z programu. Każda z opcji prowadzi do dalszych podmenu związanych z daną kategorią.\
***passwords_menu i network_security_menu:*** Te sekcje oferują specjalistyczne narzędzia - pierwsza pozwala na generowanie, dekodowanie i weryfikację haseł, druga zaś umożliwia skanowanie sieci, analizę ruchu oraz testowanie przepustowości. 


## Generowanie haseł

Kod stanowi narzędzie do generowania bezpiecznych haseł, które użytkownik może dostosować poprzez wybór długości. Oferuje również opcję dodatkowego zabezpieczenia poprzez zastosowanie szyfru Cezara, umożliwiając użytkownikowi wybór między prostym hasłem a hasłem zaszyfrowanym dla dodatkowej warstwy ochrony.

*Szyfr Cezara jest prostym, ale niezwykle starym sposobem na zabezpieczenie informacji, polegającym na przesuwaniu liter alfabetu o ustaloną liczbę miejsc. Jest to jednak metoda szyfrowania o niskiej bezpieczeństwie, ponieważ łatwo ją złamać poprzez analizę częstotliwości występowania liter lub próbę siłową.*

### Importowanie bibliotek
```python
import string
import random
```
**Biblioteka string**: Jest wykorzystywana do uzyskania zestawu znaków, które mogą być użyte do tworzenia haseł. Przy użyciu string.ascii_letters (które łączy małe i wielkie litery alfabetu) oraz string.digits (które zawiera cyfry od 0 do 9), kod tworzy pulę znaków, z której będą losowo wybierane poszczególne znaki hasła.

**Biblioteka random**: Umożliwia losowy wybór znaków z puli utworzonej za pomocą biblioteki string do generowania haseł. Funkcja random.choice() jest używana do wybierania pojedynczego znaku z połączonego ciągu liter i cyfr za każdym razem, gdy jest wywoływana w pętli for, która powtarza się tyle razy, ile znaków ma mieć hasło (określone przez użytkownika).

### generate password
```python
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
```
Wewnątrz metody **run()** zdefiniowana jest funkcja pomocnicza **generate_password()**, która służy do generowania losowego hasła. 

Funkcja **generate_password()** rozpoczyna się od nieskończonej pętli while, która prosi użytkownika o podanie długości hasła. 

**try-except**, kod próbuje przekonwertować wprowadzoną wartość na liczbę całkowitą **(int)**. Jeśli użytkownik wprowadzi coś, co nie jest liczbą, zostanie wyświetlony komunikat o błędzie ("Proszę podać liczbę.") i zostanie ponownie poproszony o wprowadzenie wartości. Jeżeli wprowadzona wartość jest liczbą, ale jest mniejsza niż 8, wyświetlany jest komunikat, że minimalna długość hasła to 8 znaków, i użytkownik jest ponownie proszony o wprowadzenie wartości.

Po wprowadzeniu poprawnej długości hasła, funkcja przechodzi do tworzenia samego hasła. Do tego celu używane są znaki z string.ascii_letters (łączące małe i wielkie litery alfabetu angielskiego) oraz string.digits (cyfry od 0 do 9). Funkcja random.choice(characters) losowo wybiera znak z połączonego ciągu tych znaków, a join() łączy te losowo wybrane znaki w jedno hasło o długości określonej przez użytkownika.

### Cezar
```python
def cezar(password, shift):
    result = ""
    for char in password:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - start) % 26 + start)
        else:
            result += char
    return result        
```

Funkcja **cezar()** implementuje prosty szyfr przesuwający, znany również jako szyfr Cezara, który jest jedną z najstarszych znanych technik szyfrowania.

Funkcja przyjmuje dwa argumenty: **password**, który jest hasłem (ciągiem znaków) do zaszyfrowania, oraz **shift**, który określa liczbę pozycji, o które każda litera w haśle zostanie przesunięta w alfabecie.

Funkcja używa pętli for do iteracji przez każdy znak w haśle. Dla każdego znaku sprawdza, czy jest literą **(char.isalpha())**.

Szyfrowanie liter: Jeżeli znak jest literą, funkcja określa punkt startowy alfabetu (start), który wynosi 65 dla wielkich liter (wg kodu ASCII litera 'A' ma wartość 65) i 97 dla małych liter (wg kodu ASCII litera 'a' ma wartość 97). Następnie, używając funkcji ord(), konwertuje znak na jego wartość ASCII, dodaje przesunięcie (shift), odejmuje wartość startową, aby przeskalować wynik do zakresu 0-25 (odpowiadającego liczbie liter w alfabecie angielskim), a następnie oblicza resztę z dzielenia przez 26 (liczbę liter w alfabecie), aby zapewnić "zawijanie" w przypadku przekroczenia zakresu liter. Wynikowa wartość jest następnie przeskalowana z powrotem do zakresu kodów ASCII i konwertowana na znak za pomocą funkcji chr(). Jeśli znak nie jest literą, jest on dodawany do wynikowego ciągu (result) bez zmian.

Po przetworzeniu wszystkich znaków w haśle, funkcja zwraca wynikowy ciąg, który jest zaszyfrowaną wersją oryginalnego hasła.

### Main
```python
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
```
Funkcja main() pełni rolę punktu wejścia do procesu generowania i opcjonalnego szyfrowania hasła.
Użytkownik jest następnie proszony o wybór algorytmu szyfrowania. Może wybrać zastosowanie szyfru Cezara (opcja 1) lub pozostawienie hasła bez zmian (opcja 2).

Jeśli użytkownik wybierze szyfr Cezara, funkcja prosi o podanie przesunięcia, które ma być użyte do szyfrowania. Hasło jest następnie przekazywane do funkcji **cezar()**

Na koniec, w zależności od dokonanego wyboru, wyświetlane jest albo zaszyfrowane hasło (jeśli wybrano szyfr Cezara), albo oryginalne hasło (jeśli nie wybrano szyfrowania).

## Odszyfrowywanie haseł

Służy do deszyfrowania haseł zakodowanych za pomocą szyfru Cezara. Użytkownik jest proszony o podanie hasła oraz wartości przesunięcia, a następnie program odwraca szyfrowanie i wyświetla oryginalne hasło.
```python
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
```

Przechodzi przez każdy znak w podanym haśle **(password)** i sprawdza, czy dany znak jest dużą literą **(char.isupper())** lub małą literą **(char.islower())**.

Dla liter oblicza ich pozycję w alfabecie, a następnie przesuwa je wstecz o określoną wartość **(shift)**. Jeżeli znaki nie są literami, dodaje je do rozwiązania. 

Na samym końcu otrzymujemy rozszyfrowane hasło.

```python
print("Podaj hasło do odszyfrowania:")
password = input("Hasło: ")

print("Algorytmem szyfrująącem jest: 'Szyfr Cezara'")

shift = int(input("Podaj przesunięcie dla szyfru Cezara: "))
decrypted_password = caesar_decipher(password, shift)
        
if decrypted_password is not None:
    print("Odszyfrowane hasło:", decrypted_password)

input("Naciśnij Enter, aby kontynuować")
```

Program prosi użytkownika o wprowadzenie hasła, które ma zostać odszyfrowane, dane które wpisał użytkownik do programu są przechowywane w zmiennej **'password'**

Użytkownik jest proszony o podanie wartości przesunięcia użytej w szyfrze Cezara. Ta wartość jest przechwytywana, konwertowana na liczbę całkowitą i przechowywana w zmiennej **'shift'**

Jeśli odszyfrowane hasło zostanie pomyślnie utworzone (czyli **decrypted_password** nie jest **None**), program wyświetla odszyfrowane hasło.

## Sprawdzanie hasła według kryteriów

Program prosi użytkownika o wprowadzenie hasła, a następnie ocenia jego siłę na podstawie kryteriów takich jak długość, obecność wielkich i małych liter, cyfr oraz znaków specjalnych. Na koniec wypisuje ocenę hasła. 

*Kryteria są ustalone przez nas, można modyfikować według uznania.*

```python
class passwd:
    def run(self):
        def password():
            password = input("Proszę wprowadzić hasło: ")
    
        # Zdefiniowanie zmiennych
    
            dlugosc = len(password) >= 8   
            duze = any(char.isupper() for char in password) 
            male = any(char.islower() for char in password) 
            liczby = any(char.isdigit() for char in password) 
            znaki_specjalne = any(not char.isalnum() for char in password)

```
password = input("Proszę wprowadzić hasło: ") - prosi użytkownika o wprowadzenie hasła i przypisuje wprowadzoną wartość do zmiennej **password**.

Następnie definiujemy pięć zmiennych, które oceniają różne aspekty bezpieczeństwa wprowadzonego hasła:

**dlugosc** - sprawdza, czy długość hasła jest większa lub równa 8 znakom. Jeśli tak, zmienna przyjmuje wartość **True**; w przeciwnym razie False.

**duze** - ocenia, czy hasło zawiera co najmniej jedną wielką literę.

**male** - działa podobnie do duze, ale sprawdza obecność co najmniej jednej małej litery w haśle.

**liczby** - sprawdza, czy w haśle znajduje się co najmniej jedna cyfra

**znaki_specjalne** - ocenia, czy hasło zawiera co najmniej jeden znak specjalny

```python

# Sprawdzanie warunków
    
if dlugosc and duze and male and liczby and znaki_specjalne:
    return "Świetne"
elif dlugosc and (duze or male) and liczby:
    return "Bezpieczne"
elif dlugosc and (duze or male):
    return "Poprawne"
elif dlugosc:
    return "Słabe"
else:
    return "Niebezpieczne"
    
# Wypisuje wynik 
result = password()
print(result)
    
input("Naciśnij Enter, aby kontynuować")

```

Tutaj natomiast oceniana jest siła hasła przy użyciu serii instrukcji warunkowych if, elif, else, opierając się na wcześniej zdefiniowanych zmiennych dlugosc, duze, male, liczby, znaki_specjalne.

- Jeśli hasło spełnia wszystkie kryteria (jest dostatecznie długie, zawiera wielkie i małe litery, cyfry oraz znaki specjalne), funkcja zwraca ocene hasła jako: "Świetne".
- Jeśli hasło jest dostatecznie długie, zawiera co najmniej jedną wielką lub małą literę oraz co najmniej jedną cyfrę, ale nie wymaga obecności znaków specjalnych, funkcja zwraca ocene hasła jako: "Bezpieczne".
- Jeśli hasło jest dostatecznie długie i zawiera co najmniej jedną wielką lub małą literę (bez wymogu cyfr lub znaków specjalnych), funkcja zwraca ocenę hasła jako: "Poprawne".
- Jeśli hasło jest tylko dostatecznie długie, bez dodatkowych wymagań, funkcja zwraca ocenę hasła jako: "Słabe".

  W każdym innym przypadku (gdy żadne z powyższych kryteriów nie jest spełnione), funkcja zwraca ocenę hasła jako: "Niebezpieczne".

## Sprawdzanie prędkości internetu

Program mierzy prędkość pobierania i wysyłania internetu użytkownika za pomocą biblioteki speedtest. Po obliczeniu prędkości w megabitach na sekundę, wyświetla wynik.

```python
import speedtest

class bandwith:
    def run(self):
        speed = speedtest.Speedtest()

        download = round((speed.download()/1048576),2)
        upload = round((speed.upload()/1048576),2)
        print(f"Twoją prędkość pobierania wynosi: {download} Mb/s")
        print(f"Twoją prędkość wysyłania wynosi: {upload} Mb/s")
```

## Skaner 

**Skaner sieci** jest narzędziem do identyfikowania aktywnych urządzeń w określonym zakresie adresów IP poprzez wysyłanie do nich sygnałów ping. Narzędzie wykorzystuje biblioteki ipaddress, threading oraz subprocess do przeprowadzenia wielowątkowego skanowania, co pozwala na szybsze przeszukiwanie zakresów adresów.

```python
import ipaddress
import threading
import subprocess

class scanner:
    def run(self):
        def ping_host(ip, available_hosts, timeout=2):
            try:
                result = subprocess.check_output(['ping', '-c', '1', '-W', str(timeout), ip], stderr=subprocess.STDOUT, universal_newlines=True)
                if "1 packets transmitted, 1 received" in result and "0% packet loss" in result:
                    available_hosts.append(ip)
            except subprocess.CalledProcessError:
                pass
            
        def scan_ip_range(ip_range):
            try:
                network = ipaddress.IPv4Network(ip_range, strict=False)
            except ValueError:
                print("Niepoprawny zakres adresów IP.")
                return
    
            available_hosts = []
            threads = []
            for ip in network.hosts():
                ip = str(ip)
                thread = threading.Thread(target=ping_host, args=(ip, available_hosts))
                threads.append(thread)
                thread.start()
    
            for thread in threads:
                thread.join()
    
            if available_hosts:
                print("Dostępne hosty:")
                for host in available_hosts:
                    print(host)
            else:
                print("Brak dostępnych hostów w podanym zakresie.")
    

        ip_range = input("Podaj zakres adresów IP (np. 192.168.1.1/24): ")
        scan_ip_range(ip_range)
    
        input("Naciśnij Enter, aby kontynuować")
```

**Metoda ***run***** jest główną funkcją klasy scanner, która koordynuje działanie skanera. Rozpoczyna się od pobrania od użytkownika zakresu adresów IP do przeskanowania, a następnie inicjuje proces skanowania tego zakresu.\
**Funkcja ***scan_ip_range***** jest odpowiedzialna za przeprowadzenie skanowania wskazanego zakresu adresów IP. Zakres ten jest określany przez parametr ip_range.\
**Funkcja ***ping_host***** jest odpowiedzialna za pingowanie pojedynczego adresu IP i dodawanie go do listy dostępnych hostów, jeśli odpowiedź jest pozytywna.

## Sniffer

Prosty sniffer pakietów sieciowych napisany w Pythonie z wykorzystaniem biblioteki PyShark. Program przechwytuje pakiety sieciowe w czasie rzeczywistym na wybranym interfejsie sieciowym przez określony czas.

```python
import pyshark

class sniffer:
    def run(self):
        number_of_packets = int(input("Podaj czas w którym program ma przechwytywać pakiety (s): "))
        eth_interface = input("Podaj interface sieciowy na którym chcesz nasłuchiwać: ")
    
        # Przechwytywanie pakietów na żywo
        capture = pyshark.LiveCapture(interface=eth_interface)
        capture.sniff(timeout=number_of_packets)
        packets = [pkt for pkt in capture._packets]
        capture.close()
        for packet in packets:
            print("Nowy", packet)

        input("Naciśnij Enter, aby kontynuować")
```
***Przebieg działania programu wygląda następująco:***\
    1. Użytkownik jest proszony o podanie czasu (w sekundach), przez który program ma przechwytywać pakiety.\
    2. Następnie program prosi użytkownika o podanie nazwy interfejsu sieciowego, na którym ma zostać przeprowadzone przechwytywanie.\
    3. Po otrzymaniu obu danych wejściowych, program inicjuje przechwytywanie pakietów na żywo za pomocą klasy **pyshark.LiveCapture**,\ podając jako argument nazwę interfejsu sieciowego.\ **Metoda sniff()** jest następnie wywoływana z określonym wcześniej czasem jako limit, co uruchamia proces przechwytywania pakietów przez określony czas.\
    4. Po zakończeniu przechwytywania, program przechodzi przez wszystkie zebrane pakiety i wyświetla informacje o każdym z nich na konsoli.\ W ten sposób użytkownik może zobaczyć szczegóły przechwyconych pakietów.


