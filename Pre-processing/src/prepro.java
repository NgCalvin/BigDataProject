import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;
import java.util.ArrayList;

public class prepro 
{
	static ArrayList<String> stopWords = new ArrayList<String>();
	
	public static void main(String[] args) throws FileNotFoundException, IOException
	{
		
		PrintStream out = new PrintStream(new FileOutputStream("Result.csv"));
		System.setOut(out);

		try(BufferedReader br = new BufferedReader(new FileReader("stopword.txt")))
		{
			for(String line; (line = br.readLine())!= null;)
			{
				stopWords.add(line);
			}
		}
		try(BufferedReader br = new BufferedReader(new FileReader("Reviews.csv")))
		{
			for(String line; (line = br.readLine())!= null;)
			{
				String[] temp = line.split(",");
				String comment = "";
				for(int i = 9 ; i < temp.length ; i++)
				{
					comment += temp[i] + " ";
				}
				String removeStop = removeStop(comment.replaceAll("[^a-zA-Z ]", "").toLowerCase());
				String result = temp[6] + "," + temp[8] + "," + removeStop;		
				System.out.println(result);
			}
		}
	}
	
	public static String removeStop(String line)
	{
		String[] temp = line.split(" ");
		String result = "";
		for(int i = 0; i < temp.length ; i++)
		{
			for(int j = 0 ; j < stopWords.size() ; j++)
			{
				if(temp[i].equals(stopWords.get(j)))
				{
					temp[i] = null;
					break;
				}
			}
			if(i!=temp.length-1 && temp[i] != null)
			{
				result += temp[i] + " "; 
			}
			else if(temp[i] != null)
			{
				result += temp[i];
			}
		}
		return result;
	}
}
