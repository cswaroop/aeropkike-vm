How to setup?
=============

Setup the Aerospike (

1. Install Vagrant
2. run `vagrant up` in current directory
3. run the put.py to load 50000 bureau records
4. Run some adhoc queries to test the loaded data in aerospike (refer AeroSpike Commands.txt)

Run the Spark

1.Install Apache Spark on your local machine
2. spark-submit --driver-memory 12 g --class testxml.testxml --master local[8] c:\softwares\textxml.jar 1000
