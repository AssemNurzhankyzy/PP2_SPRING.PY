def revers(str):
    str = list (str.split())
    str.reverse()

    for i in str:
        print (i, end= " ")

sentence = str (input (" Enter a sentence:"))
revers (sentence)