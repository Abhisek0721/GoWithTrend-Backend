import sys
from pathlib import Path
# Add the project root directory to the Python path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from app.models import nseCompanyModel, marketPriceHistoryModel
from app.db import base
from nselib import capital_market
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time
from app.constants import constants

engine = create_engine(
    constants.DB_DOMAIN)
Session = sessionmaker(bind=engine)
session = Session()

# Create the table if it doesn't exist
base.Base.metadata.create_all(engine, checkfirst=True)


class NSE_DataInsertion:
    def is_table_empty(self, table):
        return session.query(table).count() == 0

    def renameDataframeColumn(self, dataframe, column_to_replace):
        current_columns = dataframe.columns.tolist()
        for index in range(len(current_columns)):
            current_columns[index] = column_to_replace[index]
        dataframe.columns = current_columns
        return dataframe

    def insertNSECompaniesToDB(self):
        is_NSECompaniesEmpty = self.is_table_empty(nseCompanyModel.NSEcompany)
        if(is_NSECompaniesEmpty == False):
            print("nse_companies table is not empty. Can't be Inserted!")
            return {"success": False}
        equity_list = capital_market.equity_list()
        equity_list = self.renameDataframeColumn(
            equity_list, 
            ["symbol","nameOfCompany", "series", "dateOfListing", "faceValue"]
        )
        equity_list['dateOfListing'] = pd.to_datetime(
            equity_list['dateOfListing'], format="%d-%b-%Y")
        result = equity_list.to_dict(orient="records")
        for data in result:
            company = nseCompanyModel.NSEcompany(**data)
            session.add(company)
        session.commit()
        print("Successfully inserted NSE companies list.")
        return {"success": True}
    
    def getCompanyStockPriceHistory(self, symbol="TCS", from_date="01-01-2023", to_date="04-03-2024"):
        company_data = capital_market.price_volume_and_deliverable_position_data(
            symbol=symbol, from_date=from_date, to_date=to_date
        )
        column_to_replace = [
            "symbol",
            "series",
            "createdOn",
            "prevClose",
            "openPrice",
            "highPrice",
            "lowPrice",
            "lastPrice",
            "closePrice",
            "averagePrice",
            "totalTradedQuantity",
            "turnoverInINR",
            "numberOfTrades",
            "deliverableQty",
            "dailyQtyToTradedQtyInPercent"
        ]
        company_data = self.renameDataframeColumn(company_data, column_to_replace)
        company_data['createdOn'] = pd.to_datetime(
            company_data['createdOn'], format="%d-%b-%Y"
        )
        floatTypeColumns = [
            "prevClose",
            "openPrice",
            "highPrice",
            "lowPrice",
            "lastPrice",
            "closePrice",
            "averagePrice"
        ]
        # converting into float if it is in string
        for floatTypeColumn in floatTypeColumns:
            company_data[floatTypeColumn] = company_data[floatTypeColumn].apply(
                lambda x: float(x.replace(',', '')) if isinstance(x, str) else x
            ).astype(float)

        company_data = company_data.drop(
            ["symbol","series","deliverableQty","dailyQtyToTradedQtyInPercent"], 
            axis=1
        )
        result = company_data.to_dict(orient="records")
        return result

    
    def insertCompaniesStockPriceHistory(self, number_of_companies=10, from_date="01-01-2023", to_date="04-03-2024"):
        is_companyStockPriceHistoryEmpty = self.is_table_empty(marketPriceHistoryModel.MarketPriceHistory)
        if(is_companyStockPriceHistoryEmpty == False):
            print("market_price_history table is not empty. Can't be Inserted!")
            return {"success": False}
        
        # Query the NSEcompany table for symbols
        companies = session.query(
            nseCompanyModel.NSEcompany.id,
            nseCompanyModel.NSEcompany.symbol
        ).limit(number_of_companies).all()
        for company in companies:
            result = self.getCompanyStockPriceHistory(
                symbol=company[1], from_date=from_date, to_date=to_date
            )
            for data in result:
                data["nse_company_id"] = company[0]
                company_price_history = marketPriceHistoryModel.MarketPriceHistory(**data)
                session.add(company_price_history)
            session.commit()
            time.sleep(3)
            print(f"Stock price history of {company[1]} is inserted.")
        return {"success": True}


nseDataInsertion = NSE_DataInsertion()
nseDataInsertion.insertNSECompaniesToDB()
nseDataInsertion.insertCompaniesStockPriceHistory(50)
