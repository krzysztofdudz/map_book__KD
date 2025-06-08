

users:list=[
    {'name':'Maciej','location':'Lódź','posts':100},
    {'name':'Mateusz','location':'Poznań','posts':200},
    {'name':'Maciej01','location':'Siedlce','posts':300},
    {'name':'Konrad','location':'Grudziądz','posts':400},
]


def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowosci {user['location']} opublikował {user["posts"]} postów. ')

get_user_info(users)