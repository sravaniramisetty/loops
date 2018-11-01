n=int(input("Enter number:"))
even=0
odd=0
for x in range(n):
    if x % 2:
        odd=odd+1
    else:
        even=even+1
print("No of even numbers",even)
print("No odd even numbers",odd)
