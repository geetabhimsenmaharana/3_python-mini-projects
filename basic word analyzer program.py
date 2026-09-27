print("***************** Welcome to Test 1 *****************")

userword = input("Please enter a word or a short phrase: ").strip().lower()

print("You have entered:", userword)

print("Doing some validation...")

if userword == "":
    print("Text is empty")

else:
    print("Text:", userword)
    print("First character:", userword[0])
    print("Last character:", userword[-1])

    reversed_word = userword[::-1]

    print("Reversed word:", reversed_word)

    # Check for palindrome
    if reversed_word == userword:
        print("Text is a palindrome")
    else:
        print("Text is NOT a palindrome")

    # Check for the letter "a"
    if "a" in userword:
        print("Text contains the letter 'a'")
    else:
        print("Text does not contain the letter 'a'")

    # Check the length
    if len(userword) >= 5:
        print("Great job! Your text has 5 or more characters.")
    else:
        print("Keep practicing!")

