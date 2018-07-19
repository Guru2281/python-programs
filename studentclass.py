class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):

	return"name="+self.name+"age:"+self.age

class student(person):
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    def __str__(self):

	return"name="+self.name+"branch:"+self.branch

s=student("guru","cse")
print s
    
