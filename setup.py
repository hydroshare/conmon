"""
Setup script for the conmon package.
"""

from setuptools import setup
from setuptools import find_packages


def version():
    """
    version() -> str

    Return the version string.
    """

    with open("VERSION.txt") as v:
        _version = v.read()
    return _version.strip()


__version__ = version()


def long_description():
    """
    long_descriptions -> str

    Return the long description text.
    """

    with open("README.rst") as r:
        long_description_1 = r.read()
    with open("HISTORY.rst") as h:
        long_description_2 = h.read()
    return "\n".join([long_description_1, long_description_2, ])


setup(name="conmon",
      version=__version__,
      packages=find_packages(),
      author="Chris Calloway",
      author_email="cbc@chriscalloway.org",
      description="A package for monitoring Docker containers.",
      long_description=long_description(),
      url="https://github.com/hydroshare/conmon",
      download_url="https://github.com/hydroshare/conmon/tarball/" + __version__,
      keywords="Docker container monitor",
      classifiers=["Development Status :: 2 - Pre-Alpha",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: POSIX :: Linux",
                   "Programming Language :: Python :: 3",
                   "Topic :: System :: Monitoring",
                   "Intended Audience :: Developers",
                   "Intended Audience :: System Administrators",
                  ],
      zip_safe=False,
      python_requires='>=3',
      install_requires=["docker-py",
                        "pyyaml",
                       ],
      tests_require=["docker-py",
                     "pyyaml",
                    ],
      test_suite="conmon.tests")
