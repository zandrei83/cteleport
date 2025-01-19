# C teleport test assignment
Creating testing framework for website kiwi.com. 
## Set up environment
Clone the project from GitHub:
```
git clone https://github.com/zandrei83/cteleport.git
```
Change working  directory:
```
cd cteleport
```
Create and activate virtual environment:
```
python -m venv venv
venv\Scripts\activate
```
Install project dependencies:
```
pip install -r requirements.txt
```
Install the required browsers:
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

To run one particular test from test suite:

```
pytest --headed -v -s --language=en .\tests\test_basic_search.py::TestBasicSearch::test_basic_search_not_logged
```