 #intialize sum of variable
total=0
while True:
    number = int(input("enter a number:"))
    if number < 0:
        break
    total += number
print("the total sum is:",total)
enter a number:5
enter a number:10
enter a number:7
enter a number:-2
the total sum is: 22
