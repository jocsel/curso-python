
def ciclo(a):
	for i in range(len (a)):
		for r in range (len(a) - 1, i,-1):
			if(a[r] < a[r-1]):
				s(a,r,r-1)
def s(a,x,y):
	a[x],a[y]=a[y],a[x]
contador= int(input('Ingresa la cantidad de numeros a ordenar: '))
sort_num=[]
for i in range(contador):
	sort_num.append(int(input('Numero: ')))
ciclo(sort_num)
print('Los numero ordenados son:')
print(sort_num)
print('Los numeros ordenados pares son:')
#
for e in range(len(sort_num)):
	if (sort_num[e])%2==0:
		sort_num.sort()

		print(sort_num[e])
print('Los numeros ordenados impares son:')

for h in range(len(sort_num)):
	if (sort_num[h])%2 !=0:
		sort_num.sort()
		
		print(sort_num[h])