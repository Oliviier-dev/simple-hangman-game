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
