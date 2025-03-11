def writesome(list_of_elements):
    with open("some.txt", '+a') as f:
        text = "\n"
        for i in list_of_elements:
            text+=str(i)+' '
        f.write(text)
        f.close()
    
 

writesome( ["Python", "Directories", "and",  "Files ", "exercises", 123456])