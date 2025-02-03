import fastapi

router = fastapi.APIRouter()

@router.get("/section/{section_id}")
async def get_section():
    return {"courses": []}

@router.get("/section/{section_id}/content-blocks")
async def get_section_content_blocks():
    return {"courses": []}

@router.get("content-blocks/{content_block_id}")
async def get_content_block():
    return {"courses": []}
