import re
file1 = open('east.xsd', 'r') 
Lines = file1.readlines() 
  
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
print(content)