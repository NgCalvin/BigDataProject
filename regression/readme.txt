these files focus on running Regression part

'main_regress.py' runs both (1) training and (2)prediction steps.

(1) training step:
input: training data with 'Score' and  'Predictor 0~5 score'
output: regression coefficients [don't forget the intercept]

(2) prediction step:
input: test data with 'Predictor 0~5 score'
output: append a new col 'reg_score'

N.B.
the "reg_score" might be out of the 1~5 score range.
it is fine and we can still report the mean square error to compare the performance

##########################################################################

The following is the input and result file:

[100 rows]

regression coefficient: intercept, beta_1 ~ beta_5

-5.79370162
1.75900845
0.25175293
0.14534007
-0.04414925
0.51880787

training file: mapred-filtered-100-metrics.csv
https://storage.googleapis.com/cmsc-5741-project-data/mapred-filtered-100-metrics.csv

testing file: mapred-filtered-100-test.csv
https://storage.googleapis.com/cmsc-5741-project-data/mapred-filtered-100-test.csv

output file: mapred-filtered-100-regress-test.csv
https://storage.googleapis.com/cmsc-5741-project-data/mapred-filtered-100-regress-test.csv



[300 rows]

regression coefficient: intercept, beta_1 ~ beta_5

-11.98096962
3.24943721
0.27913471
0.13868265
0.05064995
0.39289528

training file: mapred-filtered-300-metrics.csv
https://storage.googleapis.com/cmsc-5741-project-data/mapred-filtered-300-metrics.csv

testing file: mapred-filtered-300-test.csv
https://storage.googleapis.com/cmsc-5741-project-data/mapred-filtered-300-test.csv

output file: mapred-filtered-300-regress-test.csv
https://storage.googleapis.com/cmsc-5741-project-data/mapred-filtered-300-regress-test.csv
