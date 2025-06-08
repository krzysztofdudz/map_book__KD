import requests
from bs4 import BeautifulSoup


def get_coordinates(city: str) -> list:
    url = f'https://pl.wikipedia.org/wiki/{city}'
    response = requests.get(url).text
    response.html = BeautifulSoup(response, 'html.parser')
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    return [longitude, latitude]

def get_map(users_data: list) -> None:
    map = folium.Map(location=(52.23, 21.00), zoom_start=6)
    for user in users_data:
        coordinates = get_coordinates(user['location'])

        folium.Marker(
            location=coordinates[0], coordinates[1]),
            popup=f"Twój znajomy {user['name']}, br/> miejscowosc: {user['location']} opublikował {user['posts']} postów").add_to(map)

        map.save('mapa.html')

