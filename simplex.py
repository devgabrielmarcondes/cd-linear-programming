class optimize:
    def __init__(self, c, A_ub=None, b_ub=None, A_eq=None, b_eq=None):
        self.M = 10e4
        self.c=c
        self.Aub=A_ub
        self.bub=b_ub
        self.Aeq=A_eq
        self.beq=b_eq

        # Return
        self.x = []
        self.b= [0]

        # Utils
        self.utils = utils()
        self.min_col_idx = -10
        self.min_row_idx = -10
        self.matrix=[[]]
    
    def choose_case(self):
        # Problema com apenas <=
        bub_min = self.utils.find_neg(self.bub) # (min, False | True)

        if(len(Aeq) == 0 and bub_min[1] == False):
            self.upper_bound_case()
        else:
            self.big_m_case()
    
    def upper_bound_case(self):
        print("Upper bound case")

        # Building the first row
        self.matrix[0].extend(self.c)
        self.matrix[0].extend([0 for i in self.bub])
        self.matrix[0].extend([0]) # First "b" value

        # Building constraint rows
        for i in range(len(self.bub)):
            row = i+1
            self.matrix.append([])
            self.matrix[row].extend(self.Aub[row-1])
            self.matrix[row].extend([1 if _ == i else 0 for _ in range(len(self.bub))]) # Loose values
            self.matrix[row].append(self.bub[i]) # Append b values

        self.b.extend(self.bub) # Initial b vector
        print(self.matrix)

        while self.utils.find_neg(self.matrix[0])[1]:
            min_col = self.utils.find_min_col(self.matrix[0]) # For the first row
            min_row = self.utils.find_min_row(self.matrix, self.b, min_col[1])
            self.matrix, self.b = self.utils.pivot(self.matrix, min_row[1], min_col[1])
            print(self.matrix)
        print(f"Final b: {self.b}")
        
    def big_m_case(self):
        print("Big m case")

class utils:            
    def __init__(self):
        pass

    def find_neg(self, row):
        minimum = min(row)
        if minimum < 0:
            return (minimum, True)
        else:
            return (minimum, False)

    def find_min_col(self, row):
        index_min = min(range(len(row)), key=row.__getitem__)
        return (row[index_min], index_min)

    def find_min_row(self, matrix, b, min_col_idx):
        minimum = 10e4
        index_min = -10

        for idx, row in enumerate(matrix):
            el = row[min_col_idx]
            if(el <= 0): continue # Changed from < to <= because of division by 0
            if(minimum > b[idx]/el):
                minimum = b[idx]/el
                index_min = idx
        return (minimum, index_min)

    def pivot(self, matrix, row, col):
        pivot = matrix[row][col]

        #Divide by the element
        for i in range(len(matrix[row])):
            matrix[row][i] /= pivot

        # Eliminate the other rows
        for i in range(len(matrix)):
            if i != row:
                factor = matrix[i][col]
                for j in range(len(matrix[i])):
                    matrix[i][j] -= factor * matrix[row][j]

        newB = [r[len(r)-1] for r in matrix]
        
        return (matrix, newB)
            

# LOWER BOUND CASE
obj = [-3, -2]
 
# Constraints Left side x and y Coefficient matrix
Aub = [[2,  1],   # 2x1 + x2
            [1,  1],   # x1 + x2
            [1, 0]]  # x1 
 
# right side values matrix
bub = [100,  # ......<= 100
        80,  # ......<= 80
        40]  # ..... <= 40

Aeq = []
beq = []


"""
# BIG M CASE

obj = [-3, -1]
 
# Constraints Left side x and y Coefficient matrix
Aub = [[-1,  -1],   # 0x1 + 2x2
            [2,  1],   # x1 + 2x2
            [-1, -1]]  # 1x1 + 1x2
 
# right side values matrix
bub = [-3,  # ......<= 50
            4,  # ......<= 25
            0]  # ..... <= 15

Aeq = [[1,1]]
beq = [3]
"""


opt = optimize(obj, Aub, bub, Aeq, beq)
opt.choose_case()