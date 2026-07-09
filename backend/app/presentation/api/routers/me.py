from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter

from app.application.dtos.user import UserOut, UserUpdateInput
from app.application.use_cases.auth.get_profile import GetProfileUseCase
from app.application.use_cases.auth.update_profile import UpdateProfileUseCase
from app.presentation.api.deps import CurrentUser

router = APIRouter(prefix="/me", tags=["me"])


@router.get("", response_model=UserOut)
@inject
async def get_my_profile(
    user: CurrentUser,
    use_case: FromDishka[GetProfileUseCase],
):
    """Retrieves the profile of the currently logged-in user."""
    user_entity = await use_case.execute(user.id)
    return UserOut.model_validate(user_entity)


@router.put("", response_model=UserOut)
@inject
async def update_my_profile(
    user: CurrentUser,
    payload: UserUpdateInput,
    use_case: FromDishka[UpdateProfileUseCase],
):
    """Updates the profile details of the currently logged-in user."""
    user_entity = await use_case.execute(user.id, payload)
    return UserOut.model_validate(user_entity)
