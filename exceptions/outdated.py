from datetime import datetime

while True:
    try:
        chooseDate = input("Date: ").strip()
        formatedDate1 = datetime.strptime(chooseDate, "%m/%d/%Y").date()
    except ValueError:
        try:
            formatedDate2 = datetime.strptime(chooseDate, "%B %d, %Y").date()
            print(formatedDate2)
            break
        except ValueError:
            pass
    else:
        print(formatedDate1)
        break
