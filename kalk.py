from  learn import add,div
try:
    print(div(12,2))
    print(add(12,4))
except ZeroDivisionError:
    print("მოხდა ნულზე გაყოფა")