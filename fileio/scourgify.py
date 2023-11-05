import csv
import sys
import os

def main():
    check_argument()
    new_csv()

def check_argument():
    sys.argv
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif os.path.isfile(sys.argv[1]) == False:
        sys.exit("Could not read invalid_file.csv")


def new_csv():
    output = []
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            split_name = line["name"].split(", ")
            output.append({"first":split_name[1], "last":split_name[0], "house": line["house"]})

    with open(sys.argv[2], "w") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for line in output:
            writer.writerow({"first": line["first"], "last": line["last"], "house": line["house"]})

if __name__ == "__main__":
    main()