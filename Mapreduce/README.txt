Place result.csv inside this folder.
The map reduce count the frequency of words for each score (and each k-length)
To run the mapreduce, you can:
1) run python main.py in command line, or
2) execute the whole main.py in python interpreter and change the directory in sys.path.append if necessary

#########################################
Hadoop Mapreduce version
[mapper_for_hadoop.py]
INPUT: processed csv - <score>,<text>
OUTPUT: <score>#<k>#<k-shingle>tab<1>

[reducer_for_hadoop.py]
OUTPUT: <score>#<k>#<k-shingle>#<count>
