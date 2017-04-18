# script to output the numbers entered by the user but stop if number is 42
print('Enter the Numbers: ')
array_nums = [int(x) for x in input().split()]
print('Entered list is : ' + str(array_nums))
for num in array_nums:
    if num != 42:
        print(num)
        break
print('we are done bro.')
