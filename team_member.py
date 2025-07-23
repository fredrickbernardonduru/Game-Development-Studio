class TeamMember:
    def __init__ (self, name, role):
        self.name = name
        self.role = role
    
    def __str__(self):
        return f"Hi, I'm {self.name} and I work as a {self.role}"