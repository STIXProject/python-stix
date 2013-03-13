from setuptools import setup, find_packages

setup(
    name="stix",
    version="1.0a1",
    author="STIX Project, MITRE Corporation",
    author_email="stix@mitre.org",
    description="An API for parsing and generating STIX content.",
    url="http://stix.mitre.org",
    packages=find_packages(),
    install_requires=['lxml>=2.3', 'python-dateutil', 'cybox>=1.0b1', 'maec>=3.0a1'],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)
