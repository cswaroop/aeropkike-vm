from __future__ import print_function

import xml.etree.ElementTree as etree
import aerospike
import sys

from optparse import OptionParser

################################################################################
# Option Parsing
################################################################################

usage = "usage: %prog [options] key"

optparser = OptionParser(usage=usage, add_help_option=False)

optparser.add_option(
    "--help", dest="help", action="store_true",
    help="Displays this message.")

optparser.add_option(
    "-U", "--username", dest="username", type="string", metavar="<USERNAME>",
    help="Username to connect to database.")

optparser.add_option(
    "-P", "--password", dest="password", type="string", metavar="<PASSWORD>",
    help="Password to connect to database.")

optparser.add_option(
    "-h", "--host", dest="host", type="string", default="127.0.0.1", metavar="<ADDRESS>",
    help="Address of Aerospike server.")

optparser.add_option(
    "-p", "--port", dest="port", type="int", default=3000, metavar="<PORT>",
    help="Port of the Aerospike server.")

optparser.add_option(
    "-n", "--namespace", dest="namespace", type="string", default="test", metavar="<NS>",
    help="Port of the Aerospike server.")

optparser.add_option(
    "-s", "--set", dest="set", type="string", default="demo", metavar="<SET>",
    help="Port of the Aerospike server.")

optparser.add_option(
    "--gen", dest="gen", type="int", default=5, metavar="<GEN>",
    help="Generation of the record being written.")

optparser.add_option(
    "--ttl", dest="ttl", type="int", default=1000, metavar="<TTL>",
    help="TTL of the record being written.")


(options, args) = optparser.parse_args()

if options.help:
    optparser.print_help()
    print()
    sys.exit(1)

if len(args) != 1:
    optparser.print_help()
    print()
    sys.exit(1)

################################################################################
# Client Configuration
################################################################################

config = {
    'hosts': [ (options.host, options.port) ]
}

################################################################################
# Application
################################################################################

exitCode = 0

try:

    # ----------------------------------------------------------------------------
    # Connect to Cluster
    # ----------------------------------------------------------------------------

    client = aerospike.client(config).connect(options.username, options.password)

    # ----------------------------------------------------------------------------
    # Perform Operation
    # ----------------------------------------------------------------------------

    try:

        namespace = options.namespace if options.namespace and options.namespace != 'None' else None
        set = options.set if options.set and options.set != 'None' else None

        data = ''
        with open ("/vagrant/efu_dump1.xml", "r") as myfile:
            data=myfile.read().replace('\n', '')

        for i in range(1,50000):
            r = {}
            r['FirstName'] = 'FirstName'+ `i`
            r['LastName'] =  'LastName' + `i`
            r['Ssn'] = 'Ssn' + `i`
            r['Dob'] = 'Dob' + `i`
            r['Age'] =  i
            r['ZipCode'] = 'Zip'+ `i`
        
        # tree=etree.parse('/vagrant/efu_dump1.xml')
        # for response in tree.getroot().findall('.//FDOServiceResponse'):
        #     for output in response.findall('.//Output'):
        #         if output.get('name')=='ParsedResponse':
        #             for name in output.findall('.//NameOrAlias'):
        #                 r['FirstName'] = name.get('FirstName')
        #                 r['MiddleName'] = name.get('MiddleName')
        #                 r['LastName'] =  name.get('LastName')
        #             for id in output.findall('.//Identification'):
        #                 r['Ssn'] = id.get('SubjectSsn')
        #                 r['Dob'] = id.get('SubjectDateOfBirth')
        #                 r['Age'] = id.get('Age')
        #             for addr in output.findall('.//Address'):
        #                 r['ZipCode'] = addr.get('ZipCode')
            r['BureauData'] =  data
            key = r['FirstName']+r['LastName']+r['Ssn']+r['Dob']+r['ZipCode']
            meta = {'ttl': options.ttl, 'gen': options.gen}
            policy = None

            # invoke operation
            client.put((namespace, set, key), r, meta, policy)
            
            print(r)
            print("---")
            print("OK, 1 record written.")
            
    except Exception as e:
        print("error: {0}".format(e), file=sys.stderr)
        exitCode = 2

    # ----------------------------------------------------------------------------
    # Close Connection to Cluster
    # ----------------------------------------------------------------------------

    client.close()

except Exception, eargs:
    print("error: {0}".format(eargs), file=sys.stderr)
    exitCode = 3

################################################################################
# Exit
################################################################################

sys.exit(exitCode)
