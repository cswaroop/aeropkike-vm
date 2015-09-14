package testxml;


import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;


public class testxml {
	static JavaSparkContext sc ; 	
	
		public static void main(String args[])
		{
			SparkConf conf = new SparkConf().setAppName("sud").setMaster("local");
			sc= new JavaSparkContext(conf);
			
			//LOAD The data and store in file system later move to hadoop or HIVE
			
			
			JavaRDD<String> textFile = sc.textFile("C:\\Sudhindra\\hackathon\\efu_dump_400mb.xml",8);
			//we need to build a key here 
			
			//GET
			//long starttime= System.currentTimeMillis();
			//JavaRDD<String> get = textFile.map(new XMLFunction("//NameOrAliasList/NameOrAlias[@LastName='CONSUMER1']/@FirstName"));
			JavaRDD<String> get = textFile.map(new XMLFunction("//Identification[@SubjectAge>52]/@SubjectSsn"));
			
		//	long endTime= System.currentTimeMillis();
		//System.out.println(endTime-starttime);
			System.out.println(get.collect());
		//	System.out.println(get.count());
			sc.stop();
			
			
			//PUT MEthod 
			//JavaRDD<String> addText = sc.textFile("C:\\Sudhindra\\hackathon\\equifax.xml");
				
			
		}
}
