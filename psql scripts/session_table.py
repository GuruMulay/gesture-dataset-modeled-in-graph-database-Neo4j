import psycopg2, csv, sys

conn = psycopg2.connect (database="cwcdb", user="root", password="cwc", host="localhost", port="5432")
c = conn.cursor()
print "------------ ----=="
# psql = 'DROP TABLE IF EXISTS frame_table';
c.execute("DROP TABLE IF EXISTS session_table")

c.execute("""CREATE TABLE session_table
	 (
		 SessionID INTEGER,
		 SessionName CHAR(50),
		 Project CHAR(30),
		 Session CHAR(15),
		 Participant CHAR(15),
		 Block CHAR(15),
		 FileName CHAR(50)
	 )
 """) 

i = 1;
j = 1;
print "------------"
with open('sessionTable.csv') as tsv:
	csv_data = csv.reader(tsv, delimiter=',') ## converted tsv to csv??? IMP line

	next(csv_data, None) #skip the header row from csv file without deleting it
	for row in csv_data:
		print row
		print "----------------------------" 
		print i
		c.execute("INSERT INTO session_table (SessionID, SessionName, Project, Session, Participant, Block, FileName) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(j,row[1],row[0],row[2],row[3],row[4],row[5]))

 		i += 1;
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
