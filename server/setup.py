from pip.req import parse_requirements
from setuptools import setup

INSTALL_REQS = parse_requirements('requirements.txt', session='current')
REQS = [str(ir.req) for ir in INSTALL_REQS]

setup(
    install_requires=REQS
)
