import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/openrisc/mor1kx.git"

# Module version
version_str = "5.0.post231"
version_tuple = (5, 0, 231)
try:
    from packaging.version import Version as V
    pversion = V("5.0.post231")
except ImportError:
    pass

# Data version info
data_version_str = "5.0.post119"
data_version_tuple = (5, 0, 119)
try:
    from packaging.version import Version as V
    pdata_version = V("5.0.post119")
except ImportError:
    pass
data_git_hash = "95eee0596a160ffdfd8ee6bc8b88268b2e49ec5e"
data_git_describe = "v5.0-119-g95eee05"
data_git_msg = """\
commit 95eee0596a160ffdfd8ee6bc8b88268b2e49ec5e
Merge: e28f9a4 6e61ee5
Author: Stafford Horne <shorne@gmail.com>
Date:   Wed Sep 1 22:18:37 2021 +0900

    Merge pull request #138 from Harshitha172000/master
    
    Update Mor1kx-Formal project progress in Readme

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_mor1kx."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_mor1kx".format(f))
    return fn
