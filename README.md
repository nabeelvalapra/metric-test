# Instructions
1. Pull the repo. 
2. Create a virtualenv with python3.6 
3. `pip install xmltodict`
4. Place the sample.json file inside the folder
3. `python main.py`
6. Please check the data.json and new.xml

## Task

1. In the given xml, remove all the personal information related to a patient. For example the tag patient contains the name and family name of the patient. Find all the occurrences and replace it with the text "patient name" and "patient family name". 
Eg:
```
<patient>
                <name>
                    <family>Doe</family>
                    <given>John</given>
                    <given>John</given>
                </name>
                <administrativeGenderCode code="F" codeSystem="2.16.840.1.113883.5.1" />
                <birthTime value="19781221" />
                <raceCode nullFlavor="NI" />
                <ethnicGroupCode nullFlavor="NI" />
                <languageCommunication>
                    <languageCode code="en" />
                    <preferenceInd value="false" />
                </languageCommunication>
</patient>
```
The above snippet after processing should be like the snippet below
```
<patient>
                <name>
                    <family>Patient Family Name</family>
                    <given>Patient Name</given>
                    <given>Patient Name</given>
                </name>
                <administrativeGenderCode code="F" codeSystem="2.16.840.1.113883.5.1" />
                <birthTime value="19781221" />
                <raceCode nullFlavor="NI" />
                <ethnicGroupCode nullFlavor="NI" />
                <languageCommunication>
                    <languageCode code="en" />
                    <preferenceInd value="false" />
                </languageCommunication>
</patient>
```
Also find all the occurrences of addresses in the file and replace it with the text "address".

2. Convert the given xml to json without any data lose.
