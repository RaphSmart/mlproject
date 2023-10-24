# This setup.py is responsible for creating ML models as a package.
# this way any one can deploy the package and use it for prediction.


# Importing required libraries
from setuptools import setup, find_packages
from typing import List


# Defining setup function

HYPEN_E_DOT = "-e."
def get_requirememts(filename: str) -> List[str]:
    """This function is responsible for reading the requirements.txt file
    and returning the list of requirements.
    """
    requirements = []
    with open(filename) as f:
        requirements = f.readlines()
        requirements = [x.replace("\n","") for x in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
     

setup(
    name='ML-Models',
    version='0.0.1',
    description='ML Models',
    author='RaphSmart',
    author_email='bigraph4life@yahoo.com',
    packages=find_packages(),
    install_requires=get_requirememts('requirements.txt'),
    )