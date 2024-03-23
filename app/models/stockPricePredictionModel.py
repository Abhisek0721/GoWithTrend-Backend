from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from app.db.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import engine


class StockPricePrediction(Base):
    __tablename__ = 'stock_price_prediction'
    id                           = Column(Integer, primary_key=True, autoincrement=True)
    nse_company_id               = Column(Integer, ForeignKey('nse_companies.id'))
    prevClose                    = Column(Float, nullable=False)
    openPrice                    = Column(Float, nullable=False)
    lastPrice                    = Column(Float)
    highPrice                    = Column(Float, nullable=False)
    lowPrice                     = Column(Float, nullable=False)
    closePrice                   = Column(Float, nullable=False)
    averagePrice                 = Column(Float, nullable=False)
    createdAt                    = Column(DateTime, default=datetime.utcnow())
    updatedAt                    = Column(DateTime, default=datetime.utcnow())

    # Define the relationship
    # nse_company = relationship("NSEcompany", back_populates="nse_company")
    
# Create the tables
Base.metadata.create_all(bind=engine)