@ECHO OFF
REM A collection of function analogues (really just labeled blocks) to help running different stages

SETLOCAL
SETLOCAL ENABLEDELAYEDEXPANSION

IF NOT DEFINED ROBOT_ENV SET ROBOT_ENV=dev
IF NOT DEFINED ROBOT_STAGES SET ROBOT_STAGES=0
IF NOT DEFINED CHROME_VERSION SET CHROME_VERSION=latest
IF NOT DEFINED WORKSPACE SET WORKSPACE=%CD%

CALL :%1
EXIT /B %ERRORLEVEL%


:setup_env
ECHO Setting up Python venv...
python -m venv .\.venv
CALL .\.venv\Scripts\activate.bat
ECHO Venv setup complete, python resolves to:
where python
python --version
pip install -r requirements.txt
rfbrowser init
EXIT /B 0

:test
ECHO Running robot tests...
CALL .\.venv\Scripts\activate.bat
pip install -r ./requirements-test.txt
pytest --pylint
IF %ERRORLEVEL% neq 0 EXIT /b %ERRORLEVEL%
rflint -A .rflintargs -r tasks resources
IF %ERRORLEVEL% neq 0 EXIT /b %ERRORLEVEL%
python run.py --env test %ROBOT_STAGES% --dryrun
EXIT /B %ERRORLEVEL%

:safety
ECHO Running safety...
CALL .\.venv\Scripts\activate.bat
pip install safety
python -m safety check --full-report
EXIT /B %ERRORLEVEL%

:process
ECHO Running robot process...
CALL .\.venv\Scripts\activate.bat
python run.py --env %ROBOT_ENV% %ROBOT_STAGES%
EXIT /B %ERRORLEVEL%

:merge_logs
CALL .\.venv\Scripts\activate.bat
rebot --merge -o output.xml --outputdir output output/output*.xml
EXIT /B %ERRORLEVEL%