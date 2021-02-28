import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/openrisc/mor1kx.git"

# Module version
version_str = "5.0.post178"
version_tuple = (5, 0, 178)
try:
    from packaging.version import Version as V
    pversion = V("5.0.post178")
except ImportError:
    pass

# Data version info
data_version_str = "5.0.post87"
data_version_tuple = (5, 0, 87)
try:
    from packaging.version import Version as V
    pdata_version = V("5.0.post87")
except ImportError:
    pass
data_git_hash = "0bca071fce56caa459d61f6c9cf7e096dc1c5d58"
data_git_describe = "v5.0-87-g0bca071"
data_git_msg = """\
commit 0bca071fce56caa459d61f6c9cf7e096dc1c5d58
Merge: a9ac821 7eb70ca
Author: Stafford Horne <shorne@gmail.com>
Date:   Mon Mar 1 06:33:11 2021 +0900

    Merge pull request #118 from stffrdhrn/github-ci
    
    Convert Travis CI to GitHub Actions

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_mor1kx."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_mor1kx".format(f))
    return fn
