import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.util.ArrayList;

public class prepro 
{
	static ArrayList<String> stopWords = new ArrayList<String>();
	
	public static void main(String[] args) throws FileNotFoundException, IOException
	{
		
//		PrintStream out = new PrintStream(new FileOutputStream("src/Result.csv"));
//		System.setOut(out);

		PrintWriter pw = new PrintWriter(new File("src/Result.csv"));
		try(BufferedReader br2 = new BufferedReader(new FileReader("src/stopword.txt")))
		{
			for(String line; (line = br2.readLine())!= null;)
			{
				stopWords.add(line);
			}
		}
		try(BufferedReader br = new BufferedReader(new FileReader("src/Reviews.csv")))
		{
			for(String line; (line = br.readLine())!= null;)
			{
				String[] temp = line.split(",");
				String comment = "";
				String rating = "";
				int count = 0;
				String summary = "";
				for(int j = 0 ; j < temp.length ; j++)
				{
					if(temp[j].matches("[0-9]+") && count < 4)
					{
						count++;
					}
					else
					if(temp[j].matches("[0-9]+") && count == 4)
					{
						rating = temp[j-1];

						summary = temp[j+1];
						for(int i = (j+2) ; i < temp.length ; i++)
						{
							comment += temp[i] + " ";
						}
						
						break;
					}
				}
				pw.println(rating + "," + summary + "," + removeStop(comment.replaceAll("[^a-zA-Z ]", "").toLowerCase()));
				//System.out.println(temp[0] + "," + rating + "," + summary + "," + removeStop(comment.replaceAll("[^a-zA-Z ]", "").toLowerCase()));
			}
			System.out.println("Done");
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
