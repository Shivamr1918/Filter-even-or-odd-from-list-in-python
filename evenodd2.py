odd =[]
even =[]

for i in range(4):
    userinput = int(input("Enter number : "))
    if userinput%2 == 0:
        even.append(userinput)
    else:
        odd.append(userinput)

for c in even:
    print(f"Even {c}")
for d in odd:
    print(f"Odd {d}")

