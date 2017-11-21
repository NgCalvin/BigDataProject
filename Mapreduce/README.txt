Place result.csv inside this folder.
The map reduce count the frequency of words for each score (and each k-length)
To run the mapreduce, you can:
1) run python main.py in command line, or
2) execute the whole main.py in python interpreter and change the directory in sys.path.append if necessary

#########################################
<Hadoop Mapreduce version>
[mapper_for_hadoop.py]
INPUT: processed csv - <score>,<text>
OUTPUT: <score>#<k>#<k-shingle>tab<1>

[reducer_for_hadoop.py]
This step ignores shingles that only appears once, i.e. count==1
This dracstically reduced the output from 1GB to 188MB
OUTPUT: <score>#<k>#<k-shingle>#<count>
sample output file: part-00000_trial2
########################################
<Filtering>
run "main_filtering.py"
and it is running "filtering.py"
output filtered.csv with header = score, k, frequency, shingle
########################################
<Regression>
There are two steps: (1) to training the regression coeff and (2) using the regression coeff to predict

[Training step - regression_training.py]
Using the 70% data >>> with Predictors <<< to train the regression coeff

[Prediction step - regression_predict.py]
using the regression coeff with Predictors to get the prediction

