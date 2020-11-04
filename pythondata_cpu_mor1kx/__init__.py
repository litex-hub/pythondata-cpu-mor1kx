import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/openrisc/mor1kx.git"

# Module version
version_str = "5.0.post143"
version_tuple = (5, 0, 143)
try:
    from packaging.version import Version as V
    pversion = V("5.0.post143")
except ImportError:
    pass

# Data version info
data_version_str = "5.0.post77"
data_version_tuple = (5, 0, 77)
try:
    from packaging.version import Version as V
    pdata_version = V("5.0.post77")
except ImportError:
    pass
data_git_hash = "9679d18eabaf6a15ee56eafdd35812043d9ae193"
data_git_describe = "v5.0-77-g9679d18"
data_git_msg = """\
commit 9679d18eabaf6a15ee56eafdd35812043d9ae193
Author: Andrey Bacherov <bandvig@mail.ru>
Date:   Sun Jul 26 15:40:12 2020 +0300

    Open OPTION_FTOI_ROUNDING as "CPP" in according with spec 1.3.

"""

# Tool version info
tool_version_str = "0.0.post66"
tool_version_tuple = (0, 0, 66)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post66")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_mor1kx."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_mor1kx".format(f))
    return fn
