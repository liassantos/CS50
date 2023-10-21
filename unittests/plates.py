def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    s = list(s)
    if isinstance(s[0:1], str) and 6 >= len(s) >= 2:
        print(s)
        return True
    else:
        print(s)
        return False

main()