# GoWithTrend

## (Stock Price Prediction Software - Backend)

## How to Run ?

To run this api in development environment:
Step-1
```
pip install -r requirements.txt
```
Step-2
```
uvicorn main:app --reload
```

To insert initial data to database:
Step-1
```
chmod +x insertDataToDB.sh
```
Step-2
```
./insertDataToDB.sh
```


### Link: https://chat.openai.com/share/765ed09b-442c-48bc-a363-e3901c54b0af

### Project Directory Structure

```markdown
project_root/
│
├── app/
│   ├── api/                    # API route definitions
│   │   ├── __init__.py
│   │   ├── auth.py             # Authentication routes
│   │   ├── contacts.py            # Item related routes
│   │   └── users.py            # User related routes
│   │
│   ├── core/                   # Core functionality
│   │   ├── __init__.py
│   │   ├── config.py           # Configuration settings
│   │   ├── security.py         # Security utilities
│   │   └── ...
│   │
│   ├── db/                     # Database related code
│   │   ├── __init__.py
│   │   ├── base.py             # Base DB model
│   │   └── session.py          # Database session initialization
│   │
│   ├── dependencies/           # Dependency definitions
│   │   ├── __init__.py
│   │   └── auth.py             # Authentication dependency
│   │
│   ├── models/                 # Pydantic models
│   │   ├── __init__.py
│   │   ├── item.py             # Item model
│   │   └── user.py             # User model
│   │
│   └── utils/                  # Utility functions
│       ├── __init__.py
│       ├── email.py            # Email sending utilities
│       └── ...
│
├── tests/                      # Unit and integration tests
│   ├── __init__.py
│   ├── test_api.py             # API route tests
│   ├── test_core.py            # Core functionality tests
│   └── ...
│
├── alembic/                    # Alembic migrations
│   ├── versions/
│   └── env.py
│
├── .env                        # Environment variables
├── main.py                     # FastAPI application creation
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```