def main():
    integer = get_int('Digite um número inteiro: ')
    real = get_real('Digite um número real: ')
    print(f'O valor inteiro digitado foi {integer} e o valor real digitado foi {real}')


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except (TypeError, ValueError):
            print('\033[31mERRO: Digite um número inteiro válido.\033[0;0m')
        else:
            break


def get_real(prompt):
    while True:
        try:
            return float(input(prompt))
        except (TypeError, ValueError):
            print('\033[31mERRO: Digite um número real válido.\033[0;0m')
        else:
            break

main()
