import random

word_list = ["little", "book", "trouble", "apple"]
random_word = random.choice(word_list)
Lives = 6
display = []

game_over = False
print(random_word)

for letter in random_word:
    display += "_"

print(display)

while not game_over:
    guessed_letter = input ("guess a letter").lower()

    for position in range(len(random_word)):
        letter = random_word[position]

        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)