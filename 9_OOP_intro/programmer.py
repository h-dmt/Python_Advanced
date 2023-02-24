# A class called Programmer. Upon initialization, it should receive name (string), language
# (string), skills (integer). The class should have two methods:
#     • watch_course(course_name, language, skills_earned)
#         ◦ If the programmer's language is the same as the one on the course, increase his skills with
#         the given amount and return a message "{name} watched {course_name}".
#         ◦ Otherwise return "{name} does not know {language}".
#     • change_language(new_language, skills_needed)
#         ◦ If the programmer has the skills and the new language is not the same as his,
#         change his language to the new one and return
#         "{name} switched from {previous_language} to {new_language}".
#         ◦ If the programmer has the skills, but the given language is equal to his return
#         "{name} already knows {language}".
#         ◦ In the last case, the programmer does not have enough skills, so return
#         "{name} needs {needed_skills} more skills" and do not change his language.

class Programmer:
    def __init__(self, name, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"

        else:
            return f"{self.name} does not know {language}"

    def change_language(self, new_language, skills_needed):
        if skills_needed <= self.skills:
            if new_language != self.language:
                message = f"{self.name} switched from {self.language} to {new_language}"
                self.language = new_language
                return message

            else:
                return f"{self.name} already knows {new_language}"

        else:
            needed_skills = skills_needed - self.skills
            return f"{self.name} needs {needed_skills} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
