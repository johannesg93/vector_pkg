import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vector-pkg-JOHANNES-OIDA",
    version="0.0.1",
    author="Johannes",
    author_email="jgerwinat.uni@gmail.com",
    description="Des is a vektor package. hoff ma es funktioniert. bam oida.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

