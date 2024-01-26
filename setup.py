from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("dev_requirements.txt", "r", encoding="utf-8") as fh:
    dev_requirements = fh.read()
    
setup(
    name = 'routerfy',
    version = '0.0.1',
    author = 'Bruno Junqueira & Mateus Brazil',
    author_email = 'brunosdsj@gmail.com',
    license = 'MIT',
    description = 'O Routerfy tem uma sintaxe similar ao FastAPI. Feito para ser leve e de fácil uso para serviços AWS Serverless.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.pactual.net/bruno-s-junqueira/routerfy',
    py_modules = ['routerfy'],
    include_package_data=True,
    packages = find_packages(),
    extras_require ={
        "dev": [dev_requirements]
    },
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        routerfy=routerfy.cli:cli
    '''
)