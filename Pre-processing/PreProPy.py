import re
import csv
class PrePro:

def process(line):
	#First read the stopwords from stopwords.txt.
	stopwords = []
   	with open('stopword.txt', newline='') as myFile:  
        reader = csv.reader(myFile)
        for row in reader:
        	stopwords.append(row)

            
	#Input line is set to lower case and using regex, line will only left with any charater, any integer, space and comma

	regex = r"[^a-zA-Z0-9 ,]+"
	substr = ""
	temp = re.sub(regex,substr,line.lower(),0)

	#Stripping the line into list using comma.
	tempList = [x.strip() for x in temp.split(',')]

	#Location where the slot is numerical. i.e. use to find the rating slot , summary slot and comment slot.
	location = [i for i,x in enumerate(tempList) if x.isdigit()]

	comment = [];
	#Loop the item in the sub List in the comment section and remove stopword
	for item in tempList[(location[3]+3):]:
		check = item.split(' ')
		for word in check:
			if word in stopwords:
				continue
			else:
				comment.append(word)
		


	#First part is score, second part is summary , last part is comment.
	result = str(tempList[location[3]]) + "," + str(tempList[(location[3]+2)]) + "," + " ".join(str(x) for x in comment)

	return result