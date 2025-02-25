"""This module contains the packaging routine for the ``scrapy-algolia-exporter`` package"""

from setuptools import setup, find_packages

from pip._internal.network.session import PipSession
from pip._internal.req import parse_requirements


def get_requirements(source):
    """Get the requirements from the given ``source``

    Parameters
    ----------
    source: str
        The filename containing the requirements

    """

    install_reqs = parse_requirements(filename=source, session=PipSession())

    try:
        return [str(ir.req) for ir in install_reqs]
    except Exception:
        return [str(ir.requirement) for ir in install_reqs]

setup(
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


