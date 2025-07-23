from team_member import TeamMember

class GameDesigner(TeamMember):
    def __init__(self, name, role,design_tool ):
        super().__init__(name, role)
        self.design_tool = design_tool

    def __str__(self):
        return f"{self.name} is creating mockups using {self.design_tool}"