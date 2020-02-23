#!/usr/bin/env python3
import os

from litex.data.cpu import mor1kx

print("Found mor1kx @ version", mor1kx.version_str, "("+mor1kx.git_hash+")")
print("Data is in", mor1kx.data_location)
assert os.path.exists(mor1kx.data_location)
print("It contains:\n -", end=" ")
print("\n - ".join(os.listdir(mor1kx.data_location)))