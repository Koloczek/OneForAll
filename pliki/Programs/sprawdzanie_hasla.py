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
