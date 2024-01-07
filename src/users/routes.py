from src.common.routes import BaseCrudPrefixes


class UserManagementRoutesPrefixes:
    user: str = '/user'
    user_address: list = '/user_address'

class UserRoutesPrefixes(BaseCrudPrefixes):
    ...


class UserAddressRoutesPrefixes(BaseCrudPrefixes):
    ...
