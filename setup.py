from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
# '''this function is used to get the list of requirements 
# from the requirements.txt file'''

    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = "mlproject",
    version='0.0.1',
    author = 'Arup',
    author_email='Arup.pati676@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)