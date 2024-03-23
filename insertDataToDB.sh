#!/bin/bash
source .venv/Scripts/activate
pip install -r requirements.txt
python ./app/script/insertCompanyList.py
deactivate
