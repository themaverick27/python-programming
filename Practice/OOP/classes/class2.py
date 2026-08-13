class Factory:
    def __init__(self, materials, zips, pockets): 
        #print(self) # self target specific location of object
        self.materials = materials 
        self.zips = zips
        self.pockets = pockets

    def show(self): 
        print(f"Your object details are: {self.materials}, {self.zips} and {self.pockets}")


reebok = Factory("leather", 4, 3)
campus = Factory("Nylon", 2, 2)

reebok.show()
campus.show()
