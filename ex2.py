age=int(input("Give me your age"))

if age<=5:
    print("Free Entry")

elif 5<=age and age <=11:
    print("The price is 5k ")

elif 12<=age<=59:
    print("The price is 8k")

elif 60<=age:
    print("The price is 4k")

else:
    print("Error.202")
