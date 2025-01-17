import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="example-pkg-mikevogt",
	version="0.0.1",
	author="Michael Vogt",
	author_email="author@email.co.za",
	description="a small package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/pypa/sampleproject",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT Licence",
		"Operating System :: OS Independent",
	],
	packages=setuptools.find_packages(),
	python_requires='>=3.6',
)
