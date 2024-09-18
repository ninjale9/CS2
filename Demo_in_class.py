def recursions (n) :
    if n <= 1 :
        return 1 
    return n + recursions(n-1)
    pass
def recursions_list(n) : 
    if not n :
        return 0
    return n[0] + recursions_list(n[1:])
print(recursions_list([2,4,5,6,7]))

def sum_series(n) : 
    if n <= 0 :
        return 0 
    return n + sum_series(n-2) 

print(sum_series(6))
