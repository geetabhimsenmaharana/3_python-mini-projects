# ============================================================
# 🔤 RANDOM CA / BA WORD GENERATOR
# ============================================================
# A beginner Python mini-project.
#
# The program:
# 1. Asks the user to enter "ca" or "ba"
# 2. Searches a master list for matching words
# 3. Randomly selects 5 words
# 4. Removes each selected word from the available list
# 5. Converts the selected list into a string
# 6. Displays the final result
#
# Concepts practiced:
# - input()
# - strip()
# - lower()
# - strings
# - lists
# - list slicing
# - for loops
# - if / elif / else
# - random.choice()
# - append()
# - remove()
# - len()
# - join()
# ============================================================

import random


# ------------------------------------------------------------
# MASTER WORD LIST
# ------------------------------------------------------------
# This list contains 10 words starting with "ca"
# and 10 words starting with "ba".

words = [
    "cat",
    "cab",
    "can",
    "car",
    "cake",
    "camera",
    "candle",
    "castle",
    "cactus",
    "candy",

    "bat",
    "bag",
    "ban",
    "bar",
    "ball",
    "basket",
    "banana",
    "basic",
    "badge",
    "bamboo"
]


# ------------------------------------------------------------
# WELCOME MESSAGE
# ------------------------------------------------------------

print("\n========================================")
print("      🔤 RANDOM WORD GENERATOR")
print("========================================")

print("\nEnter 'ca' or 'ba'.")
print("We will generate 5 random words for you!")


# ------------------------------------------------------------
# GET USER INPUT
# ------------------------------------------------------------

user_input = input("\nEnter your two letters: ").strip().lower()


# ------------------------------------------------------------
# GET THE FIRST TWO CHARACTERS
# ------------------------------------------------------------

prefix = user_input[0:2]


# ------------------------------------------------------------
# CHECK USER INPUT
# ------------------------------------------------------------

if prefix == "ca" or prefix == "ba":

    print(f"\n🔎 Searching for words starting with '{prefix}'...")


    # --------------------------------------------------------
    # FIND MATCHING WORDS
    # --------------------------------------------------------
    # Create a new list containing only words
    # that start with the user's prefix.

    matching_words = []

    for word in words:

        if word[0:2] == prefix:
            matching_words.append(word)


    print(f"✅ Found {len(matching_words)} matching words.")


    # --------------------------------------------------------
    # SELECT 5 RANDOM WORDS
    # --------------------------------------------------------
    # We remove each selected word from matching_words.
    # This prevents the same word from being selected twice.

    selected_words = []

    for i in range(5):

        random_word = random.choice(matching_words)

        selected_words.append(random_word)

        # Remove the selected word from the available list
        matching_words.remove(random_word)


    # --------------------------------------------------------
    # CONVERT LIST INTO A STRING
    # --------------------------------------------------------

    result = ", ".join(selected_words)


    # --------------------------------------------------------
    # DISPLAY RESULT
    # --------------------------------------------------------

    print("\n🎉 Your 5 random words are:")
    print(result)


else:

    # --------------------------------------------------------
    # INVALID INPUT
    # --------------------------------------------------------

    print("\n❌ Invalid input.")
    print("Please enter only 'ca' or 'ba'.")

print("\n========================================")
print("              GAME END")
print("========================================")