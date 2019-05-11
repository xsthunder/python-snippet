# see ()[https://stackoverflow.com/a/40749716]

from xml.dom.minidom import parseString

html_string = """
<!DOCTYPE html>
<html><head><title>title</title></head><body><p>test</p></body></html>
"""

# extract the text value of the document's <p> tag:
doc = parseString(html_string)
paragraph = doc.getElementsByTagName("p")[0]
content = paragraph.firstChild.data

print(content)

# This would raise an exception on common HTML entities such as &nbsp; or &reg;.
