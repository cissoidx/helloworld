import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helloworld_example",
    version="0.0.1",
    author="DONGXu",
    author_email="gzudong@163.com",
    description="my example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="no.url.yet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
