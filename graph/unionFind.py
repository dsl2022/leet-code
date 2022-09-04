
size = 10
root = [i for i in range(size)]
rank = [1]* size
print(root,rank)

def find(x):
    while x!= root[x]:
        x= root[x]
    return x



def union(x,y):
    rootX = find(x)
    rootY = find(y)
    if rootX !=rootY:
        if rank[x]>rank[y]:
            root[rootY]= rootX

def connected(x,y):
    if find(x) == find(y):
        return True
    else:
        return False