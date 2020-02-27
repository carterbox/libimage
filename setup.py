#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name='libimage',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
    use_scm_version=True,
    include_package_data=True,
    zip_safe=False,
    author='Daniel Ching',
    author_email='dching@anl.gov',
    license='CC BY-SA',
    platforms='Any',
)
