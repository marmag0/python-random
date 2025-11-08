#!/usr/bin/env python3

"""
Zadanie 1

Program ma na celu utworzenie kopii zapasowej plików o określonym rozszerzeniu, 
bez nadpisywania już istniejących plików backupowych.

Argumentami wejściowymi programu są kolejno:
- ścieżka do katalogu źródłowego
- ścieżka do katalogu docelowego
- rozszerzenie
"""

import sys
import shutil
import pathlib

class WrongArgs(Exception):
    """Wywoływany gdy dane wejściowe są niepoprawne"""
    pass

def main():

    # sprawdzanie argumentów wejściowych (liczba i względna poprawność)
    try:
        if len(sys.argv) == 4:
            if pathlib.Path(sys.argv[1]).exists() and sys.argv[3].startswith("."):
                print("\nData Input Correct! Processing...\n")
            else:
                raise WrongArgs
        else:
            raise WrongArgs
    except WrongArgs:
        print("\nError! Wrong format or number of arguments!\n")
        sys.exit(1)
    except:
        print("\nError! Unexpected error occurred!\n")
        sys.exit(1)

    src = pathlib.Path(sys.argv[1])   # pierwszy argument - folder źródłowy
    dst = pathlib.Path(sys.argv[2])   # drugi argument - folder docelowy
    ext = sys.argv[3].lower()         # trzeci argument - rozszerzenie

    stats = [0, 0]  # liczba plików: [skopiowanych, pominiętych]

    dst.mkdir(exist_ok=True)    # utowrzenie katalogu jeśli nie istnieje

    # zasadnicza część programu
    for file in src.glob(f"*{ext}"):
        newName = f"{file.stem}_bak{ext}"
        dstPath = dst / newName
        if not dstPath.exists():
            shutil.copy2(file, dstPath)
            stats[0] += 1
        else:
            stats[1] += 1

    # komunikat wyjścia i statystyki
    print("Backup completed!")
    print(f"copied: {stats[0]} | skipped: {stats[1]}")

    return 0

if __name__ == "__main__":
    main()
else:
    print("\nError! This script cannot be imported!\n")
