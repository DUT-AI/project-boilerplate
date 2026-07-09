from dishka import Provider, Scope, provide

from app.domain.interfaces.s3_client import IS3Client
from app.infrastructure.clients.s3_client import S3Client


class ClientProvider(Provider):
    """Provider for external API clients and infrastructure utilities."""

    scope = Scope.APP

    s3_client = provide(S3Client, provides=IS3Client)
