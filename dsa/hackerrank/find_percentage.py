n = int(input())
student_with_marks=[]

for i in range(n):
    student_with_marks.append(input())
    
student=input()

array=[]
for i in range (n):
    array.append(student_with_marks[i].split())

# print(student_with_marks)
# print(student)
# print(array)
temp=[]
for i in range(n):
    if student==array[i][0]:
      for index, item in enumerate(array[i]):
         if index==0:
            continue
         else:
            temp.append(item)
           
        #  print(item)
        #  print(index)
        

        # print(item)
integer_list = [float(value) for value in temp]
add=float(sum(integer_list))
average=float(add/3.00)
# print(float(add))
average=f"{average:.2f}"
print(average)