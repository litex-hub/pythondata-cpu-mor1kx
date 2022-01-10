import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/openrisc/mor1kx.git"

# Module version
version_str = "5.1.post118"
version_tuple = (5, 1, 118)
try:
    from packaging.version import Version as V
    pversion = V("5.1.post118")
except ImportError:
    pass

# Data version info
data_version_str = "5.1.post0"
data_version_tuple = (5, 1, 0)
try:
    from packaging.version import Version as V
    pdata_version = V("5.1.post0")
except ImportError:
    pass
data_git_hash = "16ad5add0ee799ca13aaf582002f08aa0c8c7ba7"
data_git_describe = "v5.1-0-g16ad5ad"
data_git_msg = """\
commit 16ad5add0ee799ca13aaf582002f08aa0c8c7ba7
Author: Stafford Horne <shorne@gmail.com>
Date:   Sun Jan 9 15:44:35 2022 +0900

    mor1kx v5.1

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_mor1kx."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_mor1kx".format(f))
    return fn
