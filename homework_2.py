
class Student:
    def __init__(self,name,age,gender,work,rest,money,mud,):
        self.name = name
        self.age = age
        self.gender = gender
        self.work = work
        self.rest = rest
        self.money = money
        self.mud = mud

    def getStudentInfo(self):
        print("INFO OF 1 YEAR:")
        return "name:" + self.name,"age:" + str(self.age), "gender:" + self.gender,"work:" + str(self.work),"rest:" + str(self.rest),"money:"+str(self.money),"mud:"+str(self.mud)



    def checkWork(self):
        if self.work == True:
            salary = 30
            self.money += salary
            return "Money after salary:" + str(self.money)
        else:
            return "Rest:No rest data about student"

    def checkRest(self):
        if self.rest == True:
            salary = 30
            self.money -= salary
            return "Money after rest:"+str(self.money)
        else:
            return "Rest:No rest data about student"


    def checkMoney(self):
        if self.money == False:
            return "The student has no money so " + self.gender +" went to work"
        else:
            return "Money:" + str(self.money)


    def checkMud(self):
        if self.mud == True:
            return "Mud:Feel happy and went walk with friends"
        else:
            return "Mud:Feel sad and stayed at home"

student = Student("Albert",22,"he",False,True,100,True)

print(student.getStudentInfo())

print(student.checkWork())

print(student.checkRest())

print(student.checkMoney())

print(student.checkMud())