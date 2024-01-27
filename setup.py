from setuptools import setup, find_packages

setup(
    name="cleaner",
    version="0.1.0",
    author="Ken Wu",
    author_email="kenwu1009us@gmail.com",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ken1009us/cleaner",
    packages=find_packages(),
    install_requires=[
        # Dependencies listed in requirements.txt
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11.5",
    entry_points={
        "console_scripts": [
            "cleaner=cleaner.main:main",
        ],
    },
)
