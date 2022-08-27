#!/usr/bin/python
#  -*- coding: utf-8 -*-

""" Generate Endmill tools for FreeCad Path

"""

__author__ = 'Battosai42'
__maintainer__ = 'Battosai42'
__email__ = 'git.b42@gmail.com'
__credits__ = ''
__version__ = '0.0.1'
__status__ = 'Developement'


# Basic Metric Drills [diameter, cutting lengh, tool lengh, chipload]
endmills_metric = { '1mm': [1, 10, 50, 0],
                    '1.5mm': [1.5, 18, 50, 0],
                    '2mm': [2, 24, 50, 0],
                    '2.5mm': [2.5, 27, 50, 0],
                    '3mm': [3, 34, 50, 0],
                    '3.5mm': [3.5, 34, 50, 0],
                    '4mm': [4, 36, 50, 0],
                    }
shank_diameter = 3.0
material = 'Carbide'  # HSS or Carbide

for i in endmills_metric.keys():
    f = open(f"../endmills/1flute/{material}_endmill_{i}.fctb", "w")
    f.write('{\n')
    f.write('  "version": 2,\n')
    f.write(f'  "name": "endmill_{endmills_metric[i][0]}",\n')
    f.write('  "shape": "endmill.fcstd",\n')
    f.write('  "parameter": {\n')
    f.write(f'    "Chipload": "{endmills_metric[i][3]} mm",\n')
    f.write(f'    "CuttingEdgeHeight": "{endmills_metric[i][1]}",\n')
    f.write(f'    "Diameter": "{endmills_metric[i][0]} mm",\n')
    f.write('    "Flutes": "1",\n')
    f.write(f'    "Length": "{endmills_metric[i][2]} mm",\n')
    f.write(f'    "Material": "{material}",\n')
    f.write(f'    "ShankDiameter": "{shank_diameter} mm",\n')
    f.write('    "SpindleDirection": "Forward"\n')
    f.write('  },\n')
    f.write('  "attribute": {}\n')
    f.write('}\n')
    f.close()

for i in endmills_metric.keys():
    f = open(f"../endmills/2flute/carbide_endmill_{i}.fctb", "w")
    f.write('{\n')
    f.write('  "version": 2,\n')
    f.write(f'  "name": "endmill_{endmills_metric[i][0]}",\n')
    f.write('  "shape": "D:/tools/FreeCad/FreeCAD 0.20/Mod\\\\Path\\\\Tools\\\\Shape\\\\endmill.fcstd",\n')
    f.write('  "parameter": {\n')
    f.write('    "Chipload": "0.00 mm",\n')
    f.write('    "CuttingEdgeHeight": "10.00 mm",\n')
    f.write(f'    "Diameter": "{endmills_metric[i][0]} mm",\n')
    f.write('    "Flutes": "2",\n')
    f.write('    "Length": "50.00 mm",\n')
    f.write('    "Material": "Carbide",\n')
    f.write(f'    "ShankDiameter": "{shank_diameter} mm",\n')
    f.write('    "SpindleDirection": "Forward"\n')
    f.write('  },\n')
    f.write('  "attribute": {}\n')
    f.write('}\n')
    f.close()

for i in endmills_metric.keys():
    f = open(f"../endmills/3flute/carbide_endmill_{i}.fctb", "w")
    f.write('{\n')
    f.write('  "version": 2,\n')
    f.write(f'  "name": "endmill_{endmills_metric[i][0]}",\n')
    f.write('  "shape": "D:/tools/FreeCad/FreeCAD 0.20/Mod\\\\Path\\\\Tools\\\\Shape\\\\endmill.fcstd",\n')
    f.write('  "parameter": {\n')
    f.write('    "Chipload": "0.00 mm",\n')
    f.write('    "CuttingEdgeHeight": "10.00 mm",\n')
    f.write(f'    "Diameter": "{endmills_metric[i][0]} mm",\n')
    f.write('    "Flutes": "4",\n')
    f.write('    "Length": "50.00 mm",\n')
    f.write('    "Material": "Carbide",\n')
    f.write(f'    "ShankDiameter": "{shank_diameter} mm",\n')
    f.write('    "SpindleDirection": "Forward"\n')
    f.write('  },\n')
    f.write('  "attribute": {}\n')
    f.write('}\n')
    f.close()

for i in endmills_metric.keys():
    f = open(f"../endmills/4flute/carbide_endmill_{i}.fctb", "w")
    f.write('{\n')
    f.write('  "version": 2,\n')
    f.write(f'  "name": "endmill_{endmills_metric[i][0]}",\n')
    f.write('  "shape": "D:/tools/FreeCad/FreeCAD 0.20/Mod\\\\Path\\\\Tools\\\\Shape\\\\endmill.fcstd",\n')
    f.write('  "parameter": {\n')
    f.write('    "Chipload": "0.00 mm",\n')
    f.write('    "CuttingEdgeHeight": "10.00 mm",\n')
    f.write(f'    "Diameter": "{endmills_metric[i][0]} mm",\n')
    f.write('    "Flutes": "4",\n')
    f.write('    "Length": "50.00 mm",\n')
    f.write('    "Material": "Carbide",\n')
    f.write(f'    "ShankDiameter": "{shank_diameter} mm",\n')
    f.write('    "SpindleDirection": "Forward"\n')
    f.write('  },\n')
    f.write('  "attribute": {}\n')
    f.write('}\n')
    f.close()