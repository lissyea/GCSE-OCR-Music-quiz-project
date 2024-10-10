import pythonprojeccccc


while True:
        print("\nRegister or log in")
        print("1. Register")
        print("2. Log in")
        print("3. Exit")
        
        option1 = input("Pick your number: ")

        if option1 == '1':
            pythonprojeccccc.register()
            
        elif option1 == '2':
            name = pythonprojeccccc.authentification()
            scoring = pythonprojeccccc.songsquiz()

            print("")
            print("Thank you for playing!")
            print(f"Your score: {scoring}")
            print("")
            pythonprojeccccc.scoresystem(name, scoring)
            
        elif option1 == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Error: Invalid option.")


