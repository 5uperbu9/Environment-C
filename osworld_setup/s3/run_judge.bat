@echo off
REM Activate venv if needed:
REM call ../../.venv\Scripts\activate

python -m run_judge ^
 --result_dir "results/pyautogui/screenshot" ^
 --model "qwen2.5:3b"

pause
