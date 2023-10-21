def main():
    say = input("Input: ")
    print("Output:", shorten(say))



def shorten(palavra):
    palavra = list(str(palavra).strip())
    lenght = len(palavra) + 1
    for c in range(0, lenght):
        for k in palavra:
            if k in 'AaEeIiOoUu':
                palavra.remove(k)
    if palavra == []:
        return " "
    else:
        return str(''.join(palavra))

if __name__ == "__main__":
    main()
