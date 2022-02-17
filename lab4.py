"""
Michael Balestriere
Week 4 - Make a dictionary
"""

my_dict = {}
my_dict["sport"] = "My favorite sport is soccer "
my_dict["song"] = "My favorite song is Thriller by Michael Jackson"
my_dict["game"] = "My favorite video game is League of Lengends"

while True:
    user_input = input(
        "Type in 'sport' , 'song' , or 'game' to learn one of my favorites, or type in a term to get the defenition, or type in 'new' to add a new word to the dictionary - "
    )
    if user_input == "sport":
        print(my_dict["sport"])
    if user_input == "song":
        print(my_dict["song"])
    if user_input == "game":
        print(my_dict["game"])
    if user_input == "new":
        new_term = input("Enter the new term you want to add - ")
        new_def = input("Enter the new defenition for your new term - ")
        my_dict[new_term] = new_def
    if user_input != "sport":
        if user_input != "song":
            if user_input != "game":
                if user_input != "new":
                    print(my_dict[user_input])
