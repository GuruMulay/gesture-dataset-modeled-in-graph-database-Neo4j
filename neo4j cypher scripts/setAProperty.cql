//USING PERIODIC COMMIT 100  // not working ???
LOAD CSV WITH HEADERS FROM 
'file:///cwc/gesture3s_1.csv' AS line
//WITH line
//LIMIT 1000
//RETURN line


// ------------------------------------------------------------------
MERGE (participant:Participant {pName: UPPER(line.Participant)})
SET participant.age = '25'
SET participant.gender = 'M'
SET participant.dominantHand = 'R'
;

// ------------------------------------------------------------------
MERGE (sessionName:SessionName {sName: UPPER(line.`Session Name`)})

SET sessionName.projectType = line.Project
;