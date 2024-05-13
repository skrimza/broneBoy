from .database import Base, Column
from sqlalchemy import BIGINT, BOOLEAN, ForeignKey, TIMESTAMP, SMALLINT, VARCHAR, LargeBinary, INTEGER


class User(Base):
    id = Column(BIGINT, primary_key=True)
    is_blocked = Column(BOOLEAN, default=False)

 
class UserReservation(Base):
    user_id = Column(BIGINT, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    selection = Column(BIGINT)
    delivery_type = Column(VARCHAR(24), nullable=False)
    user_name = Column(VARCHAR(128), nullable=False)
    address = Column(VARCHAR(256), nullable=True)
    phone_number = Column(VARCHAR(24), nullable=False)
    date_reservation = Column(TIMESTAMP, nullable=False)
    
# class TShirt(Base):
#     product_id = Column(SMALLINT, primary_key = True)
#     image_tshirt = Column()
#     price = column(SMALLINT, nullable=False)
    
# class SweatShirt(Base):
#     product_id = Column(SMALLINT, primary_key = True)
#     image_sweatshirt = Column()
#     price = Column(SMALLINT, nullable=False)
    