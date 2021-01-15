#Thanks Dankcoder (Discord: DankCoder#9983) for the code!
#Modified by Doggo (Discord: Doggo#4340)

import requests
import base64
import pathlib
from typing import List
from .exception import *

_baseURL = "https://api.waifulabs.com/"
_session = requests.session()
PILLOW = "PILLOW"
POSTER = "POSTER"

def _fetch(endpoint, data):
    return _session.post(_baseURL + endpoint, json=data, headers={
        "Content-Type": "application/json"
    })

def _valid_response(response: requests.Response):
    if response.status_code != 200:
        raise WaifuInvalidResponse("Got a non 200 HTTP code. Recieved {response.status_code}.")

    return response.json()

def _isvalidseed(seeds: list):
    if len(seeds) < 17: return False
    for seed in seeds[0:16]:
        if type(seed) != int:
            return False

    return True

class Waifu:
    """
        Represents a Waifulabs Waifu
        
        `base64`: str -> Base64 image of the waifu

        `seeds`: list -> The waifu's seeds

        `big`: bool -> See if the waifu is of type `big`

        `product`: bool -> See if the waifu is of type `product`

        `product_type`: str -> If waifu is product, see product type
    """
    def __init__(self, **kwargs):
        self.base64 = ""
        self.seeds = []
        self.big = False
        self.product = False
        self.product_type = False
        if "base64" in kwargs:
            if not type(kwargs['base64']) == str:
                raise TypeError(f"Argument 'base64' was type {type(kwargs['base64'])}, but expected {str}")

            self.base64 = kwargs['base64']
            self.bytes = base64.decodebytes(kwargs["base64"].encode())
        else:
            raise WaifuMissingArg("Arg 'base64' is missing!")

        if "seeds" in kwargs:
            if not type(kwargs['seeds']) == list:
                raise TypeError(f"Argument 'seeds' was type {type(kwargs['seeds'])}, but expected {list}")

            self.seeds = kwargs['seeds']
        else:
            raise WaifuMissingArg("Arg 'seeds' is missing!")

        if "big" in kwargs:
            if not type(kwargs['big']) == bool:
                raise TypeError(f"Argument 'big' was type {type(kwargs['big'])}, but expected {bool}")

            self.big = kwargs['big']

        if "product" in kwargs:
            if not type(kwargs['product']) == bool:
                raise TypeError(f"Argument 'product' was type {type(kwargs['product'])}, but expected {bool}")

            self.product = kwargs['product']

            if not "product_type" in kwargs:
                raise WaifuMissingArg("Arg 'product_type' is required when arg 'product' is set.")

            if not type(kwargs['product_type']) == str:
                raise TypeError(f"Argument 'product_type' was type {type(kwargs['product_type'])}, but expected {str}")

            self.product_type = kwargs['product_type']

    def _exists(self, file: str):
        return pathlib.Path(file).exists()
    
    def save(self, file: str) -> None:
        """
            Save a image of the current waifu.

            `file`: Filename. Directories allowed.
        """
        if not self._exists(file):
            _p = file.split("/")
            del _p[-1]
            pathlib.Path("/".join(_p)).mkdir(parents=True, exist_ok=True)

        with open(file, "wb") as f:
            f.write(self.bytes)

    def GenerateBigWaifu(self):
        """
            Generate a big waifu based on the current waifu
        """
        if not _isvalidseed(self.seeds):
            raise WaifuInvalidSeed("No valid 'Waifu' or 'Seeds' provided")
        
        _bigwaifu = _valid_response(_fetch("generate_big", {"currentGirl": self.seeds}))

        return Waifu(base64=_bigwaifu['girl'], seeds=self.seeds, big=True)

    def GenerateProduct(self, product: str):
        """
            Generate a product based on the current waifu
        """
        if not _isvalidseed(self.seeds):
            raise WaifuInvalidSeed("No valid 'Waifu' or 'Seeds' provided")

            if product != WaifuProduct.PILLOW or WaifuProduct.POSTER:
                raise WaifuInvalidProduct(f"Got {product}, not waifulabs.PILLOW, or waifulabs.POSTER")

        _waifuproduct = _valid_response(("generate_preview", {
            "currentGirl": self.seeds,
            "product": product
        }))

        return Waifu(base64=_waifuproduct['girl'], seeds=self.seeds, product=True, product_type=product)

def GenerateWaifu(seeds: list=None, step=0) -> Waifu:
    """
        Generate a waifu.

        `seeds`: Generate a waifu based on a waifu seed
    """
    waifuobject = {}
    waifuobject['step'] = max(0, min(3, step))
    
    if waifuobject['step'] > 0:
        waifuobject['currentGirl'] = seeds
        if not _isvalidseed(waifuobject['currentGirl']):
            raise WaifuInvalidSeed("No valid 'Waifu' or 'Seeds' provided")

    response = _valid_response(_fetch("generate", waifuobject))
    
    try:
        if "newGirls" not in response:
            raise WaifuInvalidResponse(f"Expected 'newGirls', got {response}.")
    except Exception as e:
        raise WaifuInvalidResponse(e)

    _waifu = response['newGirls'][0]

    return Waifu(base64=_waifu['image'], seeds=_waifu['seeds'])

def GenerateWaifus(seeds: list=None, step=0) -> List[Waifu]:
    """
        Generate 16 waifus

        `seeds`: Generate a waifu based on a waifu seed
    """
    waifuobject = {}
    _waifus = []
    waifuobject['step'] = max(0, min(3, step))
    
    if waifuobject['step'] > 0: #seeds != None: 
        waifuobject['currentGirl'] = seeds
        if not _isvalidseed(waifuobject['currentGirl']):
            raise WaifuInvalidSeed("No valid 'Waifu' or 'Seeds' provided")
    
    response = _valid_response(_fetch("generate", waifuobject))

    try:
        if "newGirls" not in response:
            raise WaifuInvalidResponse(f"Expected 'newGirls', got {response}.")
    except Exception as e:
        raise WaifuInvalidResponse(e)

    _generatedWaifus = response['newGirls']
    
    for x in _generatedWaifus:
        _waifus.append(Waifu(base64=x['image'], seeds=x['seeds']))

    return _waifus
