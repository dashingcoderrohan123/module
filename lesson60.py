#Write a Python program to find the sum and average of the list. The average of the list is defined as the sum of the elements divided by the number of the elements. Also, find the largest and the smallest number in the list.

numbers=[1,2,3,4,5,6,7,8,9]
print(numbers)

count=0

for x in numbers:
    count += x
avg=count/len(numbers) 
print("The sum is :",count)
print("The average is:",avg)  

print(numbers.sort())

print("The smallest element is:",numbers[0])
print("The largest element is:",numbers[-1])