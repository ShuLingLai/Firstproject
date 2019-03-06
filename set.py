allStudents={'John', 'Eva', 'Jill', 'Eric', 'Andy', 'Albert', 'Polina', 'Kristin', 'Angela'}
guitarClub = {'John', 'Eva', 'Jill', 'Eric', 'Andy'}
danceClub = {'Andy', 'Eric', 'Albert', 'Polina', 'Kristin'}

print(danceClub & guitarClub)
print(guitarClub-danceClub)
print(allStudents-(guitarClub | danceClub))