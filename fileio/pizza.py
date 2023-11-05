import sys
import os
import csv

from tabulate import tabulate

def main():
    check_argument()
    tabular_format()
#check se o argumento é válido e é um arquivo .csv
def check_argument():
    sys.argv
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    elif os.path.isfile(sys.argv[1]) == False:
        sys.exit("File does not exist")


#converter csv file em tabualar. Format the table using the library’s grid format.
def tabular_format():
    with open(sys.argv[1], "r") as file:
        table = list(csv.reader(file))
        print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

if __name__ == "__main__":
    main()
