class Person :
    def __init__(self,param_name):
        print("i am f",self)
        self.name=param_name
    def talk(self):
        print("안녕하세요 이름은 ",self.name)
person1=Person("유재속")
person2=Person("박명")
print(person1.name)
print(person2.name)
person1.talk()
person2.talk()
