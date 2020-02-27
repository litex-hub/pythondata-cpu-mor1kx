import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from litex.data.cpu.mor1kx import version_str

setuptools.setup(
    name="litex-data-cpu-mor1kx",
    version=version_str,
    author="LiteX Authors",
    author_email="litex@googlegroups.com",
    description="Python module containing data files for using the OpenRISC1000 cpu with LiteX.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/litex-hub/litex-data-cpu-mor1kx",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={'litex.data.cpu.mor1kx': ['litex/data/cpu/mor1kx/verilog/**']},
    include_package_data=True,
)
