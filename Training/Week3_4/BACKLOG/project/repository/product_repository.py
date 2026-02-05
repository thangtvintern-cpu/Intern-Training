from repository.base_repository import BaseRepository
from models.models import Product
from sqlmodel import Session


class ProductRepository(BaseRepository[Product]):
    def __init__(self, session: Session):
        super().__init__(Product, session)

    def get_by_name(self, name: str):
        return (
            self.session.query(self.model_type)
            .filter(self.model_type.name == name)
            .first()
        )
