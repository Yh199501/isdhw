import math
class Circle:
    def Circle(self,r):
        return math.pi*r*r
class Ellipse:
    def Ellipse(self,m,n):
        return(math.pi*m*n)
class Rectangle:
    def Rectangle(self,x,y):
        return x*y
class Square:
    def Square(self,z):
        return(z*z)
class TotalArea(Ellipse,Square,Rectangle,Circle):
    number=0
    def compute_area(self,shapes):
        a=TotalArea()
        b=[]
        m=shapes
        n=m.split(',')
        j=0
        c=0
        while(j<len(n)):
            n[j]='a.'+n[j]
            if(ord(n[j][len(n[j])-1])>=48 and ord(n[j][len(n[j])-1])<=57):
                n[j]=n[j]+','+n[j+1]
                b.append(j+1)
                j=j+1
            j=j+1
        for i in b:
            del n[i-c]
            c=c+1
        for j in range(0,len(n)):
            exec('TotalArea.number+='+n[j])
        return(TotalArea.number)
b=TotalArea()
print("这些图形的面积之和是：",b.compute_area(input("请输入一个图形列表，例如Ellipse(10,20),Square(15)),Rectangle(20,15),Circle(5):")))

