#Given the list animals = ['dog', 'cat', 'elephant', 'lion'], how can you replace 'elephant' with 'tiger'?
#List 
animals = ['dog', 'cat', 'elephant', 'elephant', 'lion']
print(animals)

#Replace 'elephant' with 'tiger'
#Find index of elephant
index_ele = animals.index('elephant')
print(index_ele)

# #Remove 'elephant' from the list
animals.pop(index_ele)
print(animals)

# #Now insert 'tiger' same index of 'elephant'
animals.insert(index_ele,'tiger')
print(animals)