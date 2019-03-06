from setuptools import setup, find_packages

setup(
    name="dddc-petition-api",
    version="0.1.0",
    author="Puria Nafisi Azizi",
    author_email="puria@dyne.org",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.7.1",
        "zenroom==0.1.2",
        "pre-commit==1.14.4",
        "pytest_runner==4.4",
    ],
    tests_require=["pytest", "codecov", "requests", "pytest-cov"],
)