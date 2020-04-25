from setuptools import setup, find_packages

# Package meta-data
NAME = "trumptweeter"
DESCRIPTION = "A library for generating Trump tweets"

setup(
    name=NAME,
    description=DESCRIPTION,
    version="0.0.1",
    packages=find_packages("trumptweets"),
    package_dir={"": "src"},
    #test_suite="test",
    install_requires=['docker>=2.0.0'],
    #entry_points={
    #     'console_scripts': ['birg = birg.cli:start'],
    #},
    include_package_data=True,
)

