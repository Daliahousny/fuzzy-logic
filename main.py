class variable:
    def __int__(self,name,crisp,range,fuzzysets):
        self.name=name
        self.crisp=crisp
        self.range=range
        self.fuzzysets=[]
        self.fuzzyset=fuzzySet()
    def setName(self,n):
        self.name=n
    def getName(self):
        return self.name
    def setCrisp(self,c):
        self.crisp=c
    def getCrisp(self):
        return self.crisp
    def setRange(self,r):
        self.range=r
    def getRange(self):
        return self.range
    def setFuzzySet(self,fs):
        self.fuzzysets=fs
    def getFuzzySet(self):
        return self.fuzzysets
    def fuzzification(self,x_coordinates,y_coordinates,inputv):
        for var in inputv:
            crisp=variable.getCrisp(self)
            for fuzzyset in variable.getFuzzySet(self):
                if (crisp<fuzzyset.x_coordinates[0]|crisp>fuzzyset.x_coordinates[-1]): # value outside set
                    fuzzyset.sety(0)
                elif (crisp>fuzzyset.x_coordinates[0]|crisp<fuzzyset.x_coordinates[-1]): #value inside set
                    for i in x_coordinates:
                        if(crisp==fuzzyset.x_coordinates[i]):
                            fuzzyset.sety(y_coordinates[i])



class fuzzySet:
    def __int__(self,type,x_coordinates,y_coordinates):
        self.type = type
        self.x_coordinates=x_coordinates
        self.y_coordinates=y_coordinates
    def setType(self,t):
        self._type=t
    def getType(self):
        return self._type
    def setx(self,x):
        self.x_coordinates=x
    def getx(self):
        return self.x_coordinates
    def sety(self):
        if(self.getType()=="TRI"):
            self.y_coordinates=[0,1,0]
        elif(self.getType()=="TRAP"):
            self.y_coordinates=[0,1,1,0]
    def gety(self):
        return self.y_coordinates


class ToolBox:
    def __int__(self,inVar,outVar):
        self.inVar=inVar
        self.outVar=outVar

    def setinVar(self,inv):
        self.inVar=inv
    def getinVar(self):
        return self.inVar
    def setoutVar(self,outv):
        self.outVar=outv
    def getoutVar(self):
        return self.outVar




v=variable()
f=fuzzySet()
n=input("please enter variable name")
name=v.setName(n)
c=input("enter the crisp variable")
crisp=v.setCrisp(c)
fin=input("enter fuzzy set type")
t=f.setType(fin)
tt=f.getType()
print(tt)
xc=input("enter the x coordinates for the fuzzy set")
x=f.setx(xc)
y=f.sety()
print(f.gety())



#
# f=fuzzySet()
# t=f.setType("TRI")
# x=f.setx([0,0,15])
# # f.setType("TRI")
# # f.setType("TRAP")
# # print(f.get_y())
#
# v=variable()
# a=v.addFuzzy(t,x)
# print(a)
# fs=input("enter the fuzzy sets")
# n=v.setFuzzySet(fs)
# g=v.getFuzzySet()
# ff=v.addFuzzy()
# print(ff)
#
#
#
# # vv=v.addFuzzy()
# # print(vv)
#
# v.setName("slow")
# print(v.getName())