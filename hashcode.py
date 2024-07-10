x=input()
x=x.split()
noofcontributor=int(x[0])
noofproject=int(x[1])
contributor=[]
for i in range (0,noofcontributor):
    contributor.append([])
    name=input()
    name=name.split()
    skillno=int(name[1])
    contributor[i].append(name)
    for j in range(0,skillno):
        skill=input()
        skill=skill.split()
        contributor[i].append(skill)

project=[]
for i in range(0,noofproject):
    name=input()
