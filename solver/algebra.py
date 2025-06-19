from sympy import symbols, Eq, solve
import re

def solve_equation(equation):
    x = symbols('x')
    eq = Eq(*map(lambda s: eval(s.strip()), equation.split('=')))
    sol = solve(eq, x)
    return sol
