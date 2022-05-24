# 1 Making empty list
even =[] # For even list
odd =[]  # For odd  list
o = []   # For present store user enter value

# 2 For getting 5 value from user 
for i in range(5):
    a =  int(input("enter a number ")) #User input in int
    o.append(a) #Store user number in 'o' list

# 3 Checking odd/even number in 'o' list
for c in o:
    if int(c)%2 == 0:
        even.append(c)
    else:
        odd.append(c)

# 4 last printing even/odd list
for e in even:
    print(f"Even {e}")

for g in odd:
    print(f"odd  {g}")
