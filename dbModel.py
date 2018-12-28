from sqlalchemy import Column, Integer, Unicode
from app import db

class Product(db.Model):
    __tablename__ = "Product"
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', Unicode, nullable=True)
    currentPrice = Column('currentPrice', Unicode, nullable=True)
    originalPrice = Column('originalPrice', Unicode, nullable=True)
