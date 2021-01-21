import setuptools
import glob
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

scripts = []

for f in glob.glob(os.path.join('bin', '*')):
    if os.path.isfile(f):
        scripts.append(f)

print(scripts)

setuptools.setup(
    name="dicomUtils-fsantini",
    version="0.0.1",
    author="Francesco Santini",
    author_email="francesco.santini@gmail.com",
    description="Set of scripts to deal with DICOM images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fsantini/python-dicom-utils",
    packages=['dicomUtils'],
    scripts = scripts,
    install_requires=['numpy', 'nibabel', 'pydicom', 'progress', 'h5py', 'scipy', 'SimpleITK'],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
