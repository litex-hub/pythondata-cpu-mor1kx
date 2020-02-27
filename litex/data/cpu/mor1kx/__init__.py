import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/openrisc/mor1kx.git"
git_hash = "06e2e46afbad62572c31bde88e8f2424e23ecda2"
git_describe = "v5.0-76-g06e2e46"
version_str = "5.0.post76"
version_tuple = (5, 0)
try:
    from packaging.version import Version as V
    pversion = V("5.0.post76")
except ImportError:
    pass
