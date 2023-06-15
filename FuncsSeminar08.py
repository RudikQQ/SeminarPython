import os                                         #Очистка os.system ('CLS')

def show_contacts(file_name):      #Открыть файл, демонстрация
    os.system('CLS')                                 
    with open(file_name,'r') as file:
        data = file.readlines()

        for contacts in data:
            print(contacts, end='')
    input('\npress any key')        

def add_contact(file_name):                          #Добавить информацию в файл TXT демонстрация     
    os.system('CLS')                             
    with open(file_name, "a") as file:
        res = ''
        res += input('Input a surname of contact: ') + ' '
        res += input('Input a name of contact: ') + ' '
        res += input('Input a phone number of contact: ')

        file.write('\n' + res) 

    input('Contact was successfully added! Press any key for return')

def search_contact(file_name):                                       #Поиск контакта
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

def drawing():                                  #Интерфейс
    print('1 - show contacts')
    print("2 - add contact")
    print('3 - search contact')
    print('4 - exit ')

def main(file_name):                               #Основа
    while True:
        os.system('CLS')
        drawing()        
        user_choice = int(input("Input a number from 1 to 4: "))

        if user_choice == 1 :
            show_contacts(file_name)
        elif user_choice == 2 :
            add_contact(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4:
            print('Have a nice day!')
            return
        
main('test.txt')

