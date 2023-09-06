#Let's Start

#Input
data = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


#Find row size of this list
row_size = len(data)

#Find column size of this list
column_size = 0
for i in range(row_size):
    len_column = len(data[i])
    if column_size <len_column:
        column_size = len_column
# print(column_size)
print('Input:')
for row in data:
    print(row)

print('\n')
    
# Create an empty 2D list using list comprehension
data2 = [[0 for i in range(column_size)] for j in range(row_size)]

# # Print the empty 2D list
# print('Empty 2D List:')
# for row in data2:
#     print(row)

# print('\n')

#Outut-1
print('Output - 1:')
for row in range(row_size):
    for column in range(column_size):
        # print(data[row][column])
        if (data[row][column])>=10:
           if (data[row][column]) % 10 == 0:
               data2[row][column] = 1
           else:
               data2[row][column] = (data[row][column]) % 10
        else:
            data2[row][column] = data[row][column]

for row in data2:
    print(row)

print('\n')

#Output-2

# Create an empty 2D list using list comprehension
data3 = [[0 for i in range(column_size)] for j in range(row_size)]

print('Output - 2:')
for row in range(row_size):
    for column in range(column_size):
        if (data2[row][column]) % 2 != 0:
            data3[row][column] = 'Odd'
        else:
            data3[row][column] = 'Even'

for row in data3:
    print(row)
print('\n')

#Output - 3
row_sum = 0
output3= []
# print(type(output3))
print('Output - 3:')
for row in range(row_size):
    for column in range(column_size):
        row_sum += int(data2[row][column])
    output3.append(row_sum)
    row_sum = 0

print(output3)
print('\n')

#Output - 4
print('Output - 4:')
output4=[]
for item in output3:
    if (item % 2) != 0:
        output4.append('Odd')
    else:
        output4.append('Even')
    

print(output4)
print('\n')