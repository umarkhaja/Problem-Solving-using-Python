def natural_numbers(n):
    if n>0:
       natural_numbers(n-1)
       print(n)
n=int(input("Enter a no:"))
print(natural_numbers(n))
