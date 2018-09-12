// First Part of Session Information -----------------------------------------------------
CREATE CONSTRAINT ON (l:Label) ASSERT l.id IS UNIQUE;
CREATE CONSTRAINT ON (sn:SessionName) ASSERT sn.sName IS UNIQUE;
CREATE CONSTRAINT ON (p:Participant) ASSERT p.pName IS UNIQUE;
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
//GESTURE = "GESTURE"  
SET label.labelType = "GESTURE"  // "INTENT" for
SET label.startFrame = line.`Start Frame`
SET label.endFrame = line.`End Frame`
SET label.startTimestamp = line.`Start Timestamp`
SET label.endTimestamp = line.`End Timestamp`
SET label.duration = line.Duration
SET label.startFrameTimestamp = line.`Start Frame Timestamp`
SET label.endFrameTimestamp = line.`End Frame Timestamp`


MERGE (sessionName:SessionName {sName: UPPER(line.`Session Name`)})
SET sessionName.fileName = line.`File Name`
SET sessionName.sessionNumber = line.Session
SET sessionName.participantNumber = line.Participant
SET sessionName.blockNumber = line.Block
SET sessionName.projectType = line.Project

CREATE (label)-[pi:PRESENT_IN]->(sessionName)


MERGE (participant:Participant {pName: UPPER(line.Participant)})
SET participant.age = '25'
SET participant.gender = 'M'
SET participant.dominantHand = 'R'
CREATE (label)-[pb:PERFORMED_BY]->(participant)


MERGE (project:Project {pType: UPPER(line.Project)})

CREATE (label)-[pt_lp:PROJECT_TYPE]->(project)
CREATE (sessionName)-[pt_sp:PROJECT_TYPE]->(project)
;
