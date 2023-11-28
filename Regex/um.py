import re


def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"\b[u|U][m|M]\b", s)
    count_um = len(um)
    return count_um


if __name__ == "__main__":
    main()
