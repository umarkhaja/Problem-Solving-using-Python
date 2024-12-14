def odd_nos(p,l):
    if p>l:
        return
    if p%2!=0:
        print(p)
    odd_nos(p+1,l)
odd_nos(1,100)