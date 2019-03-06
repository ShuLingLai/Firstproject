r = input('請輸入直徑')
print (int(r)**2*3.14)

scores = [10, 30, 40, 90, 100, 60]
print(round(sum(scores)/len(scores)))

scores[0] = scores[0]**0.5*10
scores[1] = scores[1]**0.5*10
scores[2] = scores[2]**0.5*10
scores[3] = scores[3]**0.5*10
scores[4] = scores[4]**0.5*10
scores[5] = scores[5]**0.5*10
print(scores)

score = 60
if score >= 60:
    print('及格了')
else:
    print('不及格')
sex = input('請輸入性別:')
tall = input('請輸入身高:')

if sex == 'm' and int(tall) >= 190:
    print('打籃球')
elif sex == 'f' and int(tall) >= 170:
    print('打排球')


num = input('請輸入數字')
if  int(num) % 2 == 0:
    print('偶數')
else:
    print('奇數')

for i in range(0, 10):
    print(i)
for i in range(0, 10, 2):
    print(i)

mathScores = [60, 70, 10, 20, 81, 63, 4]
l = len(mathScores)

for i in range(0, l):
    print(i, mathScores[i])

for item in mathScores:
    print(item*10)

print(list(item*10 for item in mathScores))

family = {'dad': 'Homer',
          'mom': 'Lisa'}
for title, name in family.items():
    print(title, name)
for i in family.items():
    print(i)
for i, j in family.items():
    print(i,j)



X = (1, 2, 3)
Y = (4, 5, 6)
Z = (7, 8, 9)
for x, y, z in zip(X, Y, Z):
    print(x, y, z)


count = 0
while count < 10:
    print(count)
    count += 1
else:
    print('count >= 10')

for i in range(0, 20):
    if i % 2 == 1:
        print(i)

mathScores = [60, 70, 10, 20, 81, 63, 4]

for item in mathScores:
    if item > 80:
        break
    print(item)

for item in mathScores:
    if item > 80:
        continue
    print(item)


