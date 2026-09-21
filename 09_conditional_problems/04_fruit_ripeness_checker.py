fruit = "banana"

color = {
    "Green" : "Unripe",
    "Yellow": "Ripe",
    "Brown" : "Overripe"
}

for key , value in color.items():
    print(key,value)

fruit_color = str(input("Enter fruit color : ")).strip().capitalize()

if fruit_color in color :
    print(fruit, "is ", color[fruit_color])
else :
    print("unknown color")
