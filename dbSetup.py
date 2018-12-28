import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, Unicode, Binary, LargeBinary, Time, DateTime, Date, Text, Boolean, Float, JSON
from sqlalchemy.orm import relationship, backref, deferred, scoped_session
from sqlalchemy.orm import sessionmaker


def setup():
    engine = create_engine('sqlite:///db.db?check_same_thread=False')

    Base = declarative_base()

    class Product(Base):
        __tablename__ = "Product"
        id = Column('id', Integer, primary_key=True, nullable=False)
        name = Column('name', Unicode, nullable=True)
        currentPrice = Column('currentPrice', Unicode, nullable=True)
        originalPrice = Column('originalPrice', Unicode, nullable=True)

        def __repr__(self):
            return f"Product('{self.id}','{self.name}','{self.currentPrice}','{self.originalPrice}'"

    # end

    Base.metadata.create_all(engine)
    # Example creation of record
    Session = sessionmaker(bind=engine)
    session = scoped_session(sessionmaker(bind=engine))
    # prod1 = Product(name = 'Apaszka Londyn',currentPrice = '120 zł', originalPrice='120 zł')
    # session.add(prod1)
    # prod2 = Product(name = 'Apaszka Paryż',currentPrice = '120 zł', originalPrice='120 zł')
    # session.add(prod2)
    # prod3 = Product(name = 'Apaszka Tokyo',currentPrice = '120 zł', originalPrice='120 zł')
    # session.add(prod3)
    # session.commit()
    #Adding new record
    #session.commit()

