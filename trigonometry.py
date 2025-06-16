import math
import re

def solve_trigonometry(expr):
    expr = expr.lower().replace(" ", "")

    if "sin" in expr:
        angle = float(re.findall(r"sin\((\d+)\)", expr)[0])
        return round(math.sin(math.radians(angle)), 4)

    elif "cos" in expr:
        angle = float(re.findall(r"cos\((\d+)\)", expr)[0])
        return round(math.cos(math.radians(angle)), 4)

    elif "tan" in expr:
        angle = float(re.findall(r"tan\((\d+)\)", expr)[0])
        return round(math.tan(math.radians(angle)), 4)

    else:
        return "Unrecognized trigonometric expression."
