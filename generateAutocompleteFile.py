import re
my_file = open('east.xsd', 'r') 
Lines = my_file.readlines() 
  
res = []
for line in Lines: 
    matches = re.findall('<xs:element(.*?) name="(.+?)"(.*?)>', line, re.DOTALL)
    if len(matches) > 0:
        res += [x[1] for x in matches]

content = \
"""<?xml version="1.0" encoding="Windows-1252" ?>
<NotepadPlus>
    <AutoComplete>\n"""

for element in res :
    content += f"       <KeyWord name=\"{element}\" />\n"

content += """  </AutoComplete>\n"""
content += """</NotepadPlus>"""

my_file= open('autocomplete/east.xml', 'w') 
my_file.write(content)