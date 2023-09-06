data = [2,4,4,4,5,5,7,9]

# # Find how many datas in the list
len = 0
for i in data:
    len += 1
# print(len)

# #Summation of the data in the list
sum = 0
for i in data:
    sum += i
# print(sum)

#Find mean of the list
mean = sum / len
# print(mean)

#Let's find ~(Xi - (X-))
total_sum = 0
for i in data:
    total_sum += (i-mean)**2
#print(total_sum)

#Standard Deviation
sd = (total_sum / (len - 1))**0.5
# print(float(round(sd)))

a=sd-0.00
print(sd)

