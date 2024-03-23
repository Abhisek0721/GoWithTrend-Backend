from sqlalchemy import Column, Integer, String, Date
from app.db.base import Base
from sqlalchemy.orm import relationship
from app.db.session import engine

class NSEcompany(Base):
    __tablename__ = 'nse_companies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(255), nullable=False, unique=True)
    nameOfCompany = Column(String(255), nullable=False)
    series = Column(String(8), nullable=False)
    dateOfListing  = Column(Date, nullable=False)
    faceValue = Column(Integer)

    # Define the relationship
    # price_history = relationship("MarketPriceHistory", back_populates="nse_company")
    # stock_prediction = relationship("StockPricePrediction", back_populates="stock_prediction")
    
# Create the tables
Base.metadata.create_all(bind=engine)