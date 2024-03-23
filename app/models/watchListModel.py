from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship
from app.db.session import engine
from datetime import datetime


class WatchList(Base):
    __tablename__ = 'watchlist'
    id                           = Column(Integer, primary_key=True, autoincrement=True)
    user_id                      = Column(Integer, ForeignKey('nse_companies.id'))
    nse_company_id               = Column(Integer, ForeignKey('nse_companies.id'))
    symbol                       = Column(String(255), ForeignKey('nse_companies.symbol'))
    nameOfCompany                = Column(String(255), ForeignKey('nse_companies.nameOfCompany'))
    createdAt                    = Column(DateTime, default=datetime.utcnow())

    # Define the relationship
    # user = relationship("User", back_populates="user")
    # nse_company = relationship("NSEcompany", back_populates="nse_company")
    
# Create the tables
Base.metadata.create_all(bind=engine)