import sys
import os
from PIL import Image
from PIL import ImageOps


def check_argument():
    sys.argv
    ext1 = sys.argv[1].find(".")
    ext2 = sys.argv[2].find(".")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".png" not in sys.argv[1] and ".jpeg" not in sys.argv[1] and ".jpg" not in sys.argv[1]:
        sys.exit("Invalid output")
    elif ".png" not in sys.argv[2] and ".jpeg" not in sys.argv[2] and ".jpg" not in sys.argv[2]:
         sys.exit("Invalid output")
    elif os.path.isfile(sys.argv[1]) == False:
        sys.exit("Input does not exist")
    elif  sys.argv[1][ext1:] != sys.argv[2][ext2:]:
        sys.exit("Input and output have different extensions")


def main():
    check_argument()
    #sobrepor shirt na imagem imput e gerar output
    #abrir imagem
    img = Image.open(sys.argv[1])
    #abrir shirt
    shirt = Image.open("shirt.png")
    #pegar o tamanho do shirt
    size = shirt.size
    #resize imagem
    new_img = ImageOps.fit(img, size)
    #sobrepor shirt a imagem
    new_img.paste(shirt, mask=shirt)
    #mostrar imagem nova
    new_img.save(sys.argv[2])


if __name__ == "__main__":
    main()
