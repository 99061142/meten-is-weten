number_1_choosing = True
number_2_choosing = True

while number_1_choosing:
    a = input("Kies het eerste getal: ")

    try:
        if int(a):
            number_1_choosing = False
    
    except:
        print("Kies een geldig getal (1, 2, 3, etc...")


while number_2_choosing:
    b = input("Kies het tweede getal: ")

    try:
        if int(b):
            number_2_choosing = False
    
    except:
        print("Kies een geldig getal (1, 2, 3, etc...")


if a > b:
    Min = b
    Max = a
    print("a is het grootste getal: " + Max)

elif a < b:
    Min = a
    Max = b
    print("a is het kleinste getal: " + Min)

else:  
    Min = a
    Max = a
    print("a en b zijn even groot")

print("Het minimum is: " + Min)
print("Het maximum is: " + Max)