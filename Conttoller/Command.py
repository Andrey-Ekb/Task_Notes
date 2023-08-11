import Model.Note
import Repositiry.LoadFromFile as lF
import Repositiry.WriteToFile as wF


def add_note():
    title = input("Введите заголовок заметки:\n")
    body = input("Введите описание заметки:\n")
    note = Model.Note.Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if Model.Note.Note.get_id(note) == Model.Note.Note.get_id(i):
            Model.Note.Note.set_id(note)
    array_notes.append(note)
    wF.write_file(array_notes, 'a')
    print("Заметка добавлена в журнал!")
    
def show(txt):
    array_notes = lF.read_file()

    if array_notes:
        if txt == "all":
            print("ЖУРНАЛ ЗАМЕТОК:")
            for i in array_notes:
                print(Model.Note.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", Model.Note.Note.get_id(i),Model.Note.Note.get_title(i))
            id = input("\nВведите id заметки: ")
            flag = True
            for i in array_notes:
                if id == Model.Note.Note.get_id(i):
                    print(Model.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такого ID")
                
        else:
            print("Журнал заметок пустой!")
            
def del_notes():
    id = input("Введите ID удаляемой заметки: ")
    array_notes = lF.read_file()
    flag = False

    for i in array_notes:
        if id == Model.Note.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        wF.write_file(array_notes, 'a')
        print("Заметка с id: ", id, " успешно удалена!")
    else:
        print("нет такого id")
        
def change_note():
    id = input("Введите ID изменяемой заметки: ")
    array_notes = lF.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Model.Note.Note.get_id(i):
            i.title = input("измените  заголовок:\n")
            i.body = input("измените  описание:\n")
            Model.Note.Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        wF.write_file(array_notes_new, 'a')
        print("Заметка с id: ", id, " успешно изменена!")
    else:
        print("нет такого id")