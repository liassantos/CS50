def main():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    totalPrice = 0


    while True:
        try:
            order = str(input('Item: ')).strip().title()
            price = menu[order]
            totalPrice = totalPrice + price
        except EOFError:
            print("Order finished.\n"
                  f"${totalPrice:.2f} bill.\n"
                  "Thank you for choosing Felipe's Taqueria!")
            break
        except KeyError:
            pass
        else:
            print(f"${totalPrice:.2f}")


main()
