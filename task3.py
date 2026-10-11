price = int(input("Введите сумму в рублях: "))
if(price <0):
    print("Отрицательное значение!")
else:
    hundreds = price//100
    price %= 100

    fifties = price//50 
    price %= 50

    tens = price//10
    price %= 10

    fives = price //5
    price %= 5

    twos = price//2
    price %= 2

    ones = price
    
    print(f"100 руб: {hundreds}")
    print(f"50 руб:  {fifties}")
    print(f"10 руб:  {tens}")
    print(f"5 руб:   {fives}")
    print(f"2 руб:   {twos}")
    print(f"1 руб:   {ones}")
    
    