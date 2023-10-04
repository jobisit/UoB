import setuptools  

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(  
    name="pygad",  
    version="3.2.0",  
    author="Lamin Jobe",
    install_requires=["numpy", "matplotlib", "cloudpickle",],
    author_email="laminsj@hotmail.com.com",  
    description="PyGAD: A Python Library for Building the Genetic Algorithm).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jobisit/UoB",
    packages=setuptools.find_packages())
