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
## Class MainWindow
###########################################################################

class MainWindow ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"List Box Demo", pos = wx.DefaultPosition, size = wx.Size( 640,480 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.STAY_ON_TOP|wx.BORDER_THEME|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 640,480 ), wx.Size( 640,480 ) )

        MainBox = wx.BoxSizer( wx.HORIZONTAL )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Start Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        fgSizer1.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"End Port:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        fgSizer1.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Number Threads:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        fgSizer1.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        fgSizer1.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_button1, 0, wx.ALL, 5 )


        MainBox.Add( fgSizer1, 1, wx.EXPAND, 5 )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.ResultsHeader = wx.StaticText( self, wx.ID_ANY, u"Results", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.ResultsHeader.Wrap( -1 )

        bSizer2.Add( self.ResultsHeader, 0, wx.ALL, 5 )

        ResultsListboxChoices = [ u"A", u"B", u"C" ]
        self.ResultsListbox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), ResultsListboxChoices, wx.LB_ALWAYS_SB|wx.ALWAYS_SHOW_SB|wx.BORDER_DEFAULT|wx.BORDER_THEME )
        bSizer2.Add( self.ResultsListbox, 0, wx.ALL|wx.EXPAND, 5 )


        MainBox.Add( bSizer2, 1, wx.EXPAND, 5 )


        self.SetSizer( MainBox )
        self.Layout()
        self.StatusBar = self.CreateStatusBar( 4, 0, wx.ID_ANY )
        self.MenuBar = wx.MenuBar( 0 )
        self.FileMenu = wx.Menu()
        self.file_menu_open = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"&Open"+ u"\t" + u"CTRL+O", wx.EmptyString, wx.ITEM_NORMAL )
        self.FileMenu.Append( self.file_menu_open )

        self.FileMenu.AppendSeparator()

        self.FileExitMenu = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"E&xit"+ u"\t" + u"ALT+F4", wx.EmptyString, wx.ITEM_NORMAL )
        self.FileMenu.Append( self.FileExitMenu )

        self.MenuBar.Append( self.FileMenu, u"&File" )

        self.EditMenu = wx.Menu()
        self.EditMenuCopy = wx.MenuItem( self.EditMenu, wx.ID_ANY, u"&Copy"+ u"\t" + u"CTRL+C", wx.EmptyString, wx.ITEM_NORMAL )
        self.EditMenu.Append( self.EditMenuCopy )

        self.EditMenuPaste = wx.MenuItem( self.EditMenu, wx.ID_ANY, u"Paste"+ u"\t" + u"CTRL+V", wx.EmptyString, wx.ITEM_NORMAL )
        self.EditMenu.Append( self.EditMenuPaste )

        self.MenuBar.Append( self.EditMenu, u"&Edit" )

        self.HelpMenu = wx.Menu()
        self.HelpMenuAbout = wx.MenuItem( self.HelpMenu, wx.ID_ANY, u"About"+ u"\t" + u"F1", wx.EmptyString, wx.ITEM_NORMAL )
        self.HelpMenu.Append( self.HelpMenuAbout )

        self.MenuBar.Append( self.HelpMenu, u"&Help" )

        self.SetMenuBar( self.MenuBar )


        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


