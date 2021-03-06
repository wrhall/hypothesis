# coding=utf-8

# Copyright (C) 2013-2015 David R. MacIver (david@drmaciver.com)

# This file is part of Hypothesis (https://github.com/DRMacIver/hypothesis)

# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.

# END HEADER

from distutils.core import setup
from setuptools.command.test import test as TestCommand
from setuptools import find_packages
import sys
import os


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


def local_file(name):
    return os.path.join(os.path.dirname(__file__), name)

SOURCE = local_file("src")
REQUIREMENTS = local_file("requirements.txt")
README = local_file("README.rst")

setup(
    name='hypothesis-fakefactory',
    version='0.2.2',
    author='David R. MacIver',
    author_email='david@drmaciver.com',
    packages=find_packages(SOURCE),
    package_dir={"": SOURCE},
    url='https://github.com/DRMacIver/hypothesis',
    license='MPL v2',
    description='Adds support for generating fake-factory data to Hypothesis',
    install_requires=[
        "hypothesis==0.7.2",
        "fake-factory==0.4.2",
    ],
    long_description=open(README).read(),
    entry_points={
        'hypothesis.extra': 'hypothesisfakefactory = hypothesisfakefactory'
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Testing",
    ],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
