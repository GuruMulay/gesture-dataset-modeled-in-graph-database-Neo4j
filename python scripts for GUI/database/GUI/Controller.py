import Tkinter as Tk
from View import *
from Model import *
import tkMessageBox
import os
import core_video as video


from py2neo import cypher, Path, authenticate, Graph
from py2neo import Node, Relationship


class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.root.title('Upload Video')
        #w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        #self.root.geometry("%dx%d+0+0" % (w, h))

        self.view = View(self.root)
        self.view.layout.button_get_files.button_get_documents.bind("<Button>", self.get_documents)


    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        self.root.mainloop()


    def get_data(self, event):
        self.label = self.view.sidepanel.dropdown_label.box2.get()
        self.gesture = self.view.sidepanel.dropdown_sound.box1.get()
        self.pflag = self.view.sidepanel.participant_checkbox.p_flag.get()
        self.count = self.view.sidepanel.entry_count_threshold.count_threshold.get()
        self.pcount = self.view.sidepanel.entry_participant_count.pcount_threshold.get()
        result = get_parameters([self.gesture, self.label, self.pflag, self.count, self.pcount])
        self.view.sidepanel.entry_display_data.set_text(result)


    def get_documents(self, event):
        gesture_list = []
        if self.view.layout.option_checkbox.g1.get():
            gesture_list.append('arms: apart, left;')

        if self.view.layout.option_checkbox.g2.get():
            gesture_list.append('body: move, front;')

        if(len(gesture_list) == 0):
            tkMessageBox.showerror("Error", "Please select a gesture!")
        #Loop till True

        self.generate_folders(gesture_list)
        self.process_query(gesture_list)


    def generate_folders(self, gesture_list):
        self.path = self.view.layout.directory.label_dir_name["text"]+'/'
        for g in gesture_list:
            if not os.path.exists(os.path.join(self.path, g.replace(';',''))): os.makedirs(os.path.join(self.path, g.replace(';','')))

    def process_query(self, gesture_list):
        print gesture_list

        #for every gesture, fire the query,
        #this will get you filename, start frame and end frame:
        #implement the video cutting and joining
        #video.get_frame_range(file_name, start_frame, end_frame)
        #video.write_videoframes((file_name+(gesture_name)), folder_name='temp_frames')

        #for g in gesture_list:
            #file_name, start_frame, end_frame

        # connect to the localhost  -----------------
        url = "http://localhost:7474/db/data/"
        authenticate("localhost:7474", "neo4j", "cwc")
        graph = Graph(url)
        
        # print " query -----------------------------------"
        query7 = """
        MATCH (n:Label)-[:PRESENT_IN]->(SessionName)
        WHERE n.labelName = {gesture} AND SessionName.sessionNumber = {session} AND SessionName.participantNumber = {participant} 
        RETURN count(n), n.labelName, SessionName.fileName, n.startFrameTimestamp, n.endFrameTimestamp, SessionName.sessionNumber, SessionName.participantNumber, SessionName.blockNumber
        """
        file_dir = "/home/dhruva/neo4j/database/z/"

         # AND SessionName.blockNumber = {block}
        print gesture_list, "gesture list"

        for gest in gesture_list:
            print gest
            # data = graph.run(query7, gesture="body: move, front;", session="Session 1", participant="Participant 2")
            data = graph.run(query7, gesture=gest, session="Session 1", participant="Participant 2")  # file_dir+d[2]
            #print data
            for d in data:
                #print file_dir+d[2].replace('\\','/') , d[3], d[4]
                src_path = (file_dir+d[2].replace('\\','/'))
                des_path = (self.path + '/' + (gest.replace(';', '')) + '/' + d[5].split()[-1] + '_' +
                d[6].split()[-1] + '_' + d[7].split()[-1] + '_' + d[3] + '_' + d[4] + '_' + d[2].split('\\')[-1])
                video.get_frame_range(src_path, int(d[3]), int(d[4]))
                video.write_videoframes(des_path, folder_name='temp_frames')
            
            # video.get_frame_range(file_dir+data[0][2], data[0][3], data[0][4])
            # print data[0][2], data[0][3], data[0][4]

        print " Success! -----------------------------------"


    # def graphDatabaseQueries(self, gesture_list):

    # # connect to the localhost  -----------------
    # url = "http://localhost:7474/db/data/"
    # authenticate("localhost:7474", "neo4j", "cwc")
    # graph = Graph(url)
    
    # # print " query -----------------------------------"
    # query7 = """
    # MATCH (n:Label)-[:PRESENT_IN]->(SessionName)
    # WHERE n.labelName = {gesture} AND SessionName.sessionNumber = {session} AND SessionName.participantNumber = {participant}
    # RETURN count(n), n.labelName, SessionName.fileName, n.startFrameTimestamp, n.endFrameTimestamp
    # """

    # for gest in gesture_list:
    #     # data = graph.run(query7, gesture="body: move, front;", session="Session 1", participant="Participant 2")
    #     data = graph.run(query7, gesture=gest, session="Session 1", participant="Participant 2")
    #     for d in data:
    #         print d

    #     video.get_frame_range(d[2], d[3], d[4])
    #     video.write_videoframes((d[2]+(gest)), folder_name='temp_frames')

    # print " Success! -----------------------------------"
