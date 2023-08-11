import Menu.UserMenu as team
import Conttoller.Command as com

print("Контроллер")

def start():

    while True:
        team.menu_console()
        user_input = input()
        
        if user_input == '1':
            com.show("all")
        elif user_input == '2':
            com.show("ID")            
        elif user_input == '3':
            com.show("all")
            com.change_note()     
        elif user_input == '4':
            com.add_note()    
        elif user_input == '5':
            com.show("all")    
            com.del_notes()        
        elif user_input == '6':
            print()
            print("                    журнал заметок закрыт")
            print()
            break