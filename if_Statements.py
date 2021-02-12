# if statements
# conditionals

temperature = int(input("Whats the weather today: "))

if temperature > 80 :
    print("It's a hot day")
    print("drink plenty of water")
elif temperature > 50 and temperature < 80:
    print("It feels great out side!")
elif temperature > 30 and temperature < 50:
    print("its geting cold as fuck!")
elif temperature < 30:
    print("Its fucking cold!")
print("Done")


# exercise: receive users weight and convert it to either pounds or kilograms
weight = float(input("Enter your weight: "))
metric = input("Enter k for kilograms. Or l for pounds: ")


if metric.lower() == "k":
    conversion = weight / 0.45
    print("Weight in pounds " + str(conversion))
elif metric.lower() == "l":
    conversion = weight * 0.45
    print("Weight in kilograms " + str(conversion))
