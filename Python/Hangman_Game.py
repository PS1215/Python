import random

word_list = {
    "fruit": [
        ("apple", "A round fruit with a stem and a core."),
        ("pear", "A fruit with a rounded base and a narrow top."),
        ("pineapple", "A tropical fruit with a spiky exterior."),
        ("watermelon", "A large, juicy fruit with a green rind and red flesh.")
    ],
    "vehicle": [
        ("car", "A four-wheeled vehicle powered by an engine."),
        ("train", "A vehicle that runs on tracks and carries passengers or cargo."),
        ("bicycle", "A human-powered vehicle with two wheels."),
        ("airplane", "A vehicle that can fly through the air."),
        ("helicopter", "A vehicle with rotors that allow it to fly straight up and down.")
    ]
}

max_guesses = 6

hangman = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\  |
    / \  |
        ===
    """
]

def get_word():
    category = random.choice(list(word_list.keys()))
    word, hint = random.choice(word_list[category])
    if category == "fruit":
        hint += " (Its a fruit🤫🤫)"
    return word, hint

def play_game():
    print("------Welcome to Hangman------")
    word, hint = get_word()
    word_set = set(word)
    guessed_set = set()
    incorrect_guesses = 0
    
    while len(word_set - guessed_set) > 0 and incorrect_guesses < max_guesses:
        print(hangman[incorrect_guesses])
        current_word = ""
        
        for letter in word:
            if letter in guessed_set:
                current_word += letter
            else:
                current_word += "_"
                
        print("Current word: ", current_word)
        print("Hint: ", hint)
        print("Incorrect guesses left: ", max_guesses - incorrect_guesses)
        
        guess = input("Enter a letter or the full word: ").lower()
        
        if guess == word:
            print("Congratulations you won😎😎")
            play_again()
            return
        elif guess in guessed_set:
            print("You already guessed that letter🙄🙄")
        elif guess in word_set:
            print("Correct😁😁")
            guessed_set.add(guess)
        else:
            print("Incorrect😅😅")
            incorrect_guesses += 1
            
    if incorrect_guesses == max_guesses:
        print(hangman[incorrect_guesses])
        print("Sorry you lost the word was:😯😯 ", word)
        
    play_again()

def play_again():
    again = input("Do you want to play again?🤞🤞(y for Yes/n for No)").lower()
    if again == 'y':
        play_game()
    else:
        print("Thanks for playing Goodbye🙋‍♂️🙋‍♂️")

play_game()
