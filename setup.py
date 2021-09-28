from setuptools import setup
from io import open

setup(
    name="vacances_scolaires_france",
    license="MIT",
    packages=["vacances_scolaires_france"],
    version="0.8.1",
    description="Get school holiday dates for metropolitan France",
    author="Antoine Augusti",
    author_email="hi@antoine-augusti.fr",
    url="https://github.com/AntoineAugusti/vacances-scolaires-france",
    keywords=[
        "vacances",
        "scolaires",
        "calendrier",
        "france",
        "school",
        "holiday",
        "calendar",
    ],
    extras_require={"dev": ["nose"]},
    package_data={"vacances_scolaires_france": ["data/data.csv"]},
    python_requires=">=2.7, <4",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)
