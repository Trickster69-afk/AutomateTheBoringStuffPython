#user guesses a 5-letter word
#hints = O for a correct letter in the same place in the secret word
#        o for a correct letter in a different place in the secret word
#        x for letters that are not in the secret word
#        If the guessed word is the same as the secret word, the function should return OOOOO
import random
import sys

def main():
    text = input("Enter a sentence: ").strip().split()
    secret_word = random.choice(text)
    for i in range(6): #6 tries
        while True: #keep prompting the user for 5 letter word if length != 5
            guess_word = input("Guess: ")
            if len(guess_word) == 5:
                break
            else:
                continue

        hint = get_word_hint(secret_word, guess_word)
        print(hint)
        if hint == "OOOOO": #if correct guess exit after leaving a message
            print("You guessed the word correctly")
            sys.exit()
    print(f"The secret word was {secret_word}. Better luck next time.")

def get_word_hint(secret_word, guess_word): #returns a five-character string of hint
    c = ""
    secret_word = secret_word.upper()
    guess_word = guess_word.upper()
    for i in range(5):
        if guess_word[i] == secret_word[i]:
            c += "O"
        elif guess_word[i] in secret_word:
            c += "o"
        else:
            c += "x"
    return c
        
if __name__ == "__main__":
    main()