#!/usr/bin/python
#  -*- coding: utf-8 -*-

""" Generate Bullnose Endmill tools for FreeCad Path

"""

__author__ = 'Battosai42'
__maintainer__ = 'Battosai42'
__email__ = 'git.b42@gmail.com'
__credits__ = ''
__version__ = '0.0.1'
__status__ = 'Developement'


# Basic Metric Drills [diameter, radius, cutting lengh, tool lengh, chipload]
bullnose = { '1mm': [1, 0.5, 10, 50, 0],
                    '1.5mm': [1.5, 0.75, 18, 50, 0],
                    '2mm': [2, 1.0, 24, 50, 0],
                    '2.5mm': [2.5, 1.25, 27, 50, 0],
                    '3mm': [3, 1.5, 34, 50, 0],
                    '3.5mm': [3.5, 1.75, 34, 50, 0],
                    '4mm': [4, 2.0, 36, 50, 0],
                    }

shank_diameter = 3.0
material = 'HSS'  # HSS or Carbide
flutes = 2

for i in bullnose.keys():
    f = open(f"../bullnose/2flute/{material}_bullmill_{i}.fctb", "w")
    f.write('{\n')
    f.write('  "version": 2,\n')
    f.write('  "name": "6 mm Bull Nose",\n')
    f.write('  "shape": "bullnose.fcstd",\n')
    f.write('  "parameter": {\n')
    f.write(f'    "Chipload": "0.0 mm",\n')
    f.write(f'    "CuttingEdgeHeight": "{bullnose[i][2]} mm",\n')
    f.write(f'    "Diameter": "{bullnose[i][0]} mm",\n')
    f.write(f'    "FlatRadius": "{bullnose[i][1]} mm",\n')
    f.write(f'    "Length": "{bullnose[i][3]} mm",\n')
    f.write(f'    "Material": "{material}",\n')
    f.write(f'    "ShankDiameter": "{shank_diameter} mm"\n')
    f.write('  },\n')
    f.write('  "attribute": {}\n')
    f.write('}\n')
    f.close()
