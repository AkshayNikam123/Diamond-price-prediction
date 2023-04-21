from setuptools import find_packages,setup
from typing import List

hypen_e_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace("\n"," ") for req in requirements] #\n in raw text of requirment.txt

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements


setup(
    name="RegressorProject",
    version='0.0.1',
    author='Akshay',
    author_email='nikam.ak152@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)