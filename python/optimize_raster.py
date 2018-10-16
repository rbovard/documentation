# -*- coding: utf-8 -*-

import os
import subprocess

inputPath = os.path.normpath(r"C:\Temp")
outputPath = os.path.join(inputPath, "output")
tileindexFile = os.path.join(outputPath, "tileindex.shp")
inputRasterExtension = "tif"
outputRasterExtension = "tif"

if not os.path.exists(outputPath):
    os.mkdir(outputPath)

# Convert to GeoTIFF
for file in os.listdir(inputPath):
    inputFile = os.path.join(inputPath, file)

    if os.path.isfile(inputFile):
        fileName = file.split(".")

        if fileName[1] == inputRasterExtension:
            outputFile = os.path.join(outputPath, fileName[0] + "." + outputRasterExtension)

            # Create tiled file
            # Use `COMPRESS=LZW` for lossless compression
            # Use `COMPRESS=JPEG` for lossy compression
            gdalCommand = "gdal_translate -of GTiff -co TILED=YES -co TFW=YES -co PROFILE=BASELINE -co COMPRESS=LZW {} {}".format(inputFile, outputFile)
            process = subprocess.Popen(gdalCommand).communicate()[0]

            # Build overview images
            gdalCommand = "gdaladdo -r average {} 2 4 8 16".format(outputFile)
            process = subprocess.Popen(gdalCommand).communicate()[0]

# Generate raster tileindex
gdalCommand = "gdaltindex {} {}".format(tileindexFile, os.path.join(outputPath, "*." + outputRasterExtension))
output = subprocess.Popen(gdalCommand).communicate()[0]
