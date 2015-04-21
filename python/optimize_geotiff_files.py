# -*- coding: utf-8 -*-

import os
import subprocess

inputPath = os.path.normpath("C:\Temp")
outputPath = os.path.join(inputPath, "output")

if not os.path.exists(outputPath):
    os.mkdir(outputPath)

for file in os.listdir(inputPath):
    inputFile = os.path.join(inputPath, file)

    if os.path.isfile(inputFile):
        fileName = file.split(".")

        if fileName[1] == "tif":
            outputFile = os.path.join(outputPath, file)

            # Create tiled file
            gdalCommand = "gdal_translate -of GTiff -co \"TILED=YES\" -co \"TFW=YES\" {} {}" . format(inputFile, outputFile)
            process = subprocess.Popen(gdalCommand).communicate()[0]

            # Build overview images
            gdalCommand = "gdaladdo -r average {} 2 4 8 16" . format(outputFile)
            process = subprocess.Popen(gdalCommand).communicate()[0]
