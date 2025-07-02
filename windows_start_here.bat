@echo off
echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting the CLI Exam App...
python exam_test.py

pause
