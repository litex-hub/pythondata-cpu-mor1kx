import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/openrisc/mor1kx.git"

# Module version
version_str = "5.2.post151"
version_tuple = (5, 2, 151)
try:
    from packaging.version import Version as V
    pversion = V("5.2.post151")
except ImportError:
    pass

# Data version info
data_version_str = "5.2.post3"
data_version_tuple = (5, 2, 3)
try:
    from packaging.version import Version as V
    pdata_version = V("5.2.post3")
except ImportError:
    pass
data_git_hash = "d3f15eaac6d079836d5e67b0c62d585e0e143ece"
data_git_describe = "v5.2-3-gd3f15eaac6d0"
data_git_msg = """\
commit d3f15eaac6d079836d5e67b0c62d585e0e143ece
Author: Stafford Horne <shorne@gmail.com>
Date:   Sun Oct 13 07:40:30 2024 +0100

    github: Revert from ubunutu 24.04 to 22.04
    
    The previous latest version skipped 2 versions in github.
    We were running 22.04 before no 24.04.

"""

# Tool version info
tool_version_str = "0.0.post148"
tool_version_tuple = (0, 0, 148)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post148")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_mor1kx."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_mor1kx".format(f))
    return fn
