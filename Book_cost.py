'''
Suppose the cover price of a book is $24.95, but bookstores get 40% discount. Shopping costs $3 for first copy and 75%
for each additional copy. What is total wholesale cost for 60 copies?
'''
pr = 24.95
q = 60
t = pr * q
dis = t * 0.40
tpr = t - dis

scost = 1 * 3 + 0.75 * 59
whole_cost = tpr + scost
print("The total Book cost is: " + str(whole_cost))