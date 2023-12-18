from typing import (
    Annotated,
    Union, List,
)

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from src.authentication.utils import get_current_user
from src.common.exceptions.base import ObjectDoesNotExistException
from src.common.schemas.common import ErrorResponse
from src.users.models.pydantic import (
    UserAddressModel,
    UserAddressModelDetail,
)
from src.users.routes import (
    UserManagementRoutesPrefixes,
    UserRoutesPrefixes,
    UserAddressRoutesPrefixes,
)
from src.users.services import get_user_address_service

router = APIRouter(prefix=UserManagementRoutesPrefixes.user_address)


@router.get(
    UserRoutesPrefixes.root,
    status_code=status.HTTP_200_OK,
    response_model=list[UserAddressModel],
)
async def user_address_list(
        current_user: Annotated[UserAddressModel, Depends(get_current_user)],
        user_address_service=Depends(get_user_address_service)) -> List[UserAddressModel]:
    """
        Get list of user addresses.

        Returns:
            Response with list of user addresses.
        """
    return await user_address_service.get_user_addresses(user_id=current_user.id)


@router.get(
    UserAddressRoutesPrefixes.detail,
    responses={
        status.HTTP_200_OK: {'model': UserAddressModelDetail},
        status.HTTP_404_NOT_FOUND: {'model': ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
    response_model=Union[UserAddressModelDetail, ErrorResponse],
)
async def user_address_detail(
    response: Response,
    pk: int,
    current_user: Annotated[UserAddressModelDetail, Depends(get_current_user)],
    user_address_service=Depends(get_user_address_service)
) -> Union[UserAddressModelDetail, ErrorResponse, Response]:
    """
    Retrieve user address.

    Returns:
        Response with user address details.
    """
    result = await user_address_service.get_user_address_by_id(address_id=pk, user_id=current_user.id)

    # result возврашает None вечно, ошибку ObjectDoesNotExistException вызывать не хочет, потому решил так:
    if result is None:
        response.status_code = status.HTTP_403_FORBIDDEN
        return ErrorResponse(message='This address might not belong to you!')

    return result