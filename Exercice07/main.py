## Écrivez votre code ici !
def square(number):
    if isinstance(number, (int, float)):
        return number**2
    else:
        print("Le paramètre doit être un nombre !")
        return None


print(square(5))
print(square(5.5))
print(square("5"))
