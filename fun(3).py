def fun(n):
    print(n)
    if n==0:
        return 
    
    fun(n-1)
    print(n-1)
x=int(input("Enter the no:"))
fun(x)