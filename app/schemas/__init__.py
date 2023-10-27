from pydantic import BaseModel


class OkResponseSchema(BaseModel):
    ok: bool
