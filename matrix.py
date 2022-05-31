
'''
Задача 2

Написать функцию, которая на вход получает квадратную матрицу NхN 
содержащую числовые данные, а на выходе возвращает сумму элементов 
расположенных на диагоналях матрицы. 
Сделать за как можно меньшее кол-во итераций.

'''

matrix =[
	[1,  2,  3  ],
	[10, 20, 30 ],
	[100,200,300],
] 

matrix2 = [
	[2,1,1,1,0],
	[1,2,1,0,1],
	[1,1,2,1,1],
	[1,3,1,2,1],
	[3,1,1,1,2],

]
matrix3 =[
	[1,2,3,4],
	[1,2,3,4],
	[1,2,3,4],
	[1,2,3,4],
]



def calcMatrix(m):
	n=0 #  счетчик 
	l=len(m) # длина стороны матрицы 
	s = 0 # сумма элементов 
	used_els = [] # использованные ячейки запоминаем здесь, что бы не считать дважды 
	for i in m:
		if [n,l-1-n] not in used_els:
			used_els.append([n,l-1-n])
			s+=m[n][l-1-n]

		if [n,n] not in used_els:
			used_els.append([n,n])
			s+=m[n][n]
		n+=1
	
	#print (used_els)
	return s
		
ret =  calcMatrix(matrix2)
# print("сумма элементов расположенных на диагоналях матрицы равна ",ret)


# задание 3 
'''

Написать функцию, которая на входе получает упорядоченный по возрастанию массив размером M, 
содержащий числовые данные, и некое число X, 
которое гарантированно является элементом данного массива. 
Результатом работы функции должен быть индекс элемента X в переданном массиве. 
Сделать за как можно меньшее кол-во итераций.

'''


def findindex(ar, x):
	try:
		pos = ar.index(x) 
		return pos;
	except:
	 	print("число ",x, " не является элементом массива ",ar)
	 	return 0
	


def findindex2(ar,x,beg=0, end=None):
	if  end == None:
		end = len(ar)-1	
		if ar[end]==x:
			return end 

	if ar[beg]==x:
	 	return beg
	if ar[end]==x:
		return  end

	midl = 	round((end-beg)/2)

	midlVal=ar[midl]
	print ('**** beg:',beg,' end:',end,' midl:',midl,' midlVal:',midlVal,' x:',x)

	if midlVal==x:
		return midl

	if midlVal < x:
		end = midl+1
		return findindex2(ar, x, beg, end)

	if midlVal < x:
		beg = midl-1
		return findindex2(ar, x, beg, end)




	


ar = [1,2,5,6,8,100]

x=2
print(ar)
p = findindex2(ar, x)

print("position of ",x, "is ",p)


'''

Web (Обязательно)

REST и SOAP: в каких ситуациях вы выберете один из этих подходов, а в каких другой?

SOAP — это формат протокола, основанный на XML и немного устарел, 
REST — это архитектурный подход может использовать  JSON .

Я выберу REST - если будет выбор
и буду подключаться по SOAP - если другого выбора нет 


'''