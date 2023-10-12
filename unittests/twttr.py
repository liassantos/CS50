def shorten():
    palavra = list(str(input("Digite uma palavra: ")).strip().lower())
    lenght = len(palavra) + 1
    for c in range(0, lenght):
        for k in palavra:
            if k in 'aeiou':
                palavra.remove(k)
    if palavra == []:
        print("empty")
    else:
        print(''.join(palavra))


shorten()
