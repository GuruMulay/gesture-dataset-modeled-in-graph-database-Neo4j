import Tkinter as Tk
import ttk, tkFileDialog

class Window():
    def __init__(self, root):

        self.option_checkbox = CheckBoxOptions(root)
        self.button_get_files = ButtonGetFiles(root)
        self.directory = ButtonGetDirectory(root)


class ButtonGetDirectory():
    def __init__(self, root):
        self.root = root
        inFileLbl = Tk.Label(self.root, text="Select Directory:")
        inFileLbl.grid(row=0, column=0, sticky='E')

        self.label_dir_name = Tk.Label(self.root, text=" ", width=70)
        self.label_dir_name.grid(row=0, column=1, sticky="WE")

        self.button_get_dir = Tk.Button(self.root, text="Browse ...", command = self.get_target_directory)
        self.button_get_dir.grid(row=0, column=6, sticky='W')

    def get_target_directory(self):
        global root
        video_path = tkFileDialog.askdirectory(parent=self.root, title='Target directory to store files')
        print 'Directory name is: ', video_path
        self.label_dir_name["text"] = str(video_path)


class CheckBoxOptions():
    def __init__(self, root):
        self.g1 = Tk.IntVar()
        self.g2 = Tk.IntVar()
        c1 = Tk.Checkbutton(root, text="arms apart", variable=self.g1)
        c1.grid(row=1, column=0, sticky="W")
        c2 = Tk.Checkbutton(root, text="RA move down", variable=self.g2)
        c2.grid(row=2, column=0, sticky="W")



class ButtonGetFiles():
    def __init__(self, root):
        self.button_get_documents = Tk.Button(root, text="Get Documents")
        self.button_get_documents.grid(row=0, column=7, sticky="W")


class LabelFrames():
    def __init__(self, root):
        stepOne = Tk.LabelFrame(root, text=" 1. Select parameters Label Frame")
        stepOne.grid(row=0, columnspan=20, sticky='WE', \
                     padx=35, pady=20, ipadx=10, ipady=5)

        stepTwo = Tk.LabelFrame(root, text ="2. Select button Label Frame")
        stepTwo.grid(row=0, column=20, sticky='WE', \
                       padx=35, pady=20, ipadx=10, ipady=5)

        stepThree = Tk.LabelFrame(root, text="Display Output Window Label Frame")
        stepThree.grid(row=1, columnspan=20, sticky='WE', \
                     padx=35, pady=20, ipadx=10, ipady=5)


        self.dropdown_sound = DropdownSound(stepOne)
        self.dropdown_label = DropdownLabel(stepOne)
        self.participant_checkbox = CheckBoxParticipant(stepOne)
        self.entry_count_threshold = EntryCountThreshold(stepOne)
        self.entry_participant_count = EntryParticipantCountThreshold(stepOne)

        self.button_process_data = ButtonProcessData(stepTwo)

        self.entry_display_data= EntryDisplay(stepThree)

        '''
        self.frame2 = Tk.Frame(root)
        self.frame2.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.plotBut = Tk.Button(self.frame2, text="Plot ")
        self.plotBut.pack(side="top", fill=Tk.BOTH)
        self.clearButton = Tk.Button(self.frame2, text="Clear")
        self.clearButton.pack(side="top", fill=Tk.BOTH)
        '''


class MenuBar():
    def __init__(self, root):
        self.menubar = Tk.Menu(root)
        root.config(menu=self.menubar)

        opmenu = Tk.Menu(self.menubar, tearoff=0)
        tool = Tk.Menu(self.menubar, tearoff=0)
        help1 = Tk.Menu(self.menubar, tearoff=0)
        view = Tk.Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label="File", menu=opmenu)  # file menu
        opmenu.add_command(label="Open")
        opmenu.add_separator()
        opmenu.add_command(label="Exit")

        self.menubar.add_cascade(label="Tools", menu=tool)  # tool menu
        tool.add_command(label="Wavelets")

        self.menubar.add_cascade(label="Help", menu=help1)  # help menu
        help1.add_command(label="CBVCD help")
        help1.add_command(label="System requirements")
        help1.add_separator()
        help1.add_command(label="Query Video")
        help1.add_command(label="Video Segmentation")
        help1.add_separator()
        help1.add_command(label="About Us")


class DropdownSound():
    def __init__(self, root):
        #self.menubar = Tk.Menu(root)
        lbl1 = Tk.Label(root, text="Sound :")
        lbl1.grid(row=0, column=1,  pady=20, sticky="W")
        self.box1 = ttk.Combobox(root,state='readonly')
        self.box1['values'] = ('With Sound', 'No Sound', 'Combined')
        self.box1.current(0)
        self.box1.grid(row=0, column=2, pady=20, stick="N")


class DropdownLabel():
    def __init__(self, root):
        lbl1 = Tk.Label(root, text="Label :")
        lbl1.grid(row=0, column=3, pady=20, sticky="W")
        self.box2 = ttk.Combobox(root, state='readonly')
        self.box2['values'] = ('Gesture', 'Intent', 'Combined')
        self.box2.current(0)
        self.box2.grid(row=0, column=4, pady=20, stick="N")


class CheckBoxParticipant():
    def __init__(self, root):
        self.p_flag = Tk.IntVar()
        c = Tk.Checkbutton(root, text="Participant", variable=self.p_flag)
        c.grid(row=0, column=5, sticky="W")


class EntryCountThreshold():
    def __init__(self, root):
        self.count_threshold = Tk.IntVar()
        lbl1 = Tk.Label(root, text="Count Threshold: ")
        lbl1.grid(row=0, column=6, pady=20, sticky="W")
        self.entry_count = Tk.Entry(root, textvariable=self.count_threshold)
        self.entry_count.grid(row=0, column=7, pady=20, sticky="E")


class EntryParticipantCountThreshold():
    def __init__(self, root):
        self.pcount_threshold = Tk.IntVar()
        lbl1 = Tk.Label(root, text="Participant Threshold: ")
        lbl1.grid(row=0, column=8, pady=20, sticky="W")
        self.entry_participant = Tk.Entry(root, textvariable=self.pcount_threshold)
        self.entry_participant.grid(row=0, column=9, pady=20, sticky="E")


class ButtonProcessData():
    def __init__(self, root):
        self.button_result = Tk.Button(root, text="Get Results")
        self.button_result.grid(row=0, column=0, padx = 7, pady=18, sticky="W")

        self.button_save_file = Tk.Button(root, text="Save as File")
        self.button_save_file.grid(row=0, column=1, padx=7, pady=18, sticky="W")


class EntryDisplay():
    def __init__(self, root):
        self.root= root
        e = Tk.Entry(self.root, relief=Tk.RIDGE, state=Tk.DISABLED)

    def set_text(self, result):
        m, n = len(result), len(result[0])

        rows = []
        for i in range(m):
            cols = []
            for j in range(n):
                e = Tk.Entry(self.root, relief=Tk.RIDGE)
                e.grid(row=i, column=j, sticky=Tk.NSEW)
                e.insert(Tk.END, '%s' % (result[i][j]))
                cols.append(e)
                e.config(state='readonly')
            rows.append(cols)
