
from scipy.optimize import linprog
 
# Objective function's Coefficient matrix
obj = [-3, -1]
 
# Constraints Left side x and y Coefficient matrix
lhs_ineq = [[-1,  -1],   # -x1 -x2
            [2,  1],   # 2x1 + 1x2
            [-1, -1]]  # -x1 -x2
 
# right side values matrix
rhs_ineq = [-3,  # ......<= -3
            4,  # ......<= 4
            0]  # ..... <= 0

Aeq = [[1,1]]
beq = [3]


opt = linprog(c=obj,
              A_ub=lhs_ineq,
              b_ub=rhs_ineq,
              A_eq=Aeq,
              b_eq=beq,
              method="highs")
 
# printing the solution
print(opt)
