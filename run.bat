@echo off
echo Starting Backend and Frontend Servers...
echo.

echo Starting Backend Server on port 5000...
start "Backend Server" cmd /k "cd backend && python app.py"

timeout /t 5 /nobreak >nul

echo Starting Frontend Server on port 3000...
start "Frontend Server" cmd /k "cd frontend && npm start"

echo.
echo Please wait for both servers to start...
echo Backend: http://localhost:5000/api/message
echo Frontend: http://localhost:3000
echo.
