# AIO SOC 
Struktura programu zawarta obejmuje kilka elementów:

**Główny katalog**: zawiera program.sh i README.md.\
**Katalog pliki**: Zawiera skrypt INSTALL.ps1 i menu.py.\
Dodatkowo, w podkatalogu Programs znajdują się różne skrypty Pythona, takie jak:\
***Bandwith_Monitor.py, generowanie_hasel.py, Odszyfrowywanie_hasel.py, skaner.py, Sniffer.py, sprawdzanie_hasla.py***.

### Główny program - $\color{orange}{\textsf{menu.py}}$ : Jest to główny skrypt, który służy jako punkt wejścia do aplikacji

### Klasy:
***Bandwith_Monitor.py***: Moduł do monitorowania przepustowości sieci.\
***generowanie_hasel.py***: Moduł do generowania haseł.\
***Odszyfrowywanie_hasel.py***: Moduł do odszyfrowywania haseł.\
***skaner.py***: Moduł do skanowania sieci.\
***Sniffer.py***: Moduł sniffera sieciowego.\
***sprawdzanie_hasla.py***: Moduł do sprawdzania siły hasła.

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

Kryteria są ustalone przez nas, można modyfikować według uznania.

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


