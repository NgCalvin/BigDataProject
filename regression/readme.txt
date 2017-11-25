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

##############################################################################
<Re-run using top_max = 100>

<Preprocess Stage>
[stopword list]
Add to stopword list:
br

Remove from stopword list: 
but	
most	
least	
never	
only	
ever	
still	
although
though
yet
very

The "br" is the break line command in Text.
This was not removed before.

Train Data:
preprocessed_70.csv
https://drive.google.com/open?id=1engP7OQkgF65BYuiUW0zFcO5HfDpM_9y

Test Data:
preprocessed_30.csv
https://drive.google.com/open?id=1FezHsMEcQEvLjuTiRAP_qcccGgNTmJBH

<Filtering Stage>
filter_top_100.csv
https://drive.google.com/open?id=1zutpxAdNew79epttFgdsRu2l6V5cK60S

<Prediction Stage>
Predict using score 3 as default score
predict_30_3_with_reg.csv
https://drive.google.com/open?id=11MhxKk_J36CvkDQ22nPXaL8yPkV5h8WY

Predict using train data mean as default score
predict_30_train_mean_with_reg.csv
https://drive.google.com/open?id=1emQ2jPqObuApR2QgVvLIbFT7KD8bmj3Z
