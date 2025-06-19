import re
import math

def solve_geometry(question):
    try:
        question = question.lower()

        if "area" in question and "circle" in question:
            radius = float(re.findall(r'\d+', question)[0])
            area = math.pi * radius ** 2
            return f"Area of circle: {area:.2f}"

        elif "perimeter" in question and "rectangle" in question:
            numbers = list(map(float, re.findall(r'\d+', question)))
            if len(numbers) == 2:
                length, width = numbers
                perimeter = 2 * (length + width)
                return f"Perimeter of rectangle: {perimeter:.2f}"

        elif "area" in question and "rectangle" in question:
            numbers = list(map(float, re.findall(r'\d+', question)))
            if len(numbers) == 2:
                length, width = numbers
                area = length * width
                return f"Area of rectangle: {area:.2f}"

        elif "area" in question and "triangle" in question:
            numbers = list(map(float, re.findall(r'\d+', question)))
            if len(numbers) == 2:
                base, height = numbers
                area = 0.5 * base * height
                return f"Area of triangle: {area:.2f}"

        return "Unable to solve geometry question. Please provide complete data."

    except Exception as e:
        return f"Error solving geometry question: {str(e)}"
