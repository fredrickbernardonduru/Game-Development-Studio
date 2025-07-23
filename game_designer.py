from team_member import TeamMember

class GameDesigner(TeamMember):
    def __init__(self, name,design_tool ):
        super().__init__(name, "Game Designer")
        self.design_tool = design_tool

    def create_mockup(self):
        return f"{self.name} is creating mockups using {self.design_tool}"