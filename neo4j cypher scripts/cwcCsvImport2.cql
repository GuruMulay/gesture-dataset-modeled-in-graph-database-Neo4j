// First Part of Session Information -----------------------------------------------------
CREATE CONSTRAINT ON (l:Label) ASSERT l.id IS UNIQUE;
CREATE CONSTRAINT ON (sn:SessionName) ASSERT sn.sName IS UNIQUE;
CREATE CONSTRAINT ON (cwc:Project) ASSERT cwc.pType IS UNIQUE;

//--------------------------------------------------
//USING PERIODIC COMMIT 100  // not working ???
LOAD CSV WITH HEADERS FROM 
'file:///cwc/gesture3s_1.csv' AS line
//WITH line
//LIMIT 1000
//RETURN line

//--------------------------------------------------
CREATE (label:Label {id: TOINT(line.GestureID)})
SET label.labelName = line.Label

MERGE (sessionName:SessionName {sName: UPPER(line.`Session Name`)})
SET sessionName.fileName = line.`File Name`
SET sessionName.sessionNumber = line.Session
SET sessionName.participantNumber = line.Participant
SET sessionName.blockNumber = line.Block
SET sessionName.projectType = line.Project

CREATE (label)-[:PRESENT_IN]->(sessionName)

MERGE (project:Project {pType: UPPER(line.Project)})

CREATE (label)-[:PROJECT_TYPE]->(project)

;