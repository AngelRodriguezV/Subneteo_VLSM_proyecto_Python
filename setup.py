from setuptools import setup, find_packages

import os, re, codecs

NAME = "subneteo_vlsm"
META_PATH = os.path.join(NAME, "__init__.py")
REQUIREMENRS = ["pandas"]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: Español",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
]
HERE = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


if __name__ == "__main__":
    setup(
        name = NAME,
        version = find_meta("version"),
        author = find_meta("author"),
        author_email = find_meta("email"),
        description = find_meta("description"),
        url = find_meta("url"),
        license = find_meta("license"),
        long_description = open("README.md").read(),
        packages = find_packages(),
        zip_safe=False,
        install_requires = REQUIREMENRS,
        classifiers = CLASSIFIERS
        )