class Cat:
    def __init__(self, name , age , breed , color ,position ):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.position = position

    def getAll(self):
        return "name:" + self.name,"age:" + str(self.age),"breed:" + self.breed,"color:" + self.color,"position:" + self.position

mycat = Cat("Genadiy",3,"Big Cats","White","running")

cat_info = mycat.getAll()

print(cat_info)

