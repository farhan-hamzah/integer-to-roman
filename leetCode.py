roman_numerals = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]
num = int(input("Masukkan angka (1-1000): "))
if 1 <= num <= 1000:
    result = ""
    for value, symbol in roman_numerals:
        while num >= value:
            result += symbol
            num -= value
    print("Angka Romawi:", result)
else:
    print("Harap masukkan angka antara 1 sampai 1000.")