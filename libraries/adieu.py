import inflect

p = inflect.engine()
names = []
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break
tupleNames = tuple(names)
adieu = p.join(tupleNames)
print(f"Adieu, adieu, to {adieu}")
