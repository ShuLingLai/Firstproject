#List
mathScores = [60, 70, 10, 20, 81, 63, 4, 70]
print(mathScores[2]) #取得List中某元素
print(mathScores[2:5]) #m到第n-1個
print(mathScores[-1]) #取最後一個元素
print(mathScores[:5]) #取0到第n-1個
print(mathScores[2:]) #取2到最後一個元素
print(len(mathScores)) #取得List元素個數
print(sum(mathScores)) #取得List元素的總和
print(max(mathScores)) #取得List元素的最大值
print(min(mathScores)) #取得List元素的最小值
print(sum(mathScores)/len(mathScores)) #取得List元素的平均值
print(60 in mathScores) #判斷值是否在List中
print(mathScores.count(70)) #計算某元素在List中的個數
print(sorted(mathScores)) #List排序
#--------------------------------------------------------------
chScores = [] #初始化
chScores.append(5) #新增元素
print(chScores)
chScores.insert(0,10) #指定位置新增元素
print(chScores)
#--------------------------------------------------------------
engScores = [60, 70, 10, 20, 81, 63, 4, 70]
del engScores[1:4] #刪除多個,刪除1到n-1個
print(engScores)
engScores.remove(60) #刪除一個
print(engScores)
engScores[2]=99 #修改元素
print(engScores)
#--------------------------------------------------------------
Scores1=[70,80,20,30,91,73,14]
Scores2=['a','b','c','d','e']
print(Scores1 + Scores2) #兩個List串接
#--------------------------------------------------------------
#List in List 課堂練習
grades = [[5, 14, 7], [23, 36, 28], [88, 80, 92]]
print(grades[2]) #數學成績
print(sum(grades[0])/len(grades[0])) #國文成績平均
print(sum(grades[1])/len(grades[1])) #英文成績平均
print(sum(grades[2])/len(grades[2])) #數學成績平均
grades.insert(3,[94, 90, 96])  #新增自然數學成績
print(grades)
#--------------------------------------------------------------
#--------------------------------------------------------------
#Tuple (元素的值不可更改)
TupleScores1 = (1, 2, 3, 4, 5, 1)
TupleScores2 = '6', '7', '8', '9', '10'
print(TupleScores1[2]) #取得Tuple中的某個元素
print(TupleScores2[2]) #取得Tuple中的某個元素
print(TupleScores2.index('6')) #取得某元素在Tuple中的索引
print(TupleScores1.count(1)) #計算某元素在Tuple中的個數
print(TupleScores1 + TupleScores2) #串接兩個Tuple
print(sorted(TupleScores1)) #Tuple排序
print(5 in TupleScores1) #判斷值是否在List中

a, b, c, d, e, f = TupleScores1 #tuple unpacking
print(a, b, c, d, e, f)
#課堂練習
gradesTuple = ((5, 14, 7), (23, 36, 28), (88, 80, 92))
print(gradesTuple[2]) #數學成績
print(sum(gradesTuple[0])/len(gradesTuple[0])) #國文成績平均
print(sum(gradesTuple[1])/len(gradesTuple[1])) #英文成績平均
print(sum(gradesTuple[2])/len(gradesTuple[2])) #數學成績平均
gradesTuple2 = ((94, 90, 96),) #新增自然數學成績
print(gradesTuple + gradesTuple2)
#--------------------------------------------------------------
#--------------------------------------------------------------
#Dictionary