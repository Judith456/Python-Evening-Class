from multipledispatch import dispatch

@dispatch(int, int)
def sum(w,r):
    result = w + r
    print(result)

@dispatch(int, int, int)  
def sum(w, r, t):
    result = w + r + t
    #print(f"the resultf the sum is {result}")
    print(result)
    
sum(5, 10)
sum(5, 10, 3)