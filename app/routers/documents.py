from fastapi import APIRouter, HTTPException, UploadFile, File
from markitdown import MarkItDown
import os
import markdown

router = APIRouter(
    prefix="/api/documents",
    tags=["documents"]
)

TEMP_DIR = "temp_files"


if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

@router.post("/convert-files-into-md")
async def convert_files_into_md(file: UploadFile = File(...)):
    try:
        
        file_location = os.path.join(TEMP_DIR, file.filename)
        with open(file_location, "wb") as f:
            f.write(await file.read())

        md = MarkItDown(enable_plugins=False)
        result = md.convert(file_location)

        return {
            "success": True,
            "message": "Files converted into Markdown",
            "data": result.text_content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/convert-md-into-html")
async def convert_md_into_html(file: UploadFile = File(...)):
    try:
        file_location = os.path.join(TEMP_DIR, file.filename)
        with open(file_location, "wb") as f:
            f.write(await file.read())

        with open(file_location, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        html_content = markdown.markdown(markdown_content)

        return {
            "success": True,
            "message": "Markdown converted into HTML",
            "data": html_content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))