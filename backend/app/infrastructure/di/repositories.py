from dishka import Provider, Scope, provide

from app.domain.interfaces.user_repo import IUserRepository
from app.infrastructure.repositories.users import UserRepository


class RepositoryProvider(Provider):
    """Provider for DB repositories."""

    scope = Scope.REQUEST

    user_repo = provide(UserRepository, provides=IUserRepository)
