#Given the list data = [10, 20, 30, 40, 50], which method can you use to remove and return the last item from the list?
#List
data = [10, 20, 30, 40, 50]
print(data)

#remove last item and see the list
last_item = data.pop()
print(data)
print(last_item)

#return that iten to the list
data.append(last_item)
print(data)