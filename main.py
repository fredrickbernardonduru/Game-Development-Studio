from team_member import TeamMember
from game_designer import GameDesigner
from developer import Developer
from game_project import GameProject


def main():
    member1 = TeamMember("Jakes", "Designer")
    member2 = TeamMember("Kim" , "Developer")

    design_tool1 = GameDesigner("Figma")
    design_tool2 = GameDesigner("Sketch")

    programming_language1 = Developer("Python")
    programming_language2 = Developer("C#")

    GameProject1 = GameProject("Bounce", {})


    print(member1)
    print(member2)
    print(design_tool1)
    print(design_tool2)
    print(programming_language1)
    print(programming_language2)
    print(GameProject1)

if __name__ == "__main__":
        main()

    