#!/usr/bin/env python3
import os

from litex.data.cpu import mor1kx

print("Found mor1kx @ version", mor1kx.version_str, "(with data", mor1kx.data_version_str, ")")
print()
print("Data is in", mor1kx.data_location)
assert os.path.exists(mor1kx.data_location)
print("Data is version", mor1kx.data_version_str, mor1kx.data_git_hash)
print("-"*75)
print(mor1kx.data_git_msg)
print("-"*75)
print()
print("It contains:")
for root, dirs, files in os.walk(mor1kx.data_location):
    dirs.sort()
    for f in sorted(files):
        path = os.path.relpath(os.path.join(root, f), mor1kx.data_location)
        print(" -", path)
