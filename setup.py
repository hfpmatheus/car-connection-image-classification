import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

__version__ = "0.0.0"

GITHUB_REPO_NAME = "car-connection-image-classification"
GITHUB_AUTHOR_USERNAME = "hfpmatheus"
SRC_REPO = "src"
AUTHOR_EMAIL = "matheushffp@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=GITHUB_AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="Model to classify cars",
    long_description=long_description,
    url=f"https://github.com/{GITHUB_AUTHOR_USERNAME}/{GITHUB_REPO_NAME}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)