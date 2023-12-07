import datetime as dt
import inflect
import sys
import re


def main():
    print(get_text(get_minutos()))



def get_minutos():
    try:
        entrada = input('Data de Nascimento: ')
        data_nascimento = dt.date.fromisoformat(entrada)
        data_hoje = dt.date.today()
        dias = data_hoje - data_nascimento
        if re.match(r'[1-2][0-9][0-9][0-9]-[0-1][1-9]-[0-3][0-9]', entrada):
            pass
        else:
            sys.exit('Data inválida 👎')
        return int(dias.total_seconds() // 60)
    except ValueError:
        sys.exit('Data inválida 👎')



def get_text(minutos):
    p = inflect.engine()
    return f"{p.number_to_words(minutos, andword='')} minutes"



if __name__=="__main__":
    main()
