#-*- coding:utf-8 -*-
import os
import sys
import time

from beautifultable import BeautifulTable

from model.database import create_connection
from model.contact_dao import ContactDAO
from model.contact_model import Contact
from model.csv_handler import export_to_csv

__author__ = "Felipe Henrique"

def create_contact():
    with create_connection() as conn:
        dao = ContactDAO(conn)
        name = input("Type the name: ")
        email = input("Type the email: ")
        date = input("Type de Date: (yyyy-DD-MM)")
        dao.create(Contact(name, email, date))


def list_contacts():
    with create_connection() as conn:
        dao = ContactDAO(conn)
        contacts = dao.read()
        print("============================")
        for item in contacts:
            print(item)
        print("----------------------------")


def find_contact():
    with create_connection() as conn:
        dao = ContactDAO(conn)
        code = int(input("Type the code"))
        search = dao.find_by_id(code)
        if search:
            print(search)
        else:
            print('The contact is not included')


def update_contact():
    with create_connection() as conn:
        dao = ContactDAO(conn)
        name = input("Type the name: ")
        email = input("Type the email: ")
        date = input("Type de Date: (yyyy-DD-MM)")
        code = int(input("Type the code"))
        dao.update(Contact(name, email, date, code))


def remove_contact():
    with create_connection() as conn:
        dao = ContactDAO(conn)
        code = int(input("Digite the code"))
        contacts = dao.remove(code)


def clear():
    os.system("clear")

def exportar():
    with create_connection() as conn:
        dao = ContactDAO(conn)
        contacts = dao.read()
        export_to_csv(contacts)

def main():
    print("==================================================")
    print("                 Agenda   			     ")
    print("==================================================")
    print("   This program is writted by Felipe Henrique\n")
    time.sleep(1)
    print(" And helped by Cassio Botaro")
    input("\nPress Enter:")
    os.system('clear')
   
    os.system('clear')
    user_choice = 1
    while user_choice != 0:
        features = {
                    1: create_contact, 
                    2: list_contacts,
                    3: remove_contact,
                    4: find_contact,
                    5: update_contact,
                    6:exportar,
                    42: clear
        }
        print("Digite 1 para cadastrar contato")
        print("Digite 2 para listar contato")
        print("Digite 3 para remover contato")
        print("Digite 4 para buscar contato pelo id")
        print("Digite 5 para atualizar contato")
        print("Digite 6 para exportar contatos")
        print("Digite 42 para limpar a tela")
        print("Digite 0 para sair")
        try:
            user_choice = int(input("-%>:  "))
            features[user_choice]()
        except KeyError:
            sys.exit(1)

if __name__ == "__main__":
    main()
