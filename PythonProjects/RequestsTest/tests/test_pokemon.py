import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers_status_200():
    """
    KTT-1. Get trainers status 200
    """

    response = requests.get(url=f'{URL}/trainers', timeout=5)  
    assert response.status_code == 200, 'Unexpencted status code'


def test_get_trainers_by_id_4723():
    """
    KTT-2. Get trainers by id
    """

    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 4723}, timeout=5)  
    assert response.status_code == 200, 'Unexpencted status code'
    assert response.json()['trainer_name'] == 'lexa1988' ''



