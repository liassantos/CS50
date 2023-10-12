from random import randint

def main():
    perguntas = generate_integer(get_level())
    print(perguntas)
    for k, c in perguntas.items():
        user = int(input(k))
        if user != c:



def get_level():
    while True:
        level = int(input("Level: "))
        if (level != 1) and (level != 2) and (level != 3):
            pass
        else:
            break
    return level


def generate_integer(level):
    dictionary = {}
    for c in range(10):
        if level == 1:
            x = randint(0, 9)
            y = randint(0, 9)
        elif level == 2:
            x = randint(10, 99)
            y = randint(10, 99)
        elif level == 3:
            x = randint(100, 999)
            y = randint(100, 999)
        dictionary[f"{x} + {y} = "] = x + y
    return dictionary


main()
