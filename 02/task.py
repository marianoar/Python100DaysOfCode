#Integer
# es valido separador de miles con _
print(123_000)
print(523_555.79)
#Float
print(3.14159)

#Boolean
print(True)
print(False)

print(type(123))
print(type(True))
print(type("123"))
print(type(123.123))

#print("Number of letters in your name: " + str(len(input("Enter your name"))))

print(bool("true"))
if bool("true"):
    print(True)
#exponente
print(3**3)

print(5/3)
print(5//3)

print(3 * 3 + 3 / 3 - 3)

print(3 * (3 + 3) / 3 / 2 - 3)

bmi = 84 / 1.65 ** 2

print(bmi)
print(int(bmi))
print(float(bmi))
print(round(bmi, 2))
print(round(bmi, 3))

print(f"la masa es { round(bmi) }")

# exercise 2
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
aux = bill + bill*tip/100/people
print(f"Each person should pay {round(aux,2)}")


