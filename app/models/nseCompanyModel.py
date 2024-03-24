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

    def to_json(self):
        return {
            "id": self.id,
            "symbol": self.symbol,
            "nameOfCompany": self.nameOfCompany,
            "series": self.series,
            "dateOfListing": self.dateOfListing.isoformat(),  # Convert date to string
            "faceValue": self.faceValue
        }
    
    @classmethod
    def list_to_json(cls, nse_companies):
        return [company.to_json() for company in nse_companies]
    
    # Define the relationship
    # price_history = relationship("MarketPriceHistory", back_populates="nse_company")
    # stock_prediction = relationship("StockPricePrediction", back_populates="stock_prediction")
    
# Create the tables
Base.metadata.create_all(bind=engine)