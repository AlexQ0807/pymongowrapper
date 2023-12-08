import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pymongowrapper',
    version='0.2.1',
    author='Alex Q',
    author_email='alex.quan0807@gmail.com',
    description='Personal Wrapper for Mongo DB operations',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['pymongowrapper'],
    install_requires=[
        "pymongo",
        "certifi"
    ],
)