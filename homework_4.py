
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

    def CheckChange_Password(self):
        check_pass = input("\nEnter password:")
        if check_pass == self.password:
            print("Old password:" + self.password)
            change_pass = input("\nenter new password:")
            self.password = change_pass
            return "New password:" + self.password
        else:
            return "Wrong password try again later!"



    def UpdateName(self):
        new_name = input("\n\nNew name:")
        self.name = new_name
        return "name(changed recently):" + self.name, "surname:" + self.surname,"email:" + self.email,"password(changed recently):" + self.password

octo = User("Andryxa","AnderiHalko@gmail.com","Anderei","Grigorevich")

print(octo.GetInfo())
print(octo.CheckChange_Password())
print(octo.UpdateName())