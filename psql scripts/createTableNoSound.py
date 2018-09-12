import psycopg2, csv, sys


conn = psycopg2.connect (database="cwcdb", user="root", password="cwc", host="localhost", port="5432")
c = conn.cursor()

# psql = 'DROP TABLE IF EXISTS pcount_no_sound';
c.execute("DROP TABLE IF EXISTS participant_count_no_sound")

c.execute("""CREATE TABLE participant_count_no_sound
	 (
		 id INTEGER,
		 label text,
		 no_sound_count CHAR(20),
		 participant_count CHAR(20)
		 /*with_sound_count CHAR(30)
		 end_frame CHAR(30),
		 start_timestamp CHAR(30),
		 end_timestamp CHAR(30),
		 duration CHAR(30),
		 start_frame_timestamp CHAR(30),
		 end_frame_timestamp CHAR(30),
		 label CHAR(100)*/
		 
	 )
 """) 

# csv_data = csv.reader(file("frametable.csv"))
i = 1;
with open('participant_count_no_sound.csv') as tsv:
	csv_data = csv.reader(tsv, delimiter=',') ## converted tsv to csv??? IMP line

	next(csv_data, None) #skip the header row from csv file without deleting it
	for row in csv_data:
		print row
		print "----------------------------"
		print i
		
 		# c.execute("INSERT INTO pcount_no_sound (project, session_name, file_name, start_frame, end_frame, start_timestamp, end_timestamp, duration, start_frame_timestamp, end_frame_timestamp, label) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
 		c.execute("INSERT INTO participant_count_no_sound (id, label, no_sound_count, participant_count) VALUES ('%s', '%s', '%s', '%s')"%(i, row[0],row[1],row[2]))
 		# if (i == 100) :
			# break;
		i +=1;

	conn.commit()
c.close()


'''

c.execute("DROP TABLE IF EXISTS blog_gestures")
c.execute("""CREATE TABLE blog_gestures
 (
 id INTEGER,
 gesture CHAR(100),
 count INTEGER
 )
 """) 

#filename = 'all_gestures_with_sound.txt'
filename = 'a.txt'

id_count = 1
with open(filename, 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	for row in reader:
		if (int(row[1]) == 0):
			zero+= 1
		else:	
			c.execute("INSERT INTO blog_gestures (id , gesture, count) VALUES ('%d', '%s', '%d')"%(id_count, row[0],int(row[1])))
			id_count += 1

print "%d rows were inserted" % (id_count-1)
conn.commit()
c.close()
'''
