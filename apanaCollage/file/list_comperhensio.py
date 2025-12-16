arr=[1,2,2,3,3,4,5,5,3,6,6]
square=[]
square=([i*i for i in arr if i%2==1])
print(square)

negative=[0 if i%2==1 else i for i in arr]

print(negative)

words=['i', 'm' ,'alpha', 'alphas' 'i', 'am', 'apex' ,'of ','apex' ,'predators']
words=[val.title() for val in words]
print(words)