class Person:
    def __init__(self,name,age,hieght,wieght):
        self.name=name
        self.age=age
        self.hieght=hieght
        self.weight=wieght
    def introdoue(self):
        print(f'{self.name} say hello and introdue yourself to the person')
    
person1=Person('artin',12,155,42)
print(person1.name)
print(person1.age)
class empolyee(Person):
    def slary(self):
            print("you've got 4,500,000,000,000,000,000 from your slary")