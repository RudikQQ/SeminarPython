import os                                                                                   #Очистка os.system ('CLS')

def show_contacts(file_name):                                                               #Открыть файл, демонстрация
    os.system('CLS')                                 
    with open(file_name,'r') as file:
        data = file.readlines()

        for contacts in data:
            print(contacts, end='')
    input('\npress any key')        

def add_contact(file_name):                                                                 #Добавить информацию в файл TXT демонстрация     
    os.system('CLS')                             
    with open(file_name, "a") as file:
        res = ''
        res += input('Input a surname of contact: ') + ' '
        res += input('Input a name of contact: ') + ' '
        res += input('Input a phone number of contact: ')

        file.write('\n' + res) 

    input('Contact was successfully added! Press any key for return')

def search_contact(file_name):                                                              #Поиск контакта
    os.system('CLS')
    target = input('Input a name of contact for searhing: ')
    
    with open (file_name, 'r') as file:
        contacts = file.readlines()

        for contact in contacts:
                if target in contact:
                    print(contact)
                    break
        else:
            print('there is no contacts with whis name.')  
    input('\npress any key')

def drawing():                                                                              #Интерфейс
    print('1 - show contacts')
    print("2 - add contact")
    print('3 - search contact')
    print('4 - change contact information')
    print('5 - delete contact information')
    print('6 - exit ')

def edit_data(filename):                                                                    # Изменяет информацию из файла
    print("\n Full name | Phone number")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Enter the line number to edit: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    fio = input("Enter your full name: ")
    phone = input("Enter your phone number: ")
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f" {fio} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Record  - {edit_tel_book_lines}, changed to - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))


def delete_data(filename):                                                                  # Удаляет информацию из файла
    print("\n Full name | Phone number")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Enter the line number to delete: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Record deleted: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))   

def main(file_name):                                                                        # Основа
    while True:
        os.system('CLS')
        drawing()        
        user_choice = int(input("Input a number from 1 to 6: "))

        if user_choice == 1 :
            show_contacts(file_name)
        elif user_choice == 2 :
            add_contact(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4 :
            edit_data(file_name)
        elif user_choice == 5 :
            delete_data(file_name)
        elif user_choice == 6:
            print('Have a nice day!')
            return
        


