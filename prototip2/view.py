class ViewConsole:

    
    def viewShowMenu(self):
        print("1. Login")
        print("2. Exit")
        while True: 
            option = input("Select an option: ")
            if(option.isdigit()):
                optionInt = int(option)
                if optionInt in [1, 2]:
                    return optionInt
            print("Invalid option. Please select 1 or 2.")
                
    def viewGeneral(self):
        option = -1
        while option != 2:
            option = self.viewShowMenu()
            match option:
                case 1:
                    # login
                    print("---Login---")
                
                case 2:
                    #exit
                    print("Exiting the application. Goodbye!")