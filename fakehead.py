import random
subject = [
    "Swostima Khadka",
    "Nishant Basnet",
    "Sagar Lamsal",
    "Barsha Raut",
    "Alisha Chaudhary",
    "Anna Thapa"
]
actions=[
    "Opens Fridge",
    "Studies for Five Minutes",
    "Loses Phone While Talking on the Phone",
    "Wins Family Argument by Being Everyone Favorite Food",
    "Discovers Homework",
    "Cat Sits on Laptop,"
]
places=[
    "London",
    "Austrialia",
    "korea",
    "Africa",
    "Japan",
    "France"
]
while True:
    subjects=random.choice(subject)
    action=random.choice(actions)
    place=random.choice(places)

    headline=f" Funny news headlines , laugh and enjoy:{subjects} {action} {place} "
    print("\n" + headline)
    users_input=input("\nDo you want another fake and funny headlines?(yes/no)").strip()
    if users_input == "no":
        break
print("\nThank you for using  Funny news headlines , laugh and enjoy. Have a good day.")
users_input=input("\nHow was your experience?(good/bad)").strip()