import setuptools


def get_description_from_readme():
    with open("README.md") as readme:
        return readme.read()


setuptools.setup(
    name="music-browser",
    description="Music search engine for CrossPlay web service.",
    author="Sylvan Le Deunff",
    author_email="sledeunf@gmail.com",
    version="0.0.3",
    url="https://github.com/tms-studio/python-music-browser",
    long_description=get_description_from_readme(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["marshmallow", "requests"],
    classifiers=[
        "Development Status :: Beta",
        "Intended Audience :: Developers",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Music :: Browse",
        "Topic :: Music :: Metadata",
    ],
)
