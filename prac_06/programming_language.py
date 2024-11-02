"""
Estimate:25 minutes
Actual:38 minutes
"""
from prac_06.language import visual_basic, python, ruby


class ProgrammingLanguage:
    def __init__(self,name="", typing="", reflection="", year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "dynamic"

    def __str__(self):
        return f"{self.name},{self.typing} typing, reflection= {self.reflection},First appeared in {self.year}."



