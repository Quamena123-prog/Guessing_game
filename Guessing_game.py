name = input("Enter name: ")
print(f'''Hey there {name} and welcome to my guessing game.
      I am so happy you are here.
      You have 3 chances
      Ready to guess the number?''')
option = input("(Y)es or (N)o: ")
if option.upper() == "Y":
    print("Okay! Let's start")
else:
    print("Oops! We would love for you to play sometime.")

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count< guess_limit:
    guess =int(input("Guess: "))
    guess_count +=1
    if guess == secret_number:
        print("Yayy! You won!")
        break
else:
        print("Sorry! You failed!")
