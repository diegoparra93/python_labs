def transpose(mat):
    # If esta vacio, uso esta formula. 
    if mat == []:
        return []
    
    # Check el tamano del primer row
    size = len(mat[0])
    
    # проверьте, имеют ли все строки одинаковый размер - verificar si todas las rows tienen el mismo tamano
    for row in mat:
        if len(row) != size:
            raise ValueError("not rectangular")
    
    new_matrix = []
    
    # Para cada columna - для каждого столбца
    for j in range(len(mat[0])):
        new_row = []
        # For each row  
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        new_matrix.append(new_row)
    
    return new_matrix

def row_sums(mat):
    if mat == []:
        return []
    
    # Check if rectangular - проверьте, является ли он прямоугольным
    first_size = len(mat[0])
    for row in mat:
        if len(row) != first_size:
            raise ValueError("different rows")
    
    results = []
    for row in mat:
        # Sum the row
        total = 0
        for number in row:
            total += number
        results.append(total)
    
    return results

def col_sums(mat):
    if not mat:
        return []
    
    # Check if all rows same size
    size = len(mat[0])
    for row in mat:
        if len(row) != size:
            raise ValueError("weird matrix")
    
    sums = []
    # For each column
    for col in range(len(mat[0])):
        s = 0
        # Sum that column in all rows
        for row in range(len(mat)):
            s = s + mat[row][col]
        sums.append(s)
    
    return sums

# Testing the functions
print("=== Testing transpose ===")
test1 = transpose([[1, 2, 3]])
print("Input: [[1, 2, 3]]")
print("Output:", test1)
print()

test2 = transpose([[1, 2], [3, 4]])
print("Input: [[1, 2], [3, 4]]")
print("Output:", test2)
print()

print("=== Testing row_sums ===")
test3 = row_sums([[1, 2, 3], [4, 5, 6]])
print("Input: [[1, 2, 3], [4, 5, 6]]")
print("Output:", test3)
print()

print("=== Testing col_sums ===")
test4 = col_sums([[1, 2, 3], [4, 5, 6]])
print("Input: [[1, 2, 3], [4, 5, 6]]")
print("Output:", test4)
print()

# Test with error
print("=== Testing error case ===")
try:
    bad_test = transpose([[1, 2], [3]])
    print("This should not print")
except ValueError as e:
    print("Good! Got error:", e)