#!/usr/bin/python
#  -*- coding: utf-8 -*-

""" Generate Drill tools for FreeCad Path

"""

__author__ = 'Battosai42'
__maintainer__ = 'Battosai42'
__email__ = 'git.b42@gmail.com'
__credits__ = ''
__version__ = '0.0.1'
__status__ = 'Developement'

material = 'Carbide'  # HSS or Carbide

# Basic Metric Drills
drills = {'1mm': [1, 10],
          '1.5mm': [1.5, 18],
          '2mm': [2, 24],
          '2.5mm': [2.5, 27],
          '3mm': [3, 34],
          '3.5mm': [3.5, 34],
          '4mm': [4, 36],
          '4.5mm': [4.5, 38],
          '5mm': [5, 43],
          '5.5mm': [5.5, 43],
          '6mm': [6, 46],
          '6.5mm': [6.5, 46],
          '7mm': [7, 50],
          '7.5mm': [7.5, 50],
          '8mm': [8, 60],
          '8.5mm': [8.5, 60],
          '9mm': [9, 62],
          '9.5mm': [9.5, 62],
          '10mm': [10, 70]}
for i in drills.keys():
    f = open(f"../drills/hss_drill_{i}.fctb", "w")
    f.write("{\n")
    f.write('  "version": 2,\n')
    f.write(f'  "name": "hss_drill_{i}",\n')
    f.write('  "shape": "drill.fcstd",\n')
    f.write('  "parameter": {\n')
    f.write('    "Chipload": "0.00 mm",\n')
    f.write(f'    "Diameter": "{drills[i][0]} mm",\n')
    f.write('    "Flutes": "2",\n')
    f.write(f'    "Length": "{drills[i][1]} mm",\n')
    f.write(f'    "Material": "{material}",\n')
    f.write('    "TipAngle": "119.00 \\u00b0"\n')
    f.write('  },\n')
    f.write('  "attribute": {}\n')
    f.write("}\n")
    f.close()

# Metric Threads
drills_threads = {'M1': [0.75, 10],
                  'M1.2': [0.95, 10],
                  'M1.6': [1.25, 18],
                  'M2': [1.6, 24],
                  'M2.5': [2.05, 27],
                  'M3': [2.5, 34],
                  'M4': [3.3, 36],
                  'M5': [4.2, 36],
                  'M6': [5.0, 46],
                  'M8': [6.8, 46],
                  'M10': [8.5, 60],
                  'M12': [10.2, 70]}
for i in drills_threads.keys():
    f = open(f"../drills/hss_core_drill_{i}.fctb", "w")
    f.write("{\n")
    f.write('  "version": 2,\n')
    f.write(f'  "name": "hss_drill_{i}",\n')
    f.write('  "shape": "D:/tools/FreeCad/FreeCAD 0.20/Mod\\\\Path\\\\Tools\\\\Shape\\\\drill.fcstd",\n')
    f.write('  "parameter": {\n')
    f.write('    "Chipload": "0.00 mm",\n')
    f.write(f'    "Diameter": "{drills_threads[i][0]} mm",\n')
    f.write('    "Flutes": "2",\n')
    f.write(f'    "Length": "{drills_threads[i][1]} mm",\n')
    f.write(f'    "Material": "{material}",\n')
    f.write('    "TipAngle": "119.00 \\u00b0"\n')
    f.write('  },\n')
    f.write('  "attribute": {}\n')
    f.write("}\n")
    f.close()