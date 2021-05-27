#This is a commond
print("Hello Word")
'''This is a multi-line command'''


#declaration of variable
a=10
b=10.5
c="Akash Technology"
print(a)
print("This is value of b:",b)
print("Company name is:",c)


#Change the variable
name="Akash Technolabs"
print("Name is:",name)
#assing new value
name="Akashsir.com"
print("Name is:",name)

#assing multiple vale in multiple variable
a,b,c= 10,10.5,"Akash Technology"
print(a)
print("This is value of b:",b)
print("Company name is:",c)

#Check the datatype
n1=10
print(n1,"is of type",type(n1))
n2=10.5
print(n2,"is complex number?",isinstance(10.5,int))
n3=1 + 2j
print(n2,"is complex number?",isinstance(1 +2j,complex))


#String Functions
Name ="Akash technolabe"
print(name)
 #print selected character of string
print(name[2])
 #print character strting from 3rd to 5th
print(name[2:5])
 #print strting from 3rd to character 
print(name[2:])
#print string two time
print(name*2)
#concatenated string
print(name+ "Hey")


#list datatype
list1 =[10,10.5,"Akash Technology"]
print(list1)

list1=[10,20,30,'Akash',40,50,"Technology",60]
print("list[2]=",list1[2])
print("list[0:3]=",list1[0:3])


#tuple
tuple1 =(10,10.5,"Akash Technology")
print(tuple1)

tuple1=[10,20,30,'Akash',40,50,"Technology",60]
print("list[2]=",tuple1[2])
print("list[0:3]=",tuple1[0:3])


#dictionarydatatype
d={1:'Akash',2:'Technology','key':10}
print(type(d))
print("d[1]=",d[1])
print("d[2]=",d[2])
print("d['key']=",d['key'])