from setuptools import find_packages,setup
#from typing import list
def get_requirement(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Salil',
    author_email='tambolisalil02@gmail.com',
    packages=find_packages(),
    install_requires = get_requirement('requirements.txt')
)