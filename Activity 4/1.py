# 1.	Write a Python function to find the largest of the three numbers entered as the function parameters.

def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
print(largest(1,2,3))
print(largest(1,3,2))
print(largest(3,2,1))
print(largest(3,1,2))
print(largest(2,1,3))
print(largest(2,3,1))

