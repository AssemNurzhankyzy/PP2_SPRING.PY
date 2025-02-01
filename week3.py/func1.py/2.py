def convertor(Fr):
    C = (5 / 9) * (Fr - 32)
    return C

Fr = float(input("Fahrenheit:"))
print("Centigrade: ", convertor(Fr))