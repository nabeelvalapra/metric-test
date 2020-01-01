import json
import xmltodict

from xml.etree import ElementTree


# Register the namespace, so it doesn't get appended with
# the tags while converting/modifiying the file.
ElementTree.register_namespace('', "urn:hl7-org:v3")

# Loads the file from existing directory
tree = ElementTree.parse('sample.xml')
root = tree.getroot()

replace_dict = {
    "{urn:hl7-org:v3}family": "Patient Family Name",
    "{urn:hl7-org:v3}given": "Patient Name",
    "{urn:hl7-org:v3}city": "Address",
    "{urn:hl7-org:v3}state": "Address",
    "{urn:hl7-org:v3}country": "Address",
    "{urn:hl7-org:v3}postalCode": "Address",
    "{urn:hl7-org:v3}streetAddressLine": "Address"

}
replace_dict_keys = replace_dict.keys()

# Recursively finds the children and replaces
# the text with replace dict
def find_replace_child_text(children=[root]):
    for child in children:
        if child.getchildren():
            find_in_child(child.getchildren())
        if child.tag in replace_dict_keys:
            child.text = replace_dict[child.tag]
find_replace_child_text(root)

# Saves the cleaned data
tree.write('out.xml')

# Convert the modified XML to text and json
text = ElementTree.tostring(root, encoding='unicode')
json_data = xmltodict.parse(text)

# Dumps the json to file.
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)