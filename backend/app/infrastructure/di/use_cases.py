from dishka import Provider, Scope, provide

from app.application.use_cases.auth.register import RegisterUseCase
from app.application.use_cases.auth.login import LoginUseCase
from app.application.use_cases.auth.get_profile import GetProfileUseCase
from app.application.use_cases.auth.update_profile import UpdateProfileUseCase
from app.application.use_cases.uploads.upload_file import UploadFileUseCase
from app.application.use_cases.uploads.presign_upload import PresignUploadUseCase


class UseCaseProvider(Provider):
    """Provider for application use cases."""

    scope = Scope.REQUEST

    register_uc = provide(RegisterUseCase)
    login_uc = provide(LoginUseCase)
    get_profile_uc = provide(GetProfileUseCase)
    update_profile_uc = provide(UpdateProfileUseCase)
    upload_file_uc = provide(UploadFileUseCase)
    presign_upload_uc = provide(PresignUploadUseCase)
