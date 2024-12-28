from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements file and returns a list of requirements.

    Args:
        file_path (str): Path to the requirements file.

    Returns:
        List[str]: List of dependencies.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Strip newlines and extra spaces
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="RegressionProject",
    version="0.0.1",
    author="Rk",
    author_email="ranjitkulkarni6@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
