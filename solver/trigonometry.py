import math
import re

def solve_trigonometry(question):
    try:
        question = question.lower().replace("°", "")

        match = re.search(r'(sin|cos|tan)\s*\(?(\d+)\)?', question)
        if not match:
            return "Could not parse the trigonometric function."

        func, angle = match.groups()
        angle = float(angle)
        radians = math.radians(angle)

        if func == "sin":
            result = math.sin(radians)
        elif func == "cos":
            result = math.cos(radians)
        elif func == "tan":
            result = math.tan(radians)
        else:
            return "Function not supported."

        return f"{func}({angle}°) = {result:.4f}"

    except Exception as e:
        return f"Error solving trigonometry question: {str(e)}"
