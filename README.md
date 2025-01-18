# cteleport

Clone project from GitHub
git clone https://github.com/zandrei83/cteleport.git

Change directory
cd cteleport
Create venv
python -m venv venv
Install dependencies
pip install -r requirements.txt
Install playwrite
playwright install
Running tests 
To run test for English version of website run:
pytest --headed -v -s --language=en
For Dutch:
pytest --headed -v -s --language=nl


