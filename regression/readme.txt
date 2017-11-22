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

training file: 
"mapred-filtered-100-metrics-training"
https://drive.google.com/open?id=15MlCCHPEjcb6YjaAd6fZhKsNFMZYz69r

regression coefficient: beta_1 ~ beta_5
[[ 1.75900845
 [ 0.25175293]
 [ 0.14534007]
 [-0.04414925]
 [ 0.51880787]]

regression intercept:
 [-5.79370162]

testing file:
"mapred-filtered-100-predict"
https://drive.google.com/open?id=1_NEUE4fYyusDF4Tlkz_SzYv-B9M9hYOx

output file:
"mapred-filtered-100-predict-with-reg"
https://drive.google.com/open?id=1_Fuo_XCQQvwnr7VVInMHPJis1uZ1N3AR

[300 rows]

trainig file:
"mapred-filtered-300-metrics-training"
https://drive.google.com/open?id=1L531-wD77NoywNoxiQ7gdK28kXx7efGK

regression coefficient: beta_1 ~ beta_5
[[ 3.24943721]
 [ 0.27913471]
 [ 0.13868265]
 [ 0.05064995]
 [ 0.39289528]] 
 
 regression intercept:
 [-11.98096962]

testing file:
"mapred-filtered-300-predict"
https://drive.google.com/open?id=1rW7ymVy7sYOEm1HquABOEqmrsTIwqm6b

output file:
"mapred-filtered-300-predict-with-reg"
https://drive.google.com/open?id=1LVyV8eZrAUTvsaC1VPYxeJxPyeLkgHM7
