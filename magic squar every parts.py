list=[
    [8,3,4],
    [1,5,9],
    [6,7,2]
]
i=0
while i<len(list):
    j=0
    row=0
    column=0
    diagonal=0
    while j<len(list[i]):
        row=row+list[i][j]
        column=column+list[i][j]
        diagonal=diagonal+list[j][i]
        j+=1
    i+=1
if row==column==diagonal:
    print("magic sq")
else:
    print("not")
print(row,"=sum of row")
print(column,"=sum of column")
print(diagonal,"=sum of diagonal")