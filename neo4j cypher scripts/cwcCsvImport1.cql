// First Part of Session Information -----------------------------------------------------
CREATE CONSTRAINT ON (l:Label) ASSERT l.id IS UNIQUE;
CREATE CONSTRAINT ON (s:Session) ASSERT s.sessionName IS UNIQUE;
CREATE CONSTRAINT ON (p:Participant) ASSERT p.participantName IS UNIQUE;
CREATE CONSTRAINT ON (b:Block) ASSERT b.blockName IS UNIQUE;

// --------------------------------------------------
//USING PERIODIC COMMIT 100  // not working ???
LOAD CSV WITH HEADERS FROM 
'file:///cwc/gesture3s.csv' AS line
//WITH line
//LIMIT 1000
//RETURN line

//---------------------------------------------------
CREATE (label:Label {id: TOINT(line.GestureID)})
SET label.fileName = line.`File Name`

MERGE (session:Session {sessionName: UPPER(line.Session)})
MERGE (participant:Participant {participantName: UPPER(line.Participant)})
MERGE (block:Block {blockName: UPPER(line.Block)})

CREATE (label)-[:PRESENT_IN]->(session)
CREATE (label)-[:PERFORMED_BY]->(participant)
CREATE (label)-[:PRESENT_IN]->(block)
;