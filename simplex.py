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
        self.b=[]

        # Utils
        self.utils = utils
        self.min_col_idx = -10
        self.min_row_idx = -10
        self.matrix=[[]]
    
    def choose_case(self):
        # Problema com apenas <=
        bub_min = utils.find_neg(self.bub) # (min, False | True)

        if(len(Aeq) == 0 and bub_min[1] == False):
            self.upper_bound_case()
        else:
            self.big_m_case()
    
    def upper_bound_case(self):
        print("Upper bound case")

        # Building the first row
        self.matrix[0].extend(self.c)
        self.matrix[0].extend([0 for i in self.bub])

        # Building constraint rows
        for i in range(len(self.bub)):
            row = i+1
            self.matrix.append([])
            self.matrix[row].extend(self.Aub[row-1])
            self.matrix[row].extend([1 if _ == i else 0 for _ in range(len(self.bub))])

        self.b=[0].extend(self.bub)
        print(self.matrix)
        min_col = self.utils.find_min_col(self.matrix)
        print(min_col)
        print(self.utils.find_min_row(self.matrix, self.b, min_col[1]))
        
    def big_m_case(self):
        print("Big m case")

class utils:            
    def __init__(self):
        pass

    def find_neg(self, arr):
        minimum = min(arr)
        if minimum < 0:
            return (minimum, True)
        else:
            return (minimum, False)

    def find_min_col(self, matrix):
        index_min = min(range(len(matrix[0])), key=matrix[0].__getitem__)
        return (matrix[0][index_min], index_min)

    def find_min_row(self, matrix, b, min_col_idx):
        min = -10e4
        index_min = -10

        for idx, row in enumerate(matrix):
            el = row[min_col_idx]
            if(el < 0): continue
            if(min > b[idx]/el):
                min = b[idx]/el
                index_min = idx
        return (min, index_min)
            

# LOWER BOUND CASE
obj = [-3, -2]
 
# Constraints Left side x and y Coefficient matrix
Aub = [[2,  1],   # 0x1 + 2x2
            [1,  1],   # x1 + 2x2
            [1, 0]]  # 1x1 + 1x2
 
# right side values matrix
bub = [100,  # ......<= 50
        80,  # ......<= 25
        40]  # ..... <= 15

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