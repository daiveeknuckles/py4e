import re

fhand = open('regex_sum_1778211.txt', 'r')
numlist = list() 

for line in fhand:
    line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    numlist += nums
print(numlist)

sum = 0
for i in numlist:
    sum = sum + int(i)
print(sum)

    
    