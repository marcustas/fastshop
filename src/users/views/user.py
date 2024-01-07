from typing import (
    Annotated,
    Union,
    List,
)

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from src.users.models.pydantic import(
    UserAddressDetailModel,
    UserAddressModel,
)

from src.users.routes import (
    UserManagementRoutesPrefixes,
    UserRoutesPrefixes,
    UserAddressRoutesPrefixes,
)
from src.users.services import get_user_address_service
from src.authentication.utils import get_current_user
from src.common.schemas.common import ErrorResponse


router = APIRouter(prefix=UserManagementRoutesPrefixes.user_address)

@router.get(
    ProductRoutesPrefixes.root,
    status_code=status.HTTP_200_OK,
    response_model=list[UserAddressModel],
)
async def user_address_list(
        current_user: Annotated[UserAddressModel, Depends(get_current_user)],
        user_address_service=Depends(get_user_address_service)) -> List[UserAddressModel]:
    return await user_address_service.get_user_addresses(user_id=current_user.id)


@router.get(
    UserAddressRoutesPrefixes.detail,
    responses={
        status.HTTP_200_OK: {'model': UserAddressDetailModel},
        status.HTTP_404_NOT_FOUND: {'model': ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
    response_model=Union[UserAddressDetailModel, ErrorResponse],
)
async def user_address_detail(
    response: Response,
    pk: int,

    current_user: Annotated[UserAddressDetailModel, Depends(get_current_user)],
    user_address_service=Depends(get_user_address_service)
) -> Union[UserAddressDetailModel, ErrorResponse, Response]:
    result = await user_address_service.get_address_detail(address_id=pk, user_id=current_user.id)

    if result is None:
        response.status_code = status.HTTP_403_FORBIDDEN
        return ErrorResponse(message='Sorry, it is not your address!')
    return result