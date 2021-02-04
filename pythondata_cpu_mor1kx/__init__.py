import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/openrisc/mor1kx.git"

# Module version
version_str = "5.0.post153"
version_tuple = (5, 0, 153)
try:
    from packaging.version import Version as V
    pversion = V("5.0.post153")
except ImportError:
    pass

# Data version info
data_version_str = "5.0.post80"
data_version_tuple = (5, 0, 80)
try:
    from packaging.version import Version as V
    pdata_version = V("5.0.post80")
except ImportError:
    pass
data_git_hash = "a9ac8213d9f752485a6f2bd46885ca37a53899c2"
data_git_describe = "v5.0-80-ga9ac821"
data_git_msg = """\
commit a9ac8213d9f752485a6f2bd46885ca37a53899c2
Merge: dd01358 cf2bce7
Author: Stafford Horne <shorne@gmail.com>
Date:   Fri Jan 1 10:49:08 2021 +0900

    Merge pull request #116 from openrisc/fix-ci
    
    travis: Env vars are no longer passed to docker, maybe quotes?

"""

# Tool version info
tool_version_str = "0.0.post73"
tool_version_tuple = (0, 0, 73)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post73")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_mor1kx."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_mor1kx".format(f))
    return fn
