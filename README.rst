=============================
Google Style pre-commit Hooks
=============================

.. image:: https://img.shields.io/pypi/v/google-style-pre-commit-hooks.svg
    :target: https://pypi.python.org/pypi/google-style-pre-commit-hooks

.. image:: https://travis-ci.org/starofrainnight/google-style-pre-commit-hooks.svg?branch=master
    :target: https://travis-ci.org/starofrainnight/google-style-pre-commit-hooks

.. image:: https://ci.appveyor.com/api/projects/status/github/starofrainnight/google-style-pre-commit-hooks?svg=true
    :target: https://ci.appveyor.com/project/starofrainnight/google-style-pre-commit-hooks

A series pre-commit hooks that support format source by google style

* License: Apache-2.0

Usage
---------

Environment
~~~~~~~~~~~~~~~

Before using these pre-commit hooks, you must ensure there have these components
installed:

* Python 3.5+
* pre-commit
* JRE 1.8+
* wget
* google-java-format global installed  (optional)

google-java-format will be download and installed under project's '.cache'
directory if google-java-format not been detected in global environment or under
'.cache' directory.

Configuration
~~~~~~~~~~~~~~~

Added these configs into .pre-commit-config.yaml under your project's root:

::

    repos:
    - repo: https://github.com/starofrainnight/google-style-pre-commit-hooks
      rev: master
      hooks:
      - id: google-java-style

Credits
---------

This package was created with Cookiecutter_ and the `PyPackageTemplate`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`PyPackageTemplate`: https://github.com/starofrainnight/rtpl-pypackage

