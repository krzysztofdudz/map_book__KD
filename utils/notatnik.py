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