import json
import xmltodict

from xml.etree import ElementTree


# Register the namespace, so it doesn't get appended with
# the tags while converting/modifiying the file.
ElementTree.register_namespace('', "urn:hl7-org:v3")

# Loads the file from existing directory
tree = ElementTree.parse('sample.xml')
root = tree.getroot()

ns = {'xmlns': "urn:hl7-org:v3"}
path = './xmlns:recordTarget/xmlns:patientRole/xmlns:patient/'

for ele in root.find(path, namespaces=ns):
    if 'family' in ele.tag:
        ele.text = "Patient Family Name"
    if 'given' in ele.tag:
        ele.text = "Family Name"

# Convert the modified XML to text and json
text = ElementTree.tostring(root, encoding='unicode')
json_data = xmltodict.parse(text)

# Dumps the json to file.
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)