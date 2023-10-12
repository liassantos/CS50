from fractions import Fraction

def main():
    while True:
        try:
            user_choice = Fraction(input('Fraction: '))
            decimal = float(user_choice)
            percentual = f'{decimal:.0%}'
            if decimal > 1:
                continue
        except (ValueError, ZeroDivisionError, NameError):
            pass
        else:
            if decimal <= 0.01:
                print('E')
            elif 0.99 <= decimal <= 1:
                print('F')
            else:
                print(percentual)
            break


main()