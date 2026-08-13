class Factory:
    count = 10 # attribute

    def location(self): # method
        print("Location of Factory")

#print(Factory().count)
#Factory().location() 

obj = Factory() # object/instance of class

print(obj.count)
obj.location()