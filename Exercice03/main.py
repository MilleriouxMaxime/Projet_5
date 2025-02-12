words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

voyels = ["a", "e", "i", "o", "u", "y"]

result = [(word, sum(1 for letter in word if letter in voyels)) for word in words]

print(result)
