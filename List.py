Scores=[60,70,10,20,81,63,4]
print(Scores[0])
print(Scores[3:6])
print(Scores[2:5])
print(Scores[-1])
print(Scores[:5])
print(Scores[5:])
print(len(Scores))
print(sum(Scores))
print(max(Scores))
print(sum(Scores)/len(Scores))

ls=[]
ls.append(4)
print(ls)
ls.insert(0, 10)
print(ls)

del Scores[1:4]
print(Scores)

Scores[3]=12
print(Scores)

print(60 in Scores)
print(Scores.count(60))

Scores2=[70,80,20,30,91,73,14]
ls2=['a','b','c','d','e']
print(Scores2 + ls2)

#----------------------------------------
ls = [[1, 3],[6, 5]]
print(ls[0][0])
print(ls[1][0])

print(sorted(Scores))
#----------------------------------------

grades = [[5, 14, 7], [23, 36, 28], [88, 80, 92]]
print(grades[2]) #數學成績
print(sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]))

grades.insert(0, [94, 90, 96])
print(grades)

grades.append([94, 90, 96])
print(grades)