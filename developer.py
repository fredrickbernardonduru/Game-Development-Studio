from team_member import TeamMember

class Developer(TeamMember):
    def __init__(self, name,programming_language):
        super().__init__(name, "Developer")
        self.programming_language = programming_language

    def write_codes(self):
        return f"{self.name} is wrinting code in {self.programming_language}"
    
