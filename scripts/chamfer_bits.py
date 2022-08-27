#!/usr/bin/python
#  -*- coding: utf-8 -*-

""" Generate Chamfer Bit tools for FreeCad Path

"""

__author__ = 'Battosai42'
__maintainer__ = 'Battosai42'
__email__ = 'git.b42@gmail.com'
__credits__ = ''
__version__ = '0.0.1'
__status__ = 'Developement'


# Basic Metric Drills [diameter, shank diameter, cutting height, tool lengh, tip diameter]
chamfer = {'6.3mm': [6.3, 5, 2.5, 45, 1.5],
           '8.3mm': [8.3, 6, 3.5, 49, 2],
           '10.4mm': [10.4, 7, 4.5, 49, 2],
           '12.4mm': [12.4, 8, 5, 56, 2],
           '16.5mm': [16.5, 10, 7, 63, 2],
           '20.5mm': [20.5, 10, 9, 65, 2]
           }

angle = 45
material = 'HSS'  # HSS or Carbide
flutes = 3

for i in chamfer.keys():
    f = open(f"../chamfer-bits/45deg/{material}_chamfer_{i}.fctb", "w")
    f.write('{\n')
    f.write('  "version": 2,\n')
    f.write(f'  "name": "{angle} Deg. Chamfer {i}",\n')
    f.write('  "shape": "chamfer.fcstd",\n')
    f.write('  "parameter": {\n')
    f.write(f'    "Chipload": "0.0 mm",\n')
    f.write(f'    "CuttingEdgeAngle": "{angle} \\u00b0",\n')
    f.write(f'    "CuttingEdgeHeight": "{chamfer[i][2]} mm",\n')
    f.write(f'    "Diameter": "{chamfer[i][0]} mm",\n')
    f.write(f'    "Flutes": "{flutes}",\n')
    f.write(f'    "Length": "{chamfer[i][3]} mm",\n')
    f.write(f'    "Material": "{material}",\n')
    f.write(f'    "ShankDiameter": "{chamfer[i][1]} mm",\n')
    f.write(f'    "TipDiameter": "{chamfer[i][4]} mm"\n')
    f.write('  },\n')
    f.write('  "attribute": {}\n')
    f.write('}\n')

    f.close()
