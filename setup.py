import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as r:
    required = r.read().splitlines()

setuptools.setup(
    name="pandas_Project",
    version="1.0",
    author="saba yousefzadeh",
    author_emai="sbyousef83@gmail.com",
    description="A script to find and count hashtags, mentions, or dollar words in text.",
    long_description=long_description,
    packages=setuptools.find_packages(),
    install_requires=required,
    python_requires=">=3.9",
    include_package_data=True,
)
