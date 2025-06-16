import re
import math

def solve_geometry(question):
    question = question.lower()

    if "area of circle" in question:
        r = float(re.findall(r"radius\s*(\d+)", question)[0])
        return round(math.pi * r ** 2, 2)

    elif "perimeter of square" in question:
        s = float(re.findall(r"side\s*(\d+)", question)[0])
        return 4 * s

    else:
        return "Geometry formula not recognized."
