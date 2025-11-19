#Soe Min Min Latt
#6611938
#541

roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

while True:
    roman = input()
    if not roman:
        break

    total = 0
    length = len(roman)

    for i in range(length):
        value = roman_values[roman[i]]

        if i + 1 < length and value < roman_values[roman[i + 1]]: #check if left letter is smaller than right letter(eg. IV = 5-1)
            total -= value
        else:
            total += value

    print(total)

