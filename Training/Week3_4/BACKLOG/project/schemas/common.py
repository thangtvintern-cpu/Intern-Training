


from pydantic import BaseModel,Field
class Pagination(BaseModel):
    limit: int = Field(gt=0, default=10)
    page: int = Field(default=1, gt=0)

    @property
    def offset(self):
        return (self.page - 1) * self.limit