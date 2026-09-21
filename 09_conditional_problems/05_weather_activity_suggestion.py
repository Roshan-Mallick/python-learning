suggestion = {
    "sunny":"go for a walk",
    "rainy":"Read a book",
    "snowy":"build a snowman"
}

for key , value in suggestion.items() :
    print(key,value)

weather = str(input("Enter weather today : ")).strip().lower()

if weather in suggestion :
    print("weather is ", weather , suggestion[weather])
else :
    print("no suggestion")
