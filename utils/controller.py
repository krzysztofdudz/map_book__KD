def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowosci {user['location']} opublikował {user["posts"]} postów. ')
def add_user(users_data:list)->None:
    new_name:str=input('podaj imię nowego znajomego: ')
    new_location:str=input('podaj lokalizację: ')
    new_posts: str = input('podaj liczbę postów: ')
    users_data.append({'name':new_name,'location':new_location,'posts':new_posts})

def remove_user(users_data:list)->None:
    user_name: str = input('podaj imię znajomego do usunięcia: ')
    for user in users_data:
        if user['name'] == user_name:
            users_data.remove(user)

def update_user(users_data:list)->None:
    user_name: str = input('podaj imię użytkownika do aktualizacji: ')
    for user in users_data:
        if user['name'] == user_name:
            user['name']=input('podaj nowe imię użytkownika: ')
            user['location']=input('podaj nową lokalizację użytkownika: ')
            user['posts'] =input('podaj liczbę postów:')


def get_coordinates(city: str) -> list:
    import requests
    from bs4 import BeautifulSoup

    url = f'https://pl.wikipedia.org/wiki/{city}'
    response = requests.get(url).text
    response_html = BeautifulSoup(response, 'html.parser')
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    return [latitude, longitude]

def get_map(users_data:list)->None:
    import folium
    map = folium.Map(location=(52.23, 21.00), zoom_start=6)
    for user in users_data:
        coordinates = get_coordinates(user['location'])

        folium.Marker(
            location=(coordinates[0], coordinates[1]),
            popup=f"Twój znajomy {user['name']}, <br/> miejscowość: {user['location']} <br/> opublikował {user['posts']} postów").add_to(
            map)
    map.save('mapa.html')