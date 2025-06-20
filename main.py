from utils.model import users
from utils.controller import get_user_info, add_user, remove_user, update_user, get_map


def main():

    while True:
        print('==========MENU==========')
        print('0 - zakończ program')
        print('1 - wyswietl co u znajomych')
        print('2 - dodaj znajomego')
        print('3 - usuń znajomego')
        print('4 - zaktualizuj dane znajomego')
        print("5 - Przygotuj mapę znajomych")
        print('========================')
        choice = input('wybierz opcje MENU: ')
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)
        if choice == '3': remove_user(users)
        if choice == '4': update_user(users)
        if choice == '5': get_map(users)



if __name__ == '__main__':
    main()