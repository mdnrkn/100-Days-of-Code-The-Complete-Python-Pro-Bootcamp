print("Welcome to Rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride.")
    age = int(input("What is your age?\n"))
    
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    # age >= 45 and age <= 55
    elif 45 <= age <= 55:
        print("Everything is going to be okay.\nHave a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want to have a photo take? \nType 'Y' for Yes and 'N' for No.\n")
    # add $3 dollar 
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")