import datetime
from prac_07.project import Project
"""
Estimate:2 hours
Actual: 2 hrs 47 minutes
"""


def main():
    filename = "projects.txt"
    projects = load_projects(filename)

    menu = """
    Menu:
    L - Load projects
    S - Save projects
    D - Display projects
    F - Filter projects by date
    A - Add new project
    U - Update project
    Q - Quit
    """
    print(menu)
    choice = input(": ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects(filename)
        elif choice == "S":
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice. Please try again.")
        print(menu)
        choice = input(": ").upper()
    save_choice = input(f"Do you want to save the current projects to {filename}? (Y/N): ").upper()
    if save_choice == "Y":
        save_projects(filename, projects)
    print("Thank you for using custom -built project management software!")


def load_projects(filename):
    """Load projects from file"""
    projects = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(", ")
            date_string = parts[1]
            start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            project = Project(parts[0], start_date, int(parts[2]), int(parts[3]))
            projects.append(project)
    return projects

def save_projects(filename, projects):
    """Save projects to file"""
    with open(filename, 'w') as file:
        for project in projects:
            file.write(f"{project.name}, {project.start_date}, {project.priority}\n")


def display_projects(projects):
    """Display sorted incomplete and complete projects"""
    incomplete_projects = []
    complete_projects = []
    for project in projects:
        if not project.is_completed():
            incomplete_projects.append(project)
        else:
            complete_projects.append(project)
    incomplete_projects.sort()
    complete_projects.sort()
    print("\nIncomplete Projects:")
    for project in incomplete_projects:
        print(project)

    print("\nComplete Projects:")
    for project in complete_projects:
        print(project)

def filter_projects_by_date(projects, date):
    """Filter projects by date"""
    filtered_projects = []
    for project in projects:
        if project.start_date >= date:
            filtered_projects.append(project)
    filtered_projects.sort()
    for project in filtered_projects:
        print(project)

def add_new_project(projects):
    """Add new project"""
    print("Lets add a new project")
    name = input("Project name: ")
    while name == "":
        print("Name cannot be blank.")
        name = input("Project name: ")

    start_date = input("Start date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    completion_percentage = int(input("Percent complete: "))
    project = Project(name, start_date, priority, completion_percentage)
    projects.append(project)

def update_project(projects):
    """Update project details"""
    for index, project in enumerate(projects):
        print(f"{index + 1}. {project.name}, {project.start_date}, {project.priority}, {project.completion_percentage}")
    project_index = int(input("Project choice: ")) - 1
    project = projects[project_index]
    new_completion_percentage = int(input("New percentage: "))
    project.completion_percentage = new_completion_percentage
    new_priority = int(input("New priority: "))
    project.priority = new_priority


main()