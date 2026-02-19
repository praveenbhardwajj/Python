class Student():
    def __init__(self,name,phy,math,che):
        self.name=name
        self.phy=phy
        self.math=math
        self.che=che
    def Avg(self):
        sum=self.phy + self.che + self.math
        Avg_marks=sum/3
        print(self.name)
        print("Average of marks " ,Avg_marks)

obj=Student("Rahul",30,30,40)
obj.Avg()