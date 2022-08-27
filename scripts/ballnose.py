#!/usr/bin/python
#  -*- coding: utf-8 -*-

""" Generate Ballnose Endmill tools for FreeCad Path

"""

__author__ = 'Battosai42'
__maintainer__ = 'Battosai42'
__email__ = 'git.b42@gmail.com'
__credits__ = ''
__version__ = '0.0.1'
__status__ = 'Developement'


# Basic Metric Drills [diameter, length, cutting height, chipload]
ballnose = { '1mm': [1, 50, 10, 0],
             '1.5mm': [1.5, 50, 10, 0],
             '2mm': [2, 50, 10, 0],
             '2.5mm': [2.5, 50, 10, 0],
             '3mm': [3, 50, 10, 0],
             '3.5mm': [3.5, 50, 10, 0],
             '4mm': [4, 50, 10, 0],
             }
shank_diameter = 3.0
material = 'Carbide'  # HSS or Carbide
flutes = 3

for i in ballnose.keys():
    f = open(f"../ballnose/2flute/{material}_ballmill_{i}.fctb", "w")
    f.write('{\n')
    f.write('  "version": 2,\n')
    f.write('  "name": "6mm Ball End",\n')
    f.write('  "shape": "ballend.fcstd",\n')
    f.write('  "parameter": {\n')
    f.write(f'    "Chipload": "{ballnose[i][3]} mm",\n')
    f.write(f'    "CuttingEdgeHeight": "{ballnose[i][2]} mm",\n')
    f.write(f'    "Diameter": "{ballnose[i][0]} mm",\n')
    f.write(f'    "Length": "{ballnose[i][1]} mm",\n')
    f.write(f'    "Material": "{material}",\n')
    f.write(f'    "ShankDiameter": "{shank_diameter} mm"\n')
    f.write('  },\n')
    f.write('  "attribute": {}\n')
    f.write('}\n')
    f.close()
