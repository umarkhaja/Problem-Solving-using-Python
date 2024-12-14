def even_nos(p,l):
    if(p>l):
        return
    if(p%2==0):
        print(p)
    even_nos(p+1,l)
even_nos(1,100)
        