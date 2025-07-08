import random
friends = ["Amit", "Nishat", "Rashed", "Hasan", "Billu"]

# option 1
index = random.randint(0, 4)
print(f"{friends[index]} will pay the bill.")

# option 2
print(f"{random.choice(friends)} will pay the bill.")
