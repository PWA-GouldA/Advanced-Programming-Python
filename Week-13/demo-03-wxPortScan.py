# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class PortScannerFrame
###########################################################################

class PortScannerFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
                          title=u"wxPortScan", pos=wx.DefaultPosition,
                          size=wx.Size(640, 320),
                          style=wx.DEFAULT_FRAME_STYLE | wx.BORDER_THEME | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.file_menu = wx.Menu()
        self.file_exit_menu_item = wx.MenuItem(self.file_menu, wx.ID_ANY, u"Ex&it" + u"\t" + u"ALT+x",
                                               u"Exit application", wx.ITEM_NORMAL)
        self.file_menu.Append(self.file_exit_menu_item)

        self.m_menubar1.Append(self.file_menu, u"&File")

        self.help_menu = wx.Menu()
        self.help_about_menu_item = wx.MenuItem(self.help_menu, wx.ID_ANY, u"About", u"About wxPortScan",
                                                wx.ITEM_NORMAL)
        self.help_menu.Append(self.help_about_menu_item)

        self.help_tafe_menu_item = wx.MenuItem(self.help_menu, wx.ID_ANY, u"TAFE OS", u"Who is TAFE Open Source",
                                               wx.ITEM_NORMAL)
        self.help_menu.Append(self.help_tafe_menu_item)

        self.m_menubar1.Append(self.help_menu, u"Help")

        self.SetMenuBar(self.m_menubar1)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.host_label = wx.StaticText(self, wx.ID_ANY, u"Host", wx.DefaultPosition, wx.DefaultSize, 0)
        self.host_label.Wrap(-1)

        gSizer2.Add(self.host_label, 0, wx.ALL | wx.EXPAND, 5)

        self.host_text = wx.TextCtrl(self, wx.ID_ANY, u"localhost", wx.DefaultPosition, wx.DefaultSize,
                                     0 | wx.TAB_TRAVERSAL)
        self.host_text.SetMaxLength(255)
        gSizer2.Add(self.host_text, 0, wx.ALL | wx.EXPAND, 5)

        self.port_start_label = wx.StaticText(self, wx.ID_ANY, u"Start Port", wx.DefaultPosition, wx.DefaultSize, 0)
        self.port_start_label.Wrap(-1)

        gSizer2.Add(self.port_start_label, 0, wx.ALL | wx.EXPAND, 5)

        self.port_start_text = wx.TextCtrl(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize,
                                           0 | wx.TAB_TRAVERSAL)
        self.port_start_text.SetMaxLength(5)
        gSizer2.Add(self.port_start_text, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        gSizer2.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.start_port_slider = wx.Slider(self, wx.ID_ANY, 50, 1, 65535, wx.DefaultPosition, wx.DefaultSize,
                                           wx.SL_HORIZONTAL | wx.SL_MIN_MAX_LABELS | wx.TAB_TRAVERSAL)
        gSizer2.Add(self.start_port_slider, 0, wx.ALL | wx.EXPAND, 5)

        self.port_end_label = wx.StaticText(self, wx.ID_ANY, u"End Port", wx.DefaultPosition, wx.DefaultSize, 0)
        self.port_end_label.Wrap(-1)

        gSizer2.Add(self.port_end_label, 0, wx.ALL | wx.EXPAND, 5)

        self.port_end_text = wx.TextCtrl(self, wx.ID_ANY, u"1024", wx.DefaultPosition, wx.DefaultSize,
                                         0 | wx.TAB_TRAVERSAL)
        self.port_end_text.SetMaxLength(5)
        gSizer2.Add(self.port_end_text, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText71 = wx.StaticText(self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText71.Wrap(-1)

        gSizer2.Add(self.m_staticText71, 0, wx.ALL, 5)

        self.end_port_slider = wx.Slider(self, wx.ID_ANY, 1024, 1, 65535, wx.DefaultPosition, wx.DefaultSize,
                                         wx.SL_HORIZONTAL | wx.SL_MIN_MAX_LABELS | wx.TAB_TRAVERSAL)
        gSizer2.Add(self.end_port_slider, 0, wx.ALL | wx.EXPAND, 5)

        self.threads_label = wx.StaticText(self, wx.ID_ANY, u"Threads", wx.DefaultPosition, wx.DefaultSize, 0)
        self.threads_label.Wrap(-1)

        gSizer2.Add(self.threads_label, 0, wx.ALL | wx.EXPAND, 5)

        self.threads_text = wx.TextCtrl(self, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize,
                                        0 | wx.TAB_TRAVERSAL)
        self.threads_text.SetMaxLength(3)
        gSizer2.Add(self.threads_text, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        gSizer2.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.threads_slider = wx.Slider(self, wx.ID_ANY, 64, 1, 512, wx.DefaultPosition, wx.DefaultSize,
                                        wx.SL_HORIZONTAL | wx.SL_MIN_MAX_LABELS | wx.TAB_TRAVERSAL)
        gSizer2.Add(self.threads_slider, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText711 = wx.StaticText(self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText711.Wrap(-1)

        gSizer2.Add(self.m_staticText711, 0, wx.ALL, 5)

        self.scan_button = wx.Button(self, wx.ID_ANY, u"&Scan", wx.DefaultPosition, wx.DefaultSize,
                                     0 | wx.TAB_TRAVERSAL)
        gSizer2.Add(self.scan_button, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(gSizer2, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Open Ports"), wx.VERTICAL)

        ports_listChoices = []
        self.ports_list = wx.ListBox(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                     ports_listChoices, wx.LB_SINGLE)
        sbSizer1.Add(self.ports_list, 5, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(sbSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.m_statusBar2 = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.OnExit, id=self.file_exit_menu_item.GetId())
        self.port_start_text.Bind(wx.EVT_TEXT, self.OnStartPortText)
        self.start_port_slider.Bind(wx.EVT_SLIDER, self.OnStartPortSlider)
        self.port_end_text.Bind(wx.EVT_TEXT, self.OnEndPortText)
        self.end_port_slider.Bind(wx.EVT_SLIDER, self.OnEndPortSlider)
        self.threads_text.Bind(wx.EVT_TEXT, self.OnThreadText)
        self.threads_slider.Bind(wx.EVT_SLIDER, self.OnThreadSlider)
        self.scan_button.Bind(wx.EVT_BUTTON, self.OnStartScan)

    def __del__(self):
        pass
    # Virtual event handlers, overide them in your derived class

    def OnExit(self, event):
        event.Skip()


    def OnStartPortText(self, event):
        start_port = self.port_start_text.Value
        self.start_port_slider.SetValue(int(float(start_port)))
        event.Skip()


    def OnStartPortSlider(self, event):
        start_port = self.start_port_slider.Value
        self.port_start_text.SetValue(str(start_port))
        event.Skip()


    def OnEndPortText(self, event):
        end_port = self.port_end_text.Value
        self.end_port_slider.SetValue(int(float(end_port)))
        event.Skip()


    def OnEndPortSlider(self, event):
        end_port = self.end_port_slider.Value
        self.port_end_text.SetValue(str(end_port))
        event.Skip()


    def OnThreadText(self, event):
        threads = self.threads_text.Value
        self.thread_slider.SetValue(int(float(threads)))
        event.Skip()


    def OnThreadSlider(self, event):
        threads = self.thread_slider.Value
        self.threads_text.SetValue(str(threads))
        event.Skip()


    def OnStartScan(self, event):
        event.Skip()


app = wx.App()

# Then a frame.
frm = PortScannerFrame(wx.Frame(None))

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
