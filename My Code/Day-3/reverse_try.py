'''You have the list fruits = ['apple', 'banana', 'cherry']. How can you reverse the order of the items in the
list? can you use to remove and return the last item from the list?'''

#List
fruits = ['apple', 'banana', 'cherry']
#before using reverse of this list
print(fruits)

#Reverse this list
fruits.reverse()
print(fruits)

#Now remve last item on this letter
po_pro = fruits.pop()
print(po_pro)
print(fruits)

#Add last item in this list
fruits.append(po_pro)
#Output after reverse method
print(fruits)
