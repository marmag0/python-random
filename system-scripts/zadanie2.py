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
    """Wywoływany gdy dane wejściowe są w nieprawidłowym formacie"""
    pass

class WrongNumberOfArgs(Exception):
    """Wywoływany gdy wprowadzono niewłaściwą liczbę danych wejściowych"""
    pass

def main():
    
    # instrukcja dla użytkownika i wskazanie wymaganego formatu
    print("\nEnter students' names and their scores (min. 5 pairs) in the format:")
    print("name1 score1")
    print("For example: Alice 85 Bob 90")
    print("Insert each pair in a separate line. To stop inserting, enter 'end'\n")

    # przyjmowanie i sprawdzenie poprawności danych wejściowych
    pattern = r"[a-zA-ZĄĆĘŁŃÓŚŻŹąćęłńóśżź]+\s([0-9]|[1-9][0-9]|100)"
    students = []

    while True:
        try:
            args = input()
            if args == "end":
                if len(students) < 5:
                    raise WrongArgs
                else:
                    break
            elif re.match(pattern, args):
                args = args.split()
                students.append({
                    "name": args[0],
                    "score": int(args[1]),
                    "grade": "not-assigned"
                    })
                continue
            else:
                raise WrongArgs
        except WrongArgs:
            print("\nError! Wrong format of arguments!\n")
            sys.exit(1)
        except WrongNumberOfArgs:
            print("\nError! Wrong number of arguments!\n")
            sys.exit(1)
        except:
            print("\nError! Unexpected error occurred!\n")
            sys.exit(1)

    # zasadnicza część programu
    sum = 0     # suma wszystkich wyników z testu
    passed = len(students)  # ilość studentów, którzy zdali (≥50)
    podium = [("not-assigned", 0) for i in range(3)] # imion i wynik 3 studentów z najwyższym wynikiem

    for i in range(len(students)):
        sum += students[i]["score"]

        # przypisanie oceny
        if students[i]["score"] < 50:
            students[i]["grade"] = 2.0
            passed -= 1
        elif students[i]["score"] < 60:
            students[i]["grade"] = 3.0
        elif students[i]["score"] < 70:
            students[i]["grade"] = 3.5
        elif students[i]["score"] < 80:
            students[i]["grade"] = 4.0
        elif students[i]["score"] < 90:
            students[i]["grade"] = 4.5
        elif students[i]["score"] <= 100:
            students[i]["grade"] = 5.0
        
        # ranking top3 studentów
        if students[i]["score"] > podium[0][1]:
            podium.insert(0, (students[i]["name"], students[i]["score"]))
            podium.pop()
        elif students[i]["score"] > podium[1][1]:
            podium.insert(1, (students[i]["name"], students[i]["score"]))
            podium.pop()
        elif students[i]["score"] > podium[2][1]:
            podium.insert(2, (students[i]["name"], students[i]["score"]))
            podium.pop()
        
    avg = sum / len(students)   # średni wynik testu

    # wypisanie wyników
    print(f"\nTop 3 students: {podium[0][0]} -> {podium[0][1]}, {podium[1][0]} -> {podium[1][1]}, {podium[2][0]} -> {podium[2][1]}")
    print(f"average test score: {avg} | passed: {passed}\n")

    print("All student's and their grades:")
    for i in range(len(students)):
        if i < (len(students)-1):
            print(f"{students[i]['name']} -> {students[i]['grade']}", end="; ")
        else:
            print(f"{students[i]['name']} -> {students[i]['grade']}\n")
    
    return 0

if __name__ == "__main__":
    main()
else:
    print("\nError! This script cannot be imported!\n")

