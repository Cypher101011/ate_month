players =['charles','martina','michael', 'forance','eli']

print("here are the first there player on my team: ")
for player in players[1:4:1]:
    print(player.title())
    
my_food=['pizza','falafel','carrot cake']
friend_foods=my_food


my_food.append('burger')
friend_foods.append('something')
print(my_food)
print(friend_foods)

# print(my)
print('first three items in the my food are',my_food[:3],'\n--------------------------------\n')
print(my_food)
print('the three item from the middel of the list are',my_food[1:-1])

print('last three items in the list are ',my_food[-3:])

pizza=['cheese burger','sugar_free','meet','chilli']

friend_pizza=pizza[:]


friend_pizza.append('nothing')
pizza.append('something')
print(pizza,'thes is mi pizza and \n\n -----------------\n','this is friend pizza\n',friend_pizza)

for piz in pizza:
    print('this is piza no : ',pizza.index(piz)+1,piz)
    
for pizzzas in pizza:
    print(pizzzas)
    
# list comperhension for printing pizzs of myh list
[print(f"This is pizza no {i+1}: {p}") for i, p in enumerate(pizza)]
[print(pz) or pz for pz in pizza]