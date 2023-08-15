number1 = float(input("Liczba pierwsza: "))
number2 = float(input("Liczba druga: "))
dzialanie = int(input("Wybierz działanie:\n1. Dodawanie\n2. Odejmowanie\n3. Mnożenie\n4. Dzielenie\n5. Moduł\n"))

if dzialanie == 1:
    print(number1 + number2)
elif dzialanie == 2:
    print(number1 - number2)
elif dzialanie == 3:
    print(number1 * number2)
elif dzialanie == 4:
    if number2 == 0:
        print("Nie dziel przez 0")
    else:
        print(number1 / number2)
elif dzialanie == 5:
    print(number1 % number2)
else:
    print("Nieprawidłowy wybór działania")
