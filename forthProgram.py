# Conditional Statement

# a = int(input("Provide any number? "))
# name = "Amit Kinha"

# if a >= 10:
#     print(f"My name is {name}")
# elif a <= 20:
#     print(f"my input value is {a}")
# else:
#     print("we didn't print your name")

t = int(input("Please tell the temperature :- "))

if t < 0:
    print("Freezing cold")
elif t >= 0 and t < 10:
    print("Very Cold")
elif t >= 10 and t < 20:
    print("Cold")
elif t >= 20 and t < 30:
    print("Pleasant")
elif t >= 30 and t < 40:
    print("Hot")
else:
    print("very hot temperature")