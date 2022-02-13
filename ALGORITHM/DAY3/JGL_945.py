animation ={
    "Pokemon": "Pikachu",
    "Digimon": "Agumon",
    "Yugiho": "Black Magician"
}

word = input()

# if word in animation:
#     print(animation[word])
# else:
#     print("I don't know")

print(animation.get(word, "I don't know"))