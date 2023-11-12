import re

def main():
    print(validate(input("IPV4 Address: ").strip()))


def validate(ip):
    regex = "([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])"
    if valid := re.search(f"^{regex}\.{regex}\.{regex}\.{regex}$", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()