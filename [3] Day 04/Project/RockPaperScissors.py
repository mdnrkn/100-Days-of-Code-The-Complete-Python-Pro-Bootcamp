import random

options = ["Rock 🪨", "Paper 📄", "Scissors ✂️"]

user_choose = int(input(
    "What do you want to choose?\n"
    "0 - Rock 🪨\n"
    "1 - Paper 📄\n"
    "2 - Scissors ✂️\n"
    "Enter your choice (0/1/2): "
))

computer_choose = random.randint(0, 2)

print(f"You choose      : {options[user_choose]}")
print(f"Computer choose : {options[computer_choose]}")

if user_choose == computer_choose:
    print("Draw ☹️")
elif (user_choose == 0 and computer_choose == 2) or \
     (user_choose == 1 and computer_choose == 0) or \
     (user_choose == 2 and computer_choose == 1):
    print("You Win 🎉")
else:
    print("You Lose 🚩")