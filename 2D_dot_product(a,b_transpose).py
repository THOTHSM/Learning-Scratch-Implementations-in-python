a = [[1,2],[2,4]]
b = [[1,2],[3,1]]

def dot(a,b):

    def c_len(x):
        l=0
        if not isinstance(x,list):
            return -1
        for i in x:
            l+=1
        return l
    
    def create_matrix(r,c):
        matrix = [[1 for i in range(c)] for j in range(r)]
        return matrix
    
    def dot_for_list(l1,l2):
        val=0
        for i in range(c_len(l1)):
            val+=l1[i]*l2[i]
        return val


    a = [[x for x in a]] if c_len(a[0]) == -1 else a
    a_r, a_c = c_len(a), c_len(a[0])

    b = [[x for x in b]] if c_len(b[0]) == -1 else b
    b_r, b_c = c_len(b), c_len(b[0])


    if a_c != b_c:
        return -1
    else :
        c_r=b_r
        c_c=a_r
        c= create_matrix(c_r,c_c)

        for i in range(a_r) :
            for j in range(b_r):
                c[j][i]=dot_for_list(a[i],b[j])

        return c

print(dot(a,b))    
