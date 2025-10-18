@echo off
call venv\Scripts\activate
pytest -s -v -m "regression" --html=.\reports\report.html --browser chrome
pause