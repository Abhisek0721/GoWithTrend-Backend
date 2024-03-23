from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from app.db.base import Base
from sqlalchemy.orm import relationship
from app.db.session import engine


class MarketPriceHistory(Base):
    __tablename__ = 'market_price_history'
    id                           = Column(Integer, primary_key=True, autoincrement=True)
    nse_company_id               = Column(Integer, ForeignKey('nse_companies.id'))
    createdOn                    = Column(Date, nullable=False)
    prevClose                    = Column(Float, nullable=False)
    openPrice                    = Column(Float, nullable=False)
    highPrice                    = Column(Float, nullable=False)
    lowPrice                     = Column(Float, nullable=False)
    lastPrice                    = Column(Float)
    closePrice                   = Column(Float, nullable=False)
    averagePrice                 = Column(Float, nullable=False)
    totalTradedQuantity          = Column(String(255))
    turnoverInINR                = Column(String(255))
    numberOfTrades               = Column(String(255))

    # Define the relationship
    # nse_company = relationship("NSEcompany", back_populates="price_history")

# Create the tables
Base.metadata.create_all(bind=engine)