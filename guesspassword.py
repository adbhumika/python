import random

easy_words=["tiger","lion","deer","human being"]
medium_words=["curious","anxious","gasp"]
hard_words=["ephemeral","ubiquitous","serendipity"]
print("Welcome to the guessing password game.")
print("Choose easy, medium or hard level to experience more")
level= input("Enter any level:").lower()
if level=="easy":
    secret=random.choice(easy_words)
elif level =="medium":
    secret=random.choice(medium_words)
elif level =="hard":
    secret=random.choice(hard_words)
else:
    print("Invalid Value so defaulting to easy level.")
    secret=random.choice(easy_words)
attempts=0
print("\nGuess the secret password")
while True:
    guess=input("Enter any words as guess: ").lower()
    attempts +=1
    if guess==secret:
        print(f"Congratulations. Your guess it in {attempts}attempts.")
        break
    hint=""
    for i in range(len(secret)):
        if i < len (guess) and guess[i]==secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    print("Hint:",hint)
print("Game Over")
