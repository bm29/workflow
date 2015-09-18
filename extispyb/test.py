from xml.dom import minidom
import xml.etree.ElementTree as etree

xmldoc = minidom.parse('/users/opd29/passerelle-edm/scripts/extispyb/test.xml')
itemlist = xmldoc.getElementsByTagName('blob')


varnames = [
    ('path/value', 'lat')
    ]

points = []
for pointelem in itemlist:
    point = {}
    for tag, varname in varnames:
        point[varname] = pointelem.find(tag).text
    points.append(point)

import pprint
pprint.pprint(points)

