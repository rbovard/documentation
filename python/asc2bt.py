# -*- coding: utf-8 -*-

import os
import subprocess

''' Convert ASCII Grids to Binary Terrain files '''
def asc2bt(input_path, output_path):
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for file in os.listdir(input_path):
        input_file = os.path.join(input_path, file)

        if os.path.isfile(input_file):
            file_name = file.split(".")

            if file_name[1] == "asc":
                output_file = os.path.join(output_path, file_name[0] + ".bt")
                gdal_command = "gdal_translate -of bt {} {}".format(input_file, output_file)
                process = subprocess.Popen(gdal_command).communicate()[0]

''' Generate tileindex '''
def generate_tileindex(path):
    tileindex_file = os.path.join(path, "tileindex.shp")
    gdal_command = "gdaltindex {} {}".format(tileindex_file, os.path.join(path, "*.bt"))
    output = subprocess.Popen(gdal_command).communicate()[0]

# Define variables
input_path = os.path.normpath(r"C:\Temp")
output_path = os.path.join(input_path, "output")

# Execute scripts
asc2bt(input_path, output_path)
generate_tileindex(output_path)
