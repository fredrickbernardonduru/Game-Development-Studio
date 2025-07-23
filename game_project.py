class GameProject:
    def __init__(self, title, designer, developer):
        self.title = title
        self.designer = designer
        self.developer = developer

    def start_project(self):
        return f"Starting project {self.title} with designer {self}"
        
