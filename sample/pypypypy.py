    first=int(number / 16)
    if first == 10:
        first="A"
    elif first == 11:
        first="B"
    elif first == 12:
        first="C"
    elif first == 13:
        first="D"
    elif first == 14:
        first="Ett"
    elif first == 15:
        first="F" 
    second=int(number % 16)
    if second == 10:
        second="A"
    elif second == 11:
        second="B"
    elif second == 12:
        second="C"
    elif second == 13:
        second="D"
    elif second == 14:
        second="E"
    elif second == 15:
        second="F"
    first=str(first)
    second=str(second)
    print(first+second)
else:
    print("Number is greater than expected")
