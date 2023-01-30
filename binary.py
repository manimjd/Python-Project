#دسیمال به باینری

number=0
bace=1
last=0
sums=0
number = int(input("Enter number: "))
while number:
    last = int(number%10)
    number = int(number/10)
    last *= bace
    sums += last
    bace = bace*2
print(sums)

#باینری به دسیمال

dec = int(input("enter a number: "))

print("\nThe decimal value of", dec, "is\n")
print(bin(dec), "in binary.\n")
print(oct(dec), "in octal.\n")
print(hex(dec), "in hexadecimal.\n")
