#!/usr/bin/env python3

"""
Zadanie 2

Program wczytuje imiona i wyniki studentów; zapisuje je w liście słowników; 
sprawdza poprawność danych; oblicza średni wynik; liczbę osób, które zdały; 
trzech najlepszych studentów oraz przypisuje każdemu ocenę według podanej skali.
"""

import re
import sys

class WrongArgs(Exception):
    """Wywoływany gdy dane wejściowe są niepoprawne"""
    pass

def main():
    
    # instrukcja dla uytkownika i wskazanie wymaganego formatu
    print("\nEnter students' names and their scores (in %) in the format:")
    print("name1 score1")
    print("For example: Alice 85 Bob 90")
    print("Insert each pair in a separate line. To stop inserting, enter 'end'.\n")

    # przyjmowanie i sprawdzenie poprawności danych wejściowych
    pattern = r"[a-zA-ZĄĆĘŁŃÓŚŻŹąćęłńóśżź]+\s([0-9]|[1-9][0-9]|100)"
    students = []

    while True:
        try:
            args = input()
            if args == "end":
                break
            elif re.match(pattern, args):
                args = args.split()
                students.append({args[0]: int(args[1])})
                continue
            else:
                raise WrongArgs
        except WrongArgs:
            print("\nError! Wrong format or number of arguments!\n")
            sys.exit(1)
        except:
            print("\nError! Unexpected error occurred!\n")
            sys.exit(1)

    # zasadnicza część programu
    


    



    
    
    
    return 0

if __name__ == "__main__":
    main()
else:
    print("\nError! This script cannot be imported!\n")

