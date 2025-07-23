from team_member import TeamMember

class Developer(TeamMember):
    def __init__(self, name, role,programming_language):
        super().__init__(name, role)
        self.programming_language = programming_language
        