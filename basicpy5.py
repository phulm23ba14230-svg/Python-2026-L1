colors = ["blue","white","red","black","green"]
color = input("what is your favourite color?")
if color in colors:
    index = colors.index(color)
    print("your color is at index", index, "in my list")
else:
    print("sorry, i could not find your color")