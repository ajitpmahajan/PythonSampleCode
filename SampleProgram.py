def Square(x):
    return x * x
    
listOfNumbers = [1,2,3,4,5]
print(listOfNumbers[4])

names = "Ajit.Mahajan.Kopar..Khairane".split(".")
l=len(names)
MasterData = {}
MasterData["FirstName"] = names[0]
print("Test",MasterData["FirstName"])

for name in names:
    print(name)

x = 0
while x < 10:
    if ( x % 2 == 0):
        print(x),
    x += 1
    
print(True and False)
print(Square(5))
