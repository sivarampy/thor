#Count ways to assign unique cap to every person
from collections import defaultdict
caps = defaultdict(list)
persons = int(input('Enter number od persons: ')) #input no of persons
total_caps = 100
for i in range(persons):
    temp = map(int,input(f'Enter caps owned by person {i+1}: ').split())
    for j in temp:
        caps[j].append(i)  #in this dict items are cap numbers and values are persons who own those caps
total_mask = (1<<persons)-1 #number of ways we can put persons and caps together
dp = [[-1 for i in range(total_caps+1)] for j in range(1<<persons)] #rows are subsets of total_masks, cols are cap numbers from 0 to 100

def function(mask,cap_number):
    if mask == total_mask: #this condition says that everyone got a cap to wear
        return 1

    if cap_number > total_caps: #if cap_number is greater than total caps then we have to stop reccursion 
        return 0

    if dp[mask][cap_number] != -1: #if we already calculated for that mask then we have to return the value for not calculating it again
        return dp[mask][cap_number] 

    ways = function(mask,cap_number+1) #if the cap_number is not included in the arrangement

    if cap_number in caps:
        for i in caps[cap_number]: # we are give the cap to person if he is not wearing one and moving to next cap 
            if mask & (1<<i): #we are checking whether ith person is having a cap or not, if yes we will continue with next person
                continue
            ways += function((mask | (1<<i)),cap_number+1) #we are giving cap to that ith person as he does have a cap and proceding to next cap
            ways %= ((10**9)+7) #we make sure the value does not exceed this value

    dp[mask][cap_number] = ways
    return dp[mask][cap_number]

print(function(0,1)) #we will start with person-0 means 1st person ans cap number 1
