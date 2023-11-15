def main():
    print(convert(input("Type something: ")))


def convert(text):
    happy = text.replace(":)", "🙂")
    sad = happy.replace(":(", "🙁")
    return sad


if __name__ == "__main__":
    main()
