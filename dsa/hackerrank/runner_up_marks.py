n = int(input())
data=[]

for _ in range(n):
    word =input()
    number =float(input())
    data.append([word,number])


scores=[]
j=0

for i in range(len(data)):
    if data[i][1] not in scores:
        scores.append(data[i][1])


scores.sort()
second_lowest=scores[1]
result=[]

for i in range(len(data)):
    if data[i][1]=second_lowest:
        result.append(data[i][0])


result.sort()
for value in result:
    print(value)