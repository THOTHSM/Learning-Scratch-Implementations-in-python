a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
b = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

def dot(a, b):

    def c_len(x):
        l = 0
        if not isinstance(x, list):
            return -1
        for i in x:
            l += 1
        return l

    def create_matrix(r, c):
        matrix = [[0 for _ in range(c)] for _ in range(r)]
        return matrix

    def dot_for_list(l1, l2):
        val = 0
        for i in range(c_len(l1)):
            val += l1[i] * l2[i]
        return val

    # Flattening 1D lists into 2D matrix if necessary
    a = [[x for x in a]] if c_len(a[0]) == -1 else a
    a_r, a_c = c_len(a), c_len(a[0])

    b = [[x for x in b]] if c_len(b[0]) == -1 else b
    b_r, b_c = c_len(b), c_len(b[0])

    # Checking if the shapes align for multiplication
    if a_c != b_r:
        return -1

    # Recursively calculating dot product for higher dimensions
    def recursive_dot(a, b):
        if not isinstance(a[0], list) and not isinstance(b[0], list):
            return dot_for_list(a, b)
        else:
            result = []
            for i in range(len(a)):
                row = []
                for j in range(len(b[0])):
                    val = recursive_dot(a[i], [b[k][j] for k in range(len(b))])
                    row.append(val)
                result.append(row)
            return result

    return recursive_dot(a, b)

print(dot(a, b))
