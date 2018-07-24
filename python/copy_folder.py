# -*- coding: utf-8 -*-

import os
import shutil

inputPath = os.path.normpath(r"C:\Temp\Input")
outputPath = os.path.normpath(r"C:\Temp\Output")

def copy(source, destination):
    try:
        if os.path.exists(destination):
            try:
                shutil.rmtree(destination)
            except Exception as e:
                print(e)

        shutil.copytree(source, destination)

    except Exception as e:
        print(e)

copy(inputPath, outputPath)
