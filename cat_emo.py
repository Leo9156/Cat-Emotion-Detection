import wx
import wx.xrc
import os
import cv2

save_path = ''

class MyFrame2 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_panel3 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Press the button to upload an image", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer4.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self.m_panel3, wx.ID_ANY, u"upload", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_button3, 0, wx.ALL, 5 )

        self.m_staticText6 = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )


        bSizer9.Add( bSizer4, 1, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Press the button to get the result.     ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer6.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.m_button6 = wx.Button( self.m_panel3, wx.ID_ANY, u"result", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button6, 0, wx.ALL, 5 )

        self.m_staticText8 = wx.StaticText( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer6.Add( self.m_staticText8, 0, wx.ALL, 5 )


        bSizer9.Add( bSizer6, 1, wx.EXPAND, 5 )


        self.m_panel3.SetSizer( bSizer9 )
        self.m_panel3.Layout()
        bSizer9.Fit( self.m_panel3 )
        self.m_notebook2.AddPage( self.m_panel3, u"image", False )
        self.m_panel2 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer71 = wx.BoxSizer( wx.VERTICAL )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText9 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Press the button to upload a video", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer8.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_button7 = wx.Button( self.m_panel2, wx.ID_ANY, u"upload", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_button7, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        bSizer8.Add( self.m_staticText10, 0, wx.ALL, 5 )


        bSizer71.Add( bSizer8, 1, wx.EXPAND, 5 )

        bSizer91 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText11 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Press the button to get the result.  ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer91.Add( self.m_staticText11, 0, wx.ALL, 5 )

        self.m_button8 = wx.Button( self.m_panel2, wx.ID_ANY, u"result", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer91.Add( self.m_button8, 0, wx.ALL, 5 )

        self.m_staticText12 = wx.StaticText( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        bSizer91.Add( self.m_staticText12, 0, wx.ALL, 5 )


        bSizer71.Add( bSizer91, 1, wx.EXPAND, 5 )


        self.m_panel2.SetSizer( bSizer71 )
        self.m_panel2.Layout()
        bSizer71.Fit( self.m_panel2 )
        self.m_notebook2.AddPage( self.m_panel2, u"video", False )
        self.m_panel31 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText13 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Press the button to start the camera", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        bSizer10.Add( self.m_staticText13, 0, wx.ALL, 5 )

        self.m_button9 = wx.Button( self.m_panel31, wx.ID_ANY, u"start", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button9, 0, wx.ALL, 5 )


        self.m_panel31.SetSizer( bSizer10 )
        self.m_panel31.Layout()
        bSizer10.Fit( self.m_panel31 )
        self.m_notebook2.AddPage( self.m_panel31, u"webcam", False )

        bSizer7.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer7 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button3.Bind( wx.EVT_BUTTON, self.UploadImage )
        self.m_button6.Bind( wx.EVT_BUTTON, self.GetImageResult )
        self.m_button7.Bind( wx.EVT_BUTTON, self.UploadVideo )
        self.m_button8.Bind( wx.EVT_BUTTON, self.GetVideoResult )
        self.m_button9.Bind( wx.EVT_BUTTON, self.StartCamera )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def UploadImage( self, event ):
        # Get the path of image selected by the user
        fileDialog = wx.FileDialog(self, message = "Choose a single file", defaultDir=os.path.dirname(__file__), wildcard='*.jpg', style = wx.FD_OPEN)
        dialogResult = fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            self.m_staticText6.SetLabel("Error with opening the file")
        else:
            path = fileDialog.GetPath()

            # Pass the image to detect.py and use the custom trainning model
            main_path = os.path.dirname(__file__)
            cmd = 'python ' + os.path.join(main_path, 'yolov5', 'detect.py') + ' --source {0} --weights '.format(path) +  os.path.join(main_path, 'yolov5', 'runs', 'train', 'exp2', 'weights', 'best.pt') + ' --conf-thres 0.5'
            file = os.popen(cmd, 'r')
            content = file.readlines()
            p = str(content[1]).replace('\n', '')  # Get the proper path
            global save_path 
            save_path = os.path.join(main_path, p)

            self.m_staticText6.SetLabel("Process successfully")

    def GetImageResult( self, event ):
        img = cv2.imread(save_path)
        cv2.imshow("result", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def UploadVideo( self, event ):
        # Get the path of video selected by the user
        fileDialog = wx.FileDialog(self, message = "Choose a single file", defaultDir='/Users/leoyang/DB_Yolo', wildcard='*.mp4', style = wx.FD_OPEN)
        dialogResult = fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            self.m_staticText6.SetLabel("Error with opening the file")
        else:
            path = fileDialog.GetPath()

            # Pass the image to detect.py and use the custom trainning model
            main_path = os.path.dirname(__file__)
            cmd = 'python ' + os.path.join(main_path, 'yolov5', 'detect.py') + ' --source {0} --weights '.format(path) +  os.path.join(main_path, 'yolov5', 'runs', 'train', 'exp2', 'weights', 'best.pt') + ' --conf-thres 0.5'
            file = os.popen(cmd, 'r')
            content = file.readlines()
            p = str(content[1]).replace('\n', '')  # Get the proper path
            global save_path 
            save_path = os.path.join(main_path, p)

            self.m_staticText10.SetLabel("Process successfully")

    def GetVideoResult( self, event ):
        cap = cv2.VideoCapture(save_path)
        while True:
            retval, frame = cap.read()
            if retval:
                cv2.imshow('video', frame)
            key = cv2.waitKey(10)
            if key == 27:  # Press ESC to close the video
                break

        cap.release()
        cv2.destroyAllWindows()

    def StartCamera(self, event):
        # Pass the image to detect.py and use the custom trainning model
        main_path = os.path.dirname(__file__)
        cmd = 'python ' + os.path.join(main_path, 'yolov5', 'detect.py') + ' --source 0 --weights ' +  os.path.join(main_path, 'yolov5', 'runs', 'train', 'exp2', 'weights', 'best.pt') + ' --conf-thres 0.5'
        os.system(cmd)

        

if __name__ == "__main__":
    app = wx.App()
    frm = MyFrame2(None)
    frm.Show()
    app.MainLoop()
