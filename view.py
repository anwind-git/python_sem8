from os import system, name
import model_new_user
import all_list
import search
import dell
import edit
import json

def Сlear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def Team():
    team = str(input('Введите команду: '))
    return team
        
def Menu():
    Сlear()
    print('ОСНОВНОЕ МЕНЮ:------------------------------------------------------------------------')
    print('Список команд: Сотрудники: S | Выход: exit')
    print('--------------------------------------------------------------------------------------')

def Search():
    team = 0
    while team != 'A':
        Сlear()
        print('СОТРУДНИКИ:---------------------------------------------------------------------------')
        print('Все: S | Добавить: + | Поиск: * | Удалить: - | Редактировать: R | Меню: A')
        print('--------------------------------------------------------------------------------------')
        all_list.OpenList()
        if team == '*':
            Сlear()
            search.SearchList()
        if team == '-':
            Сlear()
            dell.Dell()
        if team == '+':
            Сlear()
            model_new_user.NewEntry()
        if team == 'R':
            Сlear()
            edit.Edit()
        if team == 'J':
            Сlear()
            json.JSON(team)
        print('--------------------------------------------------------------------------------------')
        team = Team()