## Mediapipe template for Python ##

Install pyenv to manage different Python version. Currently, Mediapipe works on iOS with M1 chip with Python version 3.8.
*If you do not have a brew ([install](https://brew.sh/))* 
```commandline
brew install pyenv 
```
```commandline
pyenv install 3.8
```
Install pipenv (Python dependency management tool)
```commandline
brew install pipenv 
```
Create pipenv environment.
```commandline
pipenv 
```
Create new pipenv shell session. Which will activate virtual environment specific to your project. 
This means that any Python packages or dependencies that you install using pipenv will be installed within this virtual environment.

```commandline
pipenv shell
```
Install packages that are specified in Pipfile
```commandline
pipenv install
```
Run main script
```commandline
python main.py
```
