class SimpleProject:
    def __init__(self):
        self.project_name = "ProjSchool"
    
    def display_project(self):
        print(f"Project Name: {self.project_name}")
        
if __name__ == "__main__":
    project = SimpleProject()
    project.display_project()
