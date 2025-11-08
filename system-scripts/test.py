#!/usr/bin/env python3

import pathlib

for file in pathlib.Path("/Users/mikolajmazur").glob("*"):
    print(file)