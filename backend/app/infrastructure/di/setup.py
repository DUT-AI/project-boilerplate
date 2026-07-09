from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka

from app.infrastructure.di.database import DatabaseProvider
from app.infrastructure.di.repositories import RepositoryProvider
from app.infrastructure.di.clients import ClientProvider
from app.infrastructure.di.use_cases import UseCaseProvider


def setup_di(app):
    """Sets up Dishka dependency injection container and binds it to the FastAPI app."""
    container = make_async_container(
        DatabaseProvider(),
        RepositoryProvider(),
        ClientProvider(),
        UseCaseProvider(),
    )

    app.state.dishka_container = container
    setup_dishka(container, app)
