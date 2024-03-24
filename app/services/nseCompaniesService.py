from app.models.nseCompanyModel import NSEcompany

class NSECompaniesService:
    @staticmethod
    def get_nse_companies(db, data, currentPage, limit):
        totalCompanies = db.query(NSEcompany).count()
        totalPage = totalCompanies/limit
        if round(totalCompanies/limit) < totalPage:
            totalPage = round(totalPage) + 1
        else:
            totalPage = round(totalPage)
        responseData = {
            "companies": data,
            "totalCompanies": totalCompanies,
            "currentPage": currentPage,
            "totalPages": totalPage
        }
        return responseData