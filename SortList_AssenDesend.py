# Using list sort the element as Ascending and Descending order
n = [10, 43, 6, 28, 5]
n.sort()
print("Ascending for Int-num-list:", n)
n.sort(reverse=True)
print("Descending for Int-num-list:", n)

fn = [10.23, 10.12, 6.8, 12.56, 11.8]
fn.sort()
print("Ascending for Float-num-list:", fn)
fn.sort(reverse=True)
print("Descending for Float-num-list:", fn)

sl = ["Banana", "Apple", "Mango", "Grapes", "Coconut"]
sl.sort()
print("Ascending for String-list:", sl)
sl.sort(reverse=True)
print("Descending for String-list:", sl)