from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, File, UploadFile

from app.application.dtos.user import UploadPresignInput, UploadOut
from app.application.use_cases.uploads.presign_upload import PresignUploadUseCase
from app.application.use_cases.uploads.upload_file import UploadFileUseCase
from app.presentation.api.deps import CurrentUser

router = APIRouter(prefix="/uploads", tags=["uploads"])


@router.post("/presign", response_model=UploadOut)
@inject
async def presign_upload(
    body: UploadPresignInput,
    user: CurrentUser,
    use_case: FromDishka[PresignUploadUseCase],
):
    """Generates a presigned PUT URL for uploading file directly from client to S3."""
    return await use_case.execute(body.key, body.content_type)


@router.post("/file", response_model=UploadOut)
@inject
async def upload_file(
    user: CurrentUser,
    use_case: FromDishka[UploadFileUseCase],
    file: UploadFile = File(...),
):
    """Uploads a file directly to the S3 bucket through the FastAPI server."""
    content = await file.read()
    return await use_case.execute(
        file_content=content,
        filename=file.filename or "upload.bin",
        content_type=file.content_type or "application/octet-stream",
    )
