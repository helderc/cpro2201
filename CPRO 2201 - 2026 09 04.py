# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:57:30 2026

@author: HOliveira
"""

#%%
d = { 'apple': 5, 'work': 10, 'car': 9 }

print(d['work'])

k = "orange"
if k in d.keys():
    d[k] = d[k] + 1
else:
    d[k] = 1

print(d)

#%% List

my_list = ["test", 1, 2, True]

print(my_list)


my_list.append("something")
print(f"sz: {len(my_list)}")

print("before:", my_list)
#print(my_list[2])
#print(my_list[-1])

my_list.insert(4, "new element")

print("after:", my_list)

#%%

my_list1 = ["test", 1, 2, True]
my_list2 = ["boat", "Python"]

my_final_lst = my_list1 + my_list2

print(my_final_lst)
my_list2.extend(my_list1)
print("my_list2:", my_list2)

#my_list2.remove("test")
my_list2.remove(my_list2[1])
print(my_list2)

my_list2.pop(1)
print(my_list2)

#%%

set1 = {1,2,3,4,5,6,3,2,1}
set2 = {1,3,2,1}

# union
set3 = set1 | set2
set4 = set1.union(set2)

print("set3:",set3)
print("set4", set4)

#%%
# instersection

set1 = {1,2,3,4,5,6,3,2,1}
set2 = {1,3,2,1}

set3 = set1 & set2
print("set3 (intersection):", set3)



































