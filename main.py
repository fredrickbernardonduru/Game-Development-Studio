from game_designer import GameDesigner
from developer import Developer
from game_project import GameProject


def main():
    designer = GameDesigner("Jakes", "Figma")
    developer = Developer("Kim" , "Python")

    project = GameProject("Bounce", designer, developer)

    print(designer.introduce())
    print(designer.create_mockup())
    print(developer.introduce())
    print(developer.write_code())
    print(project.start_project())
    print(project.launch())
    
if __name__ == "__main__":
        main()

    