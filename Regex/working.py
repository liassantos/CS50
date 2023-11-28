import re

def main():
    print(convert(input("Hours: ")))


def zeroes(n):
    if n < 10:
        return f'0{n}'
    else:
        return n


import re

def main():
    print(convert(input("Hours: ")))


def zeroes(n):
    if n < 10:
        return f'0{n}'
    else:
        return n


def convert(s):
    try:
        new = re.search(r"^([1-9][0-2]?)(:[0-5][0-9])? (AM|PM) to ([1-9][0-2]?)(:[0-5][0-9])? (AM|PM)$", s)
        horasPrimNum = int(new.group(1))
        minPrimNum = new.group(2)
        horasSegNum = int(new.group(4))
        minSegNum = new.group(5)

        if new.group(3) == "PM" and horasPrimNum != 12:
            horasPrimNum += 12
        elif new.group(3) == "AM" and horasPrimNum == 12:
            horasPrimNum = 0
        if new.group(6) == "PM" and horasSegNum != 12:
            horasSegNum += 12
        elif new.group(6) == "AM" and horasSegNum == 12:
            horasSegNum = 0
        if minPrimNum == None:
            minPrimNum = ':00'
        if minSegNum == None:
            minSegNum = ':00'

        return f'{zeroes(horasPrimNum)}{minPrimNum} to {zeroes(horasSegNum)}{minSegNum}'

    except AttributeError:
        raise ValueError

if __name__ == "__main__":
    main()

