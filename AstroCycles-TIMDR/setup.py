from setuptools import setup, find_packages

setup(
    name="astrocycles_timdr",
    version="0.1.0",
    author="Jacek",
    description="A geometric model of astrological cycles based on the TIMDR framework.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.8",
    entry_points={
    "console_scripts": [
        "timdr=timdr_cli.__main__:main",
    ]
},

)
