family={}
family['dad']='Homer'
print(family)

family['dad']='Andy'
print(family)

print(family.get('mom'))

print(family.pop('dad'))
print(family)

#family.update({'uncle'：'martin', 'aunt'：'may'})

#-----------------------------------------------------

gradesDict={'chinese':[5,14,7],
            'eng':[23, 36, 28],
            'ma':[88, 80, 92]}
print(gradesDict['ma'])
print(sum(gradesDict['chinese'])/len(gradesDict['chinese']), sum(gradesDict['eng'])/len(gradesDict['eng']), sum(gradesDict['ma'])/len(gradesDict['ma']))

gradesDict['sec']=[94, 90, 96]
print(gradesDict)