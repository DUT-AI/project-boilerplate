from app.application.dtos.user import UserLoginInput, TokenOut
from app.core.jwt import create_access_token
from app.core.security import verify_password
from app.domain.exceptions.exceptions import UnauthorizedException
from app.domain.interfaces.user_repo import IUserRepository


class LoginUseCase:
    def __init__(self, user_repo: IUserRepository) -> None:
        self._user_repo = user_repo

    async def execute(self, payload: UserLoginInput) -> TokenOut:
        # Get user
        user = await self._user_repo.get_by_email(payload.email)
        if not user:
            raise UnauthorizedException("Email hoặc mật khẩu không chính xác")

        # Verify password
        if not verify_password(payload.password, user.password_hash):
            raise UnauthorizedException("Email hoặc mật khẩu không chính xác")

        # Generate Token
        token_data = {"user_id": user.id, "role": user.role}
        access_token = create_access_token(token_data)

        return TokenOut(access_token=access_token)
