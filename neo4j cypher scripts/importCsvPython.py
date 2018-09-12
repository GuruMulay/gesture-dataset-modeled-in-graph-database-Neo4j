from py2neo import cypher, Path, authenticate, Graph
from py2neo import Node, Relationship
# v2.0 from py2neo import neo4j, node, rel

# Link ------>
# http://nicolewhite.github.io/neo4j-jupyter/hello-world.html
import csv
import time

def graphDatabaseQueries():

	# connect to the localhost  -----------------
	url = "http://localhost:7474/db/data/"
	authenticate("localhost:7474", "neo4j", "cwc")
	graph = Graph(url)
	
	# graph.delete_all()

	# print "-----------------------------------"
	# query1 = """
	# start n = node(*)
	# match (n:Label)
	# return count(n)
	# """
	# data = graph.run(query1)
	# for d in data:
	# 	print d

	# print "-----------------------------------"
	# query2 = """
	# match (n:Label) where n.labelName="body: move, front;" return count(n)
	# """
	# data = graph.run(query2)
	# for d in data:
	# 	print d

	# print "-----------------------------------"
	# query3 = """
	# match (Label)-[r]-() return distinct type(r) 
	# """
	# data = graph.run(query3)
	# for d in data:
	# 	print d, type(d)

	# print "-----------------------------------"
	# query4 = """
	# MATCH (p:Participant)<-[r:PERFORMED_BY]-(n:Label)-[:PRESENT_IN]->(SessionName) 
	# WHERE n.labelName IN ['body: move, front;'] AND SessionName.sessionNumber = "Session 3" AND p.pName IN ["PARTICIPANT 5", "PARTICIPANT 6"]
	# RETURN n.labelName, SessionName.sessionNumber, p.pName, count(n:Label)
	# """
	# data = graph.run(query4)
	# for d in data:
	# 	print d

	# print " query -----------------------------------"
	# query5 = """
	# MATCH (p:Participant)<-[r:PERFORMED_BY]-(n:Label)-[:PRESENT_IN]->(SessionName) 
	# WHERE n.labelName IN ['body: move, front;'] AND SessionName.sessionNumber = "Session 3" AND p.pName IN ["PARTICIPANT 5", "PARTICIPANT 6"] 
	# RETURN n.labelName, SessionName.sessionNumber, SessionName.fileName, p.pName, count(n:Label)
	# """
	# data = graph.run(query5)
	# for d in data:
	# 	print d, type(d[4])

	# print " query -----------------------------------"
	# query6 = """
	# MATCH (n:Label)-[:PRESENT_IN]->(SessionName) 
	# WHERE n.labelName IN ['body: move, front;'] AND SessionName.sessionNumber = "Session 3" 
	# RETURN n.labelName, SessionName.sessionNumber, SessionName.fileName
	# """
	# data = graph.run(query6)
	# for d in data:
	# 	print d

	# print " query works correct; checked! -----------------------------------"
	query7 = """
	MATCH (n:Label)-[:PRESENT_IN]->(SessionName)
    WHERE n.labelName = {gesture} AND SessionName.sessionNumber = {session} AND SessionName.participantNumber = {participant}
    RETURN count(n), n.labelName, SessionName.fileName, n.startFrameTimestamp, n.endFrameTimestamp
	"""
	qResult = [0,0,0,0,0] 
	i = 0;
	data = graph.run(query7, gesture="body: move, front;", session="Session 1", participant="Participant 2")
	print data
	print "======================="
	for d in data:
		#qResult[i] = d
		print d,  " ------------------ "

		i = i+1



if __name__ == '__main__':
    start = time.time()
    # print " START -----------------------------------"

    graphDatabaseQueries()

    end = time.time() - start
    print "Total Time ", end