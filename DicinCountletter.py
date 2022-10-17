import numpy as np

freq = {}
line =input("Enter Your Line here : ")
for word in line.split():
    if word in freq:
        freq[word] = 1 + freq[word]
    else:
        freq[word] = 1
print(freq)
print(freq.keys())
print(freq.values())
l1 = list(freq.items())
print(l1)
arr = np.array(l1)
print(arr)