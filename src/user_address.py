    from typing import (
        Annotated,
        Union,
        List
    )

    from fastapi import (
        APIRouter,
        Depends,
        Response,
        status,
    )

    from src.catalogue.models.pydantic import ProductModel
    from src.catalogue.routes import (
        CatalogueRoutesPrefixes,
        ProductRoutesPrefixes,
    )
from src.users.routes import (
    UserManagementRoutesPrefixes,
    UserAddressRoutesPrefixes,
    UserRoutesPrefixes,
)
from src.catalogue.services import get_product_service
from src.common.exceptions.base import ObjectDoesNotExistException
from src.common.schemas.common import ErrorResponse
from src.users.services import get_user_address_service
from src.users.models.sqlalchemy import UserAddress

from src.authentication.utils import get_current_user

router = APIRouter(prefix=CatalogueRoutesPrefixes.product)
router = APIRouter(prefix=UserManagementRoutesPrefixes.user_address)

@router.get(
        ProductRoutesPrefixes.root,
        status_code=status.HTTP_200_OK,
        response_model=list[ProductModel],
    )
    async def product_list(product_service: Annotated[get_product_service, Depends()]) -> list[ProductModel]:
        """
        Get list of products.

        Returns:
            Response with list of products.
        """
        return await product_service.list()


@router.get(
    ProductRoutesPrefixes.detail,
    responses={
        status.HTTP_200_OK: {'model': ProductModel},
        status.HTTP_404_NOT_FOUND: {'model': ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
    response_model=Union[ProductModel, ErrorResponse],
)
async def product_detail(
        response: Response,
        pk: int,
        service: Annotated[get_product_service, Depends()],
) -> Union[Response, ErrorResponse]:
    """
    Retrieve product.

    Returns:
        Response with product details.
    """
    try:
        response = await service.detail(pk=pk)
    except ObjectDoesNotExistException as exc:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ErrorResponse(message=exc.message)

    return response

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
            List of user addresses.
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
        User address details.
    """
    result = await user_address_service.get_user_address_by_id(address_id=pk, user_id=current_user.id)
    if result is None:
        response.status_code = status.HTTP_403_FORBIDDEN
        return ErrorResponse(message='Wrong address!')
    return result