#!/bin/bash

# Instalacja
inst="pliki/INSTALL"

# Ścieżka do programu
pwd="pliki/menu.py"

# Sprawdzenie dystrybucji i informowanie użytkownika
if ! command -v apt-get &> /dev/null; then
    echo "Wykryto, że apt-get nie jest dostępny w Twoim systemie."
    echo "Upewnij się, że masz zainstalowany pipx przed kontynuacją."
    read -p "Czy chcesz kontynuować? (y/n) " choice
    if [[ $choice != "y" ]]; then
        echo "Przerwano instalację."
        exit 1
    fi
fi

# Uruchomienie instalacji z pliku
source "$inst" || { echo "Nie można wykonać pliku $inst"; exit 1; }

# Uruchomienie skryptu Python po instalacji
python3 "$pwd"