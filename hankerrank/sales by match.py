n = 8
ar = [1,2,1,2,1,3,2]


from  collections import Counter

Count_dict = Counter(ar)

total = 0

for key, values in Count_dict.items():
    total  = total + values//2

print(total)


#### dictionary_values() return a view
### rather than list