class Project:
    def __init__(self, name="", start_date="", priority="", completion_percent=""):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.completion_percent = completion_percent

    def __str__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, {self.completion_percent}%"

    def is_completed(self):
        return self.completion_percent == 100

    def __lt__(self, other):
        return self.priority < other.priority
