import xml.etree.ElementTree as etree

tree=etree.parse('/vagrant/efu_dump1.xml')
for response in tree.getroot().findall('.//FDOServiceResponse'):
    for output in response.findall('.//Output'):
        if output.get('name')=='ParsedResponse':
            for name in output.findall('.//NameOrAlias'):
                print name.get('FirstName')
                print name.get('MiddleName')
                print name.get('LastName')
            for id in output.findall('.//Identification'):
                print id.get('SubjectSsn')
                print id.get('SubjectDateOfBirth')
                print id.get('SubjectAge')
            for addr in output.findall('.//Address'):
                print  addr.get('ZipCode')
        
    





