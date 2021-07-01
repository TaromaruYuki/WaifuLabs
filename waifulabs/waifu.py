import base64
import pathlib

from .exception import *
from .func import *

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
            p = file.split("/")
            del p[-1]
            pathlib.Path("/".join(p)).mkdir(parents=True, exist_ok=True)

        with open(file, "wb") as f:
            f.write(self.bytes)

    def GenerateBigWaifu(self) -> "Waifu":
        """
            Generate a big waifu based on the current waifu
        """
        if not isvalidseed(self.seeds):
            raise WaifuInvalidSeed("No valid 'Waifu' or 'Seeds' provided")
        
        bigwaifu = valid_response(fetch("generate_big", {"currentGirl": self.seeds}))

        return Waifu(base64=bigwaifu['girl'], seeds=self.seeds, big=True)

    def GenerateProduct(self, product: str) -> "Waifu":
        """
            Generate a product based on the current waifu
        """
        if not isvalidseed(self.seeds):
            raise WaifuInvalidSeed("No valid 'Waifu' or 'Seeds' provided")

        if product != PILLOW or product != POSTER:
            raise WaifuInvalidProduct(f"Got {product}, not waifulabs.PILLOW, or waifulabs.POSTER")

        waifuproduct = valid_response(fetch("generate_preview", {
            "currentGirl": self.seeds,
            "product": product
        }))

        return Waifu(base64=waifuproduct['girl'], seeds=self.seeds, product=True, product_type=product)

class AsyncWaifu(Waifu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def GenerateBigWaifu(self) -> "AsyncWaifu":
        """
            Generate a big waifu based on the current waifu
        """
        if not isvalidseed(self.seeds):
            raise WaifuInvalidSeed("No valid 'Waifu' or 'Seeds' provided")
        
        resp = await fetch("generate_big", {"currentGirl": self.seeds})
        
        bigwaifu = await valid_async_response(resp)

        return AsyncWaifu(base64=bigwaifu['girl'], seeds=self.seeds, big=True)

    async def GenerateProduct(self, product: str) -> "AsyncWaifu":
        """
            Generate a product based on the current waifu
        """
        if not isvalidseed(self.seeds):
            raise WaifuInvalidSeed("No valid 'Waifu' or 'Seeds' provided")

        if product != PILLOW or product != POSTER:
            raise WaifuInvalidProduct(f"Got {product}, not waifulabs.PILLOW, or waifulabs.POSTER")

        resp = await fetch_async("generate_preview", {
            "currentGirl": self.seeds,
            "product": product
        })

        waifuproduct = await valid_response(resp)

        return AsyncWaifu(base64=waifuproduct['girl'], seeds=self.seeds, product=True, product_type=product)