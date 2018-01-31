from setuptools import setup, find_packages
import os,sys

setup(
    name = "CtmJobForceOk",
    version = "1.0",
    author="Miki Manor",
    author_email="mmanor@isracard.co.il",
    description="utility fom ControlM which gets var name, traslate the var to Order Id and then Force Ok The job",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.5"
    ],
    install_requires=['UsefulUtilities'],
    python_requires='>=3',
    packages = find_packages(),
    )

