row=int(input("Enter the number of rows : "))
column=int(input("Enter the number of columns : "))
print("Enter the matrix")
l=[]
m=[]
for i in range(row):
	l=[int(x) for x in input().split(' ')]
	m.append(l)
# Logic
for i in range(row):
	col=0
	flag=False
	min=m[i][0]
	for j in range(column):
		if m[i][j]<min:
			min=m[i][j]
			col=j
	print('MIN = ',min)
	max=m[0][col]
	for k in range(row):
		if m[k][col]>max:
			max=m[k][col]
	print('MAX = ',max)
	if max==min:
		flag=True
		break	
if flag:
	print('SADDLE POINT = ',max)
else:
	print('NO SADDLE POINT')