from setuptools import find_packages, setup

setup(
    name="python-utils",
    version="0.0.1",
    author="fbjarkes",
    author_email="fbjarkes-github.q5706@aleeas.com",
    description="",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.2.1",
    ],
    python_requires='>=3.9.5',
)
