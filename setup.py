import setuptools
import waifulabs

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=waifulabs.__title__,
    version=waifulabs.__version__,
    author=waifulabs.__author__,
    author_email="taromaruyuki@gmail.com",
    description="A unofficial wrapper for WaifuLabs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Taromaruu/WaifuLabs",
    download_url="https://github.com/Taromaruu/WaifuLabs/releases/",
    install_requires=["requests", "aiohttp"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    python_requires='>=3.6'
)