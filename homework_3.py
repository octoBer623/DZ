from pyclbr import readmodule_ex


class Person:
    def __init__(self ,name , surname):
        self.name = name
        self.surname = surname



class User(Person):
    def __init__(self , password, email,name,surname):
        super().__init__(name,surname)
        self.password = password
        self.email = email

    def GetInfo(self):
        return "name:" + self.name, "surname:" + self.surname,"email:" + self.email,"password:" + self.password


    def CheckPassword(self,ch_pass):
        if self.password == ch_pass:
            self.password = ch_pass
            return "Correct password:"+ self.password
        else:
            return "Wrong password try again"

    def ChangePassword(self,newpassword):
        self.password = newpassword
        return "New password:" + self.password

    def UpdateName(self,newname):
        self.name = newname
        return "New name:" + self.name

octo = User("Andryxa","AnderiHalko@gmail.com","Anderei","Grigorevich")

print(octo.GetInfo())
print(octo.CheckPassword("Andryxa"))
print(octo.ChangePassword("Egor2312334"))
print(octo.UpdateName("Egor"))
