from typing import (
    Annotated,
    List,
    Union,
)

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from src.authentication.utils import get_current_user
from src.common.schemas.common import ErrorResponse
from src.users.models.database import (
    UserAddress,
)
from src.users.routes import (
    UserAddressRoutesPrefixes,
    UserManagementRoutesPrefixes,
    UserRoutesPrefixes,
)
from src.users.services import get_user_address_service


router = APIRouter(prefix=UserManagementRoutesPrefixes.user_address)


@router.get(
    UserRoutesPrefixes.root,
    status_code=status.HTTP_200_OK,
    response_model=list[UserAddress],
)
async def user_address_list(
        current_user: Annotated[UserAddress, Depends(get_current_user)],
        user_address_service=Depends(get_user_address_service)) -> List[UserAddress]:
    """
        Get list of user addresses.

        Returns:
            Response with list of user addresses.
        """
    return await user_address_service.get_user_addresses(user_id=current_user.id)


@router.get(
    UserAddressRoutesPrefixes.detail,
    responses={
        status.HTTP_200_OK: {'model': UserAddress},
        status.HTTP_404_NOT_FOUND: {'model': ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
    response_model=Union[UserAddress, ErrorResponse],
)
async def user_address_detail(
    response: Response,
    pk: int,
        current_user: Annotated[UserAddress, Depends(get_current_user)],
        user_address_service=Depends(get_user_address_service),
) -> Union[UserAddress, ErrorResponse, Response]:
    """
    Retrieve user address.

    Returns:
        Response with user address details.
    """
    result = await user_address_service.get_user_address_by_id(address_id=pk, user_id=current_user.id)

    if result is None:
        response.status_code = status.HTTP_403_FORBIDDEN
        return ErrorResponse(message='This is not your address!')

    return result
