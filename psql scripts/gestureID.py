import csv, sys


## SEARCH KEYWORD ------------------------>
## MAKE sure that keyword[0] is same as the name of output file

#keyword = ["Unknown", "unknown"]

#keyword = ["RH", "rh", "Rh", "rH"]
#keyword = ["LH", "lh", "Lh", "lH"]
#keyword = ["hands", "Hands", "hand", "Hand"]

#keyword = ["RA", "ra", "Ra", "rA"]
#keyword = ["LA", "la", "La", "lA"]
#keyword = ["arms", "Arms", "arm", "Arm"]

#keyword = ["head", "Head"]

#keyword = ["body"]


#keyword = ["CWC - With Sound"]
keyword = ["CWC - No Sound", "CWC - With Sound"]
## =========================================
print keyword

i = 0;
rowNumber = 0; 
test = False;

with open('Labels (copy).csv', 'r') as tsv , open("gestureID_3s.csv", 'wb') as writefile :
	csv_data = csv.reader(tsv, delimiter='\t') ## converted tsv to csv??? IMP line
	csv_writer = csv.writer(writefile)

	header = csv_data.next()
	print header

	#header_new = ['GestureID', header[10], 'Session', 'Participant', 'Block', header[2], header[3], header[4], header[5], header[6], header[7], header[8], header[9]]
	header_new = ['GestureID', header[10], header[0], header[1], 'Session', 'Participant', 'Block', header[2], header[3], header[4], header[5], header[6], 'Duration', header[8], header[9]]
	print header_new
	csv_writer.writerow(header_new)

	next(csv_data, None) #skip the header row from csv file without deleting it
	##for num, row in enumerate(csv_data):
	for row in csv_data:
		rowNumber += 1;
		## print row[10]

		## To account for uppercase lowercase differences
		test = False ## IMPORTANT
		for word in keyword:
			test = test or (word in row[0])
			## print test

		if test : ## if test is true  // search in row 0 for keyword
			#print "FOUND --------------------------------" 
			
			# change format before writing
			sessionName = row[1]
			row[1:2] = row[1].split('-')
			#print row
			row_new = [rowNumber, row[12], row[0], sessionName, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]]

			csv_writer.writerow(row_new)
			##print row[10]
			#print row[9]
			i += 1
			##print rowNumber , " <------ found here"

 		##c.execute("INSERT INTO frame_table (project, session_name, file_name, start_frame, end_frame, start_timestamp, end_timestamp, duration, start_frame_timestamp, end_frame_timestamp, label) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '{%s}')"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
 		
 	print row
 	print i , " <---------- total finds"
	##conn.commit()
##c.close()
