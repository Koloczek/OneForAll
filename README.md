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
