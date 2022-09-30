# 1 2
# 2 3
# 3 6
# 4 10
# 5 15


def n_members(n,coun):
    coun += 1
    print(n)
    if n >  coun:
        return n_members(n,coun) + coun
    else:
         return coun
    

n = 5 
n_members(n, 0)

# p= (n*(n+1))/2
# print(p)