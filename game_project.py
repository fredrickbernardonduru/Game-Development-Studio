class GameProject:
    def __init__(self, title, designer, developer):
        self.title = title
        self.designer = designer
        self.developer = developer

    def start_project(self):
        return f"Starting project '{self.title}' with designer {self.designer.name} and developer {self.developer.name}."
    
    def launch(self):
        return f"Game '{self.title}' has been successfully launched!"