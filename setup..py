import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="prnt.sc-scraper",
    version="2.1.0",
    description="Pulls random images from https://prnt.sc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ItzBlinkzy/prnt.sc-scraper",
    author="Itz Blinkzy",
    author_email="kitey13579@gmail.com",
    license="GNU",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="scraper - prnt.sc",
    python_requires=">=3.7",
    packages=setuptools.find_packages(),
    install_requires=["requests", "bs4"],
)