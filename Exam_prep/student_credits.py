# https://judge.softuni.org/Contests/Practice/Index/3744#1

def students_credits(*data, needed_credits=240):
    output_data = []
    scores = {}
    tot_credits = 0

    for elements in data:
        course, course_credits, max_score, score = elements.split('-')
        course_credits = int(course_credits) * int(score) / int(max_score)
        scores[course] = course_credits
        tot_credits += course_credits

    if tot_credits >= needed_credits:
        output_data.append(f"Diyan gets a diploma with {tot_credits:.1f} credits.")
    else:
        needed = needed_credits - tot_credits
        output_data.append(f"Diyan needs {needed:.1f} credits more for a diploma.")

    scores = dict(sorted(scores.items(), key=lambda x: -x[1]))
    for course in scores:
        output_data.append(f"{course} - {scores[course]:.1f}")
    return '\n'.join(output_data)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

"""print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
"""