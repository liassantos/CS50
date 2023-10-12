def main():
    groceryList = []

    while True:
        try:
            item = str(input("Item: ")).upper().strip()
            if item.isnumeric():
                continue
        except EOFError:
            break
        else:
            groceryList.append(item)

    unique = set(groceryList)
    print("="*50)
    print("GROCERY LIST")
    for k, c in enumerate(sorted(unique)):
        print(groceryList.count(c), c)
    print("="*50)


main()
