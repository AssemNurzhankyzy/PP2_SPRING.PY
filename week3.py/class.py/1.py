class String:
    def getstring(self):
        self.sentence=input("Sentence:")
    def printstring(self):
        print(" upper case:"+self.sentence.upper())
        
mystring=String()
mystring.getstring()
mystring.printstring()

