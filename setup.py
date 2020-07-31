import setuptools
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hatespeechfilter-CAR", 
    version="1.0.0",
    author="Dnyanai Surkutwar",
    author_email="dsurkutwar@scu.edu",
    description="A hate speech filter app to mask or translate Central African Republic languages badwords and phrases to english",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://github.com/dnyanai/HateSpeechFilterApp",
    #package_dir={'':'app'},
    #packages=find_packages(where='app'),
    py_modules=["main","connect_getdata"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)
