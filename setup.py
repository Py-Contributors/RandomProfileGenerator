import setuptools
from glob import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

__title__ = 'RandomProfileGenerator'
__package_name__ = 'random_profile'
__version__ = '3.0.2'
__description__ = "Python Module To Generate Random Profile Data"
__email__ = "deepak008@live.com"
__author__ = 'Deepak Raj'
__github__ = 'https://github.com/Py-Contributors/RandomProfileGenerator'
__pypi__ = 'https://pypi.org/project/random-profile/'
__license__ = 'MIT License'


setuptools.setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    data_files=[('assets', glob('random_profile/assets/*'))],
    url=__github__,
    packages=setuptools.find_packages(),
    project_urls={"Documentation": "https://pycontributors.readthedocs.io/projects/randomprofilegenerator/en/latest/",
                  "Source": "https://github.com/Py-Contributors/RandomProfileGenerator",
                  "Tracker": "https://github.com/Py-Contributors/RandomProfileGenerator/issues",
                  "Funding": "https://github.com/sponsors/codePerfectPlus"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Environment :: Plugins"],
    entry_points={
        "console_scripts": ['rp = random_profile.cli:main',
                            "random_profile = random_profile.cli:main"],

    },
)
