def convertor (grams):
    ounces = 0.03527396 * grams
    return ounces

grams =float(input("grams:"))
print("ounces=", convertor(grams))
