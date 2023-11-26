from setuptools import setup

setup(
    py_modules=["main"],
    install_requires=[
        "click",
    ],
    entry_points={"console_scripts": ["pywc = main:main"]},
)
