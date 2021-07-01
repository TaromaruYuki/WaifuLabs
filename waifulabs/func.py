import requests
import aiohttp
import json
from .exception import WaifuInvalidResponse

baseURL = "https://api.waifulabs.com/"

session = requests.session()
aio_session = aiohttp.ClientSession(headers={"Content-Type": "application/json"})

PILLOW = "PILLOW"
POSTER = "POSTER"

_non_200_err = "Got a non 200 HTTP code. Received {}."

def fetch(endpoint, data):
    return session.post(baseURL + endpoint, json=data, headers={
        "Content-Type": "application/json"
    })

async def fetch_async(endpoint, data):
    r = await aio_session.post(baseURL + endpoint, json=data)

    return r

def valid_response(response: requests.Response):
    if response.status_code != 200:
        raise WaifuInvalidResponse(_non_200_err.format(response.status_code))

    return response.json()

async def valid_async_response(response: aiohttp.ClientResponse):
    if response.status != 200:
        raise WaifuInvalidResponse(_non_200_err.format(response.status))

    t = await response.text()

    return json.loads(t)

def isvalidseed(seeds: list):
    if len(seeds) < 17: return False
    for seed in seeds[0:16]:
        if type(seed) != int:
            return False

    return True