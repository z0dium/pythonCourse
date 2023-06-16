# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
#
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
import os

def loadDirectory():
    os.system('cls')
    with open("Directory/DirectoryBase.txt","r",encoding="utf-8") as f:
        temp = f.read().splitlines()
        for i in range(len(temp)):
            temp[i] = F"{i}, " + temp[i]   # добавляю индекс контакта для дальнейших операций с ним
        return temp
    
def printAll():
    os.system('cls')
    for record in directory:
        printDirectoryElement(record)
    menu()

def printDirectoryElement(element):
    for part in element.split(","):     
        print(F"{part.strip()}\t\t",end="")
    print()

def addNewContact(surname,name,patronymic,phoneNumber):
    directory.append(F"{surname},{name},{patronymic},{phoneNumber}")
    persistDirectory()
    printAll()

def persistDirectory():
    print()
    with open("Directory/DirectoryBase.txt","w",encoding="utf-8") as f:
        for element in directory:
            f.write(element[element.index(",")+2:]+"\n")

def findContact(filter):
    os.system('cls')
    counter = 0
    for element in directory:
        if (filter in element):
            printDirectoryElement(element)
            counter += 1
    if counter == 0:
        print("Совпадений не найдено")    
    menu()

def editContact():
    id = input("Введите id записи для редактирования (первый стоолбец): ")
    for i in range(len(directory)):
        if directory[i][:directory[i].index(",")] == (id):
            directory[i] = F"{id}, " + input("Введите {Фаимилию, Имя, Отчество, Номер телефона} контакта: ")
            persistDirectory()
            break
    menu()

def deleteContact():
    id = input("Введите id записи для удаления (первый стоолбец): ")
    index = -1
    for i in range(len(directory)):
        if directory[i][:directory[i].index(",")] == (id):
            index = i
            break
    if index != -1:
        del directory[index]
    else:
        print(F"Записи с индексом {id} нет в справочнике")
    persistDirectory()    
    menu()         


def menu():
    print()
    print("1 - Показать все контакты, 2 - Найти контакт, 3 - Редактировать контакт, 4 - Удалить контакт, 5 - Выйти из справочника")
    print()
    option = 0
    while option < 1 or option > 5:
        option = int(input("Введите вариант действия (от 1 до 5): "))
        if option == 1:
            printAll()    
        if option == 2:
            findContact(input("Введите строку для поиска: "))
        if option == 3:
            editContact()
        if option == 4:
            deleteContact()
        if option == 5:
            return    
directory = loadDirectory()
menu()







          




