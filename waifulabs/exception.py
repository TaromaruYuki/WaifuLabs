class WaifuException(Exception):
    """Base exception class"""
    pass

class WaifuInvalidResponse(WaifuException):
    """Thrown when something invalid was recieved and doesn't have a error for it"""
    pass

class WaifuInvalidSeed(WaifuException):
    """Thrown when a invalid seed(s) was given"""
    pass

class WaifuInvalidProduct(WaifuException):
    """Thrown when a invalid product was given"""
    pass

class WaifuMissingArg(WaifuException):
    """Thrown when a argument is missing"""
    pass