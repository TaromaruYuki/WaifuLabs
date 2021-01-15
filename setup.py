import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WaifuLabs",
    version="1.0.0",
    author="Doggotaco",
    author_email="taromaruyuki@gmail.com",
    description="A unofficial wrapper for WaifuLabs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Taromaruu/WaifuLabs",
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)