from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in computroidcms/__init__.py
from computroidcms import __version__ as version

setup(
	name="computroidcms",
	version=version,
	description="Computroid CMS",
	author="netmanthan",
	author_email="info@netmanthan.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
