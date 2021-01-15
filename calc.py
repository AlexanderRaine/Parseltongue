what = input("Выбор +- ")
a = float(input("Число А"))
b = float(input("Число Б"))
c = 0
if what == "+":
    c = a + b
elif what == "-":
    c = a - b
else:
    print("Zatrahal")
print(c)
