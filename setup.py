from setuptools import find_packages, setup 

def get_library_requirements(filepath: str)->list[str]:
    """
    The objective here is to return the list of the requirement libraries.
    """

    hyphen_edot = '-e .'
    requirements = []
    with open("filepath", "r") as file:
        requirements = file.readlines()
        requirements = [reg.replace("\n","") for reg in requirements]
        
        if hyphen_edot in requirements:
            requirements.remove(hyphen_edot)
    return requirements



setup(
    name="mlproject",
    version="0.0.1",
    author="hhdonglo",
    author_email="hkdonglo@gmail.com",
    packages=find_packages(),
    install_requires=get_library_requirements('requirements.txt'),
    description="ML project for climate time series analysis"
)


