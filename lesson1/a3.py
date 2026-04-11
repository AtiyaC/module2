# 1) Display a menu asking the user to select a ride:
#    - 1 for Bike
#    - 2 for Car
print("Select your ride")
print("1. Bike")
print("2. Car")

# 2) Take the user’s input and store it in `choice`.
choice = int(input("Enter your choice"))
# 3) If `choice` is 1 (Bike):
#    a) Show bike options (Scooty / Scooter)
#    b) Take the user’s input for bike type and store it in `choice2`
#    c) If `choice2` is 1, print "you have selected scooty"
#       Else, print "you have selected scooter"
if choice == 1:
    print("Select your bike")
    print("1. Scooty")
    print("2. Scooter")
    choice2 = int(input("Enter your bike choice"))
    if choice2 == 1:
        print("your have choosen scooty")
    else:
        print("you have choosen scooter")
elif choice == 2:
    print("Select your car")
    print("1. Sedan")
    print("2. XUV")
    choice3 = int(input("Enter your car choice"))
    if choice3 == 1:
        print("your have choosen sedan")
    else:
        print("you have choosen XUV")

else:
    print("Wrong choice")
        

# 4) Else if `choice` is 2 (Car):
#    a) Show car options (Sedan / XUV)
#    b) Take the user’s input for car type and store it in `choice3`
#    c) If `choice3` is 1, print "you have selected sedan"
#       Else, print "you have selected XUV"

# 5) Else (if `choice` is not 1 or 2):
#    Print "Wrong choice!"