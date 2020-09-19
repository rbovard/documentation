# -*- coding: utf-8 -*-

import os
import subprocess

''' Convert to GeoTIFF '''
def convert_to_geotiff(input_path, input_raster_extension, output_path, output_compression):
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for file in os.listdir(input_path):
        input_file = os.path.join(input_path, file)

        if os.path.isfile(input_file):
            file_name = file.split(".")

            if file_name[1] == input_raster_extension:
                output_file = os.path.join(output_path, file_name[0] + ".tif")

                # Create tiled file
                gdal_command = "gdal_translate -of GTiff -co TILED=YES -co TFW=YES -co PROFILE=BASELINE -co COMPRESS={} {} {}".format(output_compression, input_file, output_file)
                process = subprocess.Popen(gdal_command).communicate()[0]

                # Build overview images
                gdal_command = "gdaladdo -r average {} 2 4 8 16".format(output_file)
                process = subprocess.Popen(gdal_command).communicate()[0]

''' Generate raster tileindex '''
def generate_raster_tileindex(path):
    tileindex_file = os.path.join(path, "tileindex.shp")
    gdal_command = "gdaltindex {} {}".format(tileindex_file, os.path.join(path, "*.tif"))
    output = subprocess.Popen(gdal_command).communicate()[0]

# Define variables
input_path = os.path.normpath(r"C:\Temp")
output_path = os.path.join(input_path, "output")
input_raster_extension = "tif"

# `LZW`: lossless compression
# `JPEG`: lossy compression
output_compression = "LZW"

# Execute scripts
convert_to_geotiff(input_path, input_raster_extension, output_path, output_compression)
generate_raster_tileindex(output_path)
