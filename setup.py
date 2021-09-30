import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="svo-extract",
    version="0.0.1",
    author="owo",
    author_email="key.cat@outlook.com",
    description="A package using clip to extrac S,V,O",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Keycatowo/svo-extract",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    # install_requires=[
    #     "python>=3.6.0"
    #     "tensorflow>=1.13.1",
    #     "gdown",
    # ],

)