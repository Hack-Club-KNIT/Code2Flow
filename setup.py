import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()

setuptools.setup(
    name="Code2Flow", # Replace with your own username
    version="0.0.1",
    license="MIT",
    author="Hack Club KNIT community",
    author_email="hcknitsln@gmail.com",
    description="A small package for converting code to a simple flowgraph",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hack-Club-KNIT/Code2Flow",
    packages=setuptools.find_packages(),
    install_requires=[req for req in requirements if req[:2] != "# "],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
