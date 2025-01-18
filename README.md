# C teleport test assignment
Creating testing framework for website kiwi.com. 
## Sett up environment
Clone the project from GitHub
```
git clone https://github.com/zandrei83/cteleport.git
```
Change working  directory
```
cd cteleport
```
Create venv
```
python -m venv venv
```
Install dependencies
```
pip install -r requirements.txt
```
Install Playwright
```
playwright install
```
### Running tests 
Implemented the possibility of testing the website in different languages. 

For English:
```
pytest --headed -v -s --language=en
```
For Dutch:
```
pytest --headed -v -s --language=nl
```
