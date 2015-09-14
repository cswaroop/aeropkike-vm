package testxml;

import java.io.StringReader;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPathFactory;

import org.apache.spark.api.java.function.Function;
import org.w3c.dom.Document;
import org.xml.sax.InputSource;

public class XMLFunction implements Function<String, String> {

	/**
	 * 
	 */
	private static final long serialVersionUID = -2382095604414613482L;
	String xpath;

	public XMLFunction(String xpath) {
		this.xpath = xpath;
	}

	@Override
	public String call(String s) throws Exception {

		//System.out.println(s);
		DocumentBuilder dBuilder = null;
		Document doc = null;
		InputSource source = new InputSource(new StringReader(s));

		try {
			dBuilder = DocumentBuilderFactory.newInstance()
					.newDocumentBuilder();

			doc = dBuilder.parse(source);

			if ("" == XPathFactory
					.newInstance()
					.newXPath()
					.compile(xpath)
					.evaluate(doc))
				return null;
			else
				return s;
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}

}
