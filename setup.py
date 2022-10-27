from setuptools import setup, find_packages
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "sensor-fault-detection "
AUTHOR_USER_NAME = "Akash soni"
SRC_REPO = "sensor"

REQUIREMENTS_FILE = "requirements.txt"

HYPEN_E_DOT = "-e ."

def get_requirements()->List[str]:

    requirement_list:List[str] = []

    """
    Write a code to read requiremts.txt file and append each requirements in requirements_list variable.
    """
    with open(REQUIREMENTS_FILE) as f:
        requirement_list = f.readlines()
        requirement_list = [requirement.replace("\n","")for requirement in requirement_list]
        print(requirement_list)

        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)
        
        return requirement_list
# LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Akash soni",
    description="sensor-fault-detection for Air Pressure System(APS) braking for heavy duty vheicle ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/akash-soni/sensor-fault-detection",
    author_email="akash.200287@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.8",
    install_requires= get_requirements()#LIST_OF_REQUIREMENTS
)