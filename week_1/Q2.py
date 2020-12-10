num=int(input("Number of input: "))
data =[]
for i in range(num):
    roll_num =input("Roll Number: " )
    name= input("Name: ")
    age=input("Age: ")
    marks = input("Marks: ")
    sdata={"Rollnum":roll_num, "Name":name,"Age":age, "Marks":marks}
    #print(sdata)
    data.append(sdata)
    print("\n")

#print(data)
print("\n")
print ("{:<7} {:<15} {:<5} {:<6}".format("Roll Num", "Name", "Age", "Marks"))
total=0
high=0
low=100

for  v,val in enumerate(data):
    total += int(data[v]['Marks'])
    if int(data[v]['Marks'])>high:
        high=int(data[v]['Marks'])
    if int(data[v]['Marks'])<low:
        low=int(data[v]['Marks'])    
    print ("{:<6} {:<15} {:<5} {:<7}".format(data[v]['Rollnum'], data[v]['Name'], data[v]['Age'], data[v]['Marks']))
print("\n\n\n\n")

average=total/num

print ("{:<12} {:<12} {:<12}".format("Class Average","Class Highest", "Class Lowest"))
print ("{:<12} {:<12} {:<12}".format(str(average),str(low),str(high)))
num=int(input("Number of input: "))
data =[]
for i in range(num):
    roll_num =input("Roll Number: " )
    name= input("Name: ")
    age=input("Age: ")
    marks = input("Marks: ")
    sdata={"Rollnum":roll_num, "Name":name,"Age":age, "Marks":marks}
    #print(sdata)
    data.append(sdata)
    print("\n")

#print(data)
print("\n")
print ("{:<7} {:<15} {:<5} {:<6}".format("Roll Num", "Name", "Age", "Marks"))
total=0
high=0
low=100

for  v,val in enumerate(data):
    total += int(data[v]['Marks'])
    if int(data[v]['Marks'])>high:
        high=int(data[v]['Marks'])
    if int(data[v]['Marks'])<low:
        low=int(data[v]['Marks'])    
    print ("{:<6} {:<15} {:<5} {:<7}".format(data[v]['Rollnum'], data[v]['Name'], data[v]['Age'], data[v]['Marks']))
print("\n\n\n\n")

average=total/num

print ("{:<12} {:<12} {:<12}".format("Class Average","Class Highest", "Class Lowest"))
print ("{:<12} {:<12} {:<12}".format(str(average),str(low),str(high)))
