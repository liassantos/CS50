def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greeting = list(str(greeting).strip().lower())
    lista = str("".join(greeting)).split()
    if lista[0] == "hello":
        return "$0"
    elif greeting[0] == "h":
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
