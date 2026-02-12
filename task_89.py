import json
import requests
from typing import Callable,Any,Optional,Dict,List



def give_date(name:str,file: dict)->Optional[dict]:
    falcone : Optional[dict]  = None
    for i in file['results']:
        if i['name'] == name:
           falcone = i
    return falcone

def give_pilots(method : dict)->list[dict]:
    pilots_list: list = []
    for i in method['pilots']:
        pilots_info  = requests.get(i).json()
        pilots_planet = requests.get(pilots_info['homeworld']).json()
        pilots_list.append({
        "имя": pilots_info['name'],
        "рост": pilots_info['height'],
        "вес": pilots_info['mass'],
        "родная планета": pilots_planet['name'],
        "ссылка на информацию о родной планете": pilots_planet['url']
    })
    return pilots_list

def finish_list(ship: dict,name_info : list)->dict:
    ship_info = {
    "название": ship['name'],
    "максимальная скорость": ship['max_atmosphering_speed'],
    "класс": ship['starship_class'],
    "список пилотов": name_info}
    return ship_info


new1 = requests.get('https://swapi.dev/api/starships/')
my_ship = new1.json()
search_name = 'Millennium Falcon'
method = give_date(name=search_name,file=my_ship)
if method:
    pilots = give_pilots(method)
    result = finish_list(ship = method,name_info = pilots)
    finish = json.dumps(result,indent=4,ensure_ascii=False)
    print(finish)
else:
    print('Корабл Millenium Falcon не найден!')


