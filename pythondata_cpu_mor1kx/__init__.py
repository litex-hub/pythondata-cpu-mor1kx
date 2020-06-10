import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/openrisc/mor1kx.git"

# Module version
version_str = "5.0.post134"
version_tuple = (5, 0, 134)
try:
    from packaging.version import Version as V
    pversion = V("5.0.post134")
except ImportError:
    pass

# Data version info
data_version_str = "5.0.post76"
data_version_tuple = (5, 0, 76)
try:
    from packaging.version import Version as V
    pdata_version = V("5.0.post76")
except ImportError:
    pass
data_git_hash = "06e2e46afbad62572c31bde88e8f2424e23ecda2"
data_git_describe = "v5.0-76-g06e2e46"
data_git_msg = """\
commit 06e2e46afbad62572c31bde88e8f2424e23ecda2
Author: JaewonHur <57657645+JaewonHur@users.noreply.github.com>
Date:   Mon Dec 23 01:23:20 2019 +0900

    Fix mor1kx_decode to accept valid l.fl1 (l.ff1) instructions (#110)
    
    * Fix mor1kx_decode to only accept valid l.fl1 and l.ff1 instructions
    
    Both l.fl1 and l.ff1 have bit 9 set in the insruction as port of their op codes,
    mor1kx_decode does not currently properly check this

"""

# Tool version info
tool_version_str = "0.0.post58"
tool_version_tuple = (0, 0, 58)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post58")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_mor1kx."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_mor1kx".format(f))
    return fn
