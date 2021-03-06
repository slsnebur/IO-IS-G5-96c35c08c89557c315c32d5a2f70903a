import sys


def main():
    print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__, __name__, str(__package__)))

    from src.ioproject.graph_sketcher import DrawGraph

    directory = "./"
    if len(sys.argv) > 1:
        directory = sys.argv[1]

    # Creating drawer class which contains methods used below in the dynamic menu
    graphSketcher = DrawGraph(directory)

    # menu
    exit_condition = '0'
    choice = '0'
    while exit_condition == '0':
        print('\033[2J')  # Clear screen
        print("___________________________________________________________")
        print("\t     Dynamic menu for graph drawing")
        print("___________________________________________________________\n")

        print("Chosen directory: " + directory + "\n")

        # 1
        print("[1]:\tDraw\t", end="")
        print("\033[1;32;33mFILE" + '\033[0m', end="")
        print("\t\t\t\t\trelationship diagram")
        # 2
        print("[2]:\tDraw\t", end="")
        print("\033[1;32;96mMETHOD" + '\033[0m', end="")
        print("\t\t\t\t\trelationship diagram")
        # 3
        print("[3]:\tDraw\t", end="")
        print("\033[1;35;35mMODULE" + '\033[0m', end="")
        print("\t\t\t\t\trelationship diagram")
        # 4
        print("[4]:\tDraw\t", end="")
        print("\033[1;32;33mFILE" + '\033[0m', end=" ")
        print("+ " + "\033[1;32;96mMETHOD" + '\033[0m', end="")
        print("\t\t\trelationship diagram")
        # 5
        print("[5]:\tDraw\t", end="")
        print("\033[1;32;33mFILE" + '\033[0m', end=" ")
        print("+ " + "\033[1;32;35mMODULE" + '\033[0m', end="")
        print("\t\t\trelationship diagram")
        # 6
        print("[6]:\tDraw\t", end="")
        print("\033[1;32;96mMETHOD" + '\033[0m', end=" ")
        print("+ " + "\033[1;32;35mMODULE" + '\033[0m', end="")
        print("\t\t\trelationship diagram")
        # 7
        print("[7]:\tDraw\t", end="")
        print("\033[1;32;33mFILE" + '\033[0m', end=" ")
        print("+ " + "\033[1;32;96mMETHOD" + '\033[0m', end=" ")
        print("+ " + "\033[1;32;35mMODULE" + '\033[0m', end="")
        print("\trelationship diagram")
        # 8
        print("[8]:\tDraw\t", end="")
        print("\033[1;32;33mFILE" + '\033[0m', end=" ")
        print("+ " + "\033[1;32;97mFUNCTION" + '\033[0m', end=" ")
        print("\t\trelationship diagram")
        # Exit
        print("\nType q to exit the program")

        choice = input("\n:")

        if choice == "1":
            graphSketcher.draw_file_graph()
            print("\nGraph generated")
            input("Press enter to continue...")
        elif choice == "2":
            graphSketcher.draw_method_graph()
            print("\nGraph generated")
            input("Press enter to continue...")
        elif choice == "3":
            graphSketcher.draw_module_graph()
            print("\nGraph generated")
            input("Press enter to continue...")
        elif choice == "4":
            #graphSketcher.draw_file_method_graph()
            print("\nNot implemented")
            input("Press enter to continue...")
        elif choice == "5":
            graphSketcher.draw_file_module_graph()
            print("\nGraph generated")
            input("Press enter to continue...")
        elif choice == "6":
            #graphSketcher.draw_method_module_graph()
            print("\nNot implemented")
            input("Press enter to continue...")
        elif choice == "7":
            #graphSketcher.draw_file_method_module_graph()
            print("\nNot implemented")
            input("Press enter to continue...")
        elif choice == "8":
            graphSketcher.draw_file_method_graph_direct()
            print("\nGraph generated")
            input("Press enter to continue...")
        elif choice == "q":
            exit(0)
        else:
            input("\nWrong input.\nPress enter to continue...")


if __name__ == "__main__":
    main()
