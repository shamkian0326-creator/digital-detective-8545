try:
    number = int(input("Decimal integer: "), 10)
except ValueError:
    raise SystemExit("Enter an integer in decimal digits.") from None

print("Binary:", bin(number))
print("Hexadecimal:", hex(number))
