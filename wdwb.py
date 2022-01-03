#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

import wx
import wx.html2

USER_URLS = ["http://localhost", "http://127.0.0.0", "http://0.0.0.0"]


class WebDevWebBrowser(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((800, 900))
        self.SetTitle("WDWB")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap(f"{os.getcwd()}/wdwb.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)

        '''
        self.main_frame_statusbar = self.CreateStatusBar(1)
        self.main_frame_statusbar.SetStatusWidths([-1])
        main_frame_statusbar_fields = ["main_frame_statusbar"]
        for i in range(len(main_frame_statusbar_fields)):
            self.main_frame_statusbar.SetStatusText(main_frame_statusbar_fields[i], i)
        '''
        self.statusbar = self.CreateStatusBar(2)
        self.statusbar.SetStatusWidths([-1, -1])
        # statusbar fields
        statusbar_fields = ["statusbar_left", "statusbar_right"]
        for i in range(len(statusbar_fields)):
            self.statusbar.SetStatusText(statusbar_fields[i], i)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        toolbar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(toolbar_sizer, 0, wx.ALL | wx.EXPAND, 5)

        #self.button_home = wx.Button(self, wx.ID_HOME, "")
        self.button_home = wx.Button(self, wx.ID_ANY, style=wx.BU_EXACTFIT)
        self.button_home.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_GO_HOME, wx.ART_BUTTON))
        self.button_home.SetToolTip("Home")
        toolbar_sizer.Add(self.button_home, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        #self.button_previous = wx.Button(self, wx.ID_BACKWARD, "")
        self.button_previous = wx.Button(self, wx.ID_ANY, style=wx.BU_EXACTFIT)
        self.button_previous.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_GO_BACK, wx.ART_BUTTON))
        self.button_previous.SetToolTip("Previous page")
        toolbar_sizer.Add(self.button_previous, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        #self.button_next = wx.Button(self, wx.ID_FORWARD, "")
        self.button_next = wx.Button(self, wx.ID_ANY, style=wx.BU_EXACTFIT)
        self.button_next.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD, wx.ART_BUTTON))
        self.button_next.SetToolTip("Next page")
        toolbar_sizer.Add(self.button_next, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        #self.button_refresh = wx.Button(self, wx.ID_REFRESH, "")
        self.button_refresh = wx.Button(self, wx.ID_ANY, style=wx.BU_EXACTFIT)
        self.button_refresh.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_BUTTON))
        self.button_refresh.SetToolTip("Refresh page")
        toolbar_sizer.Add(self.button_refresh, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        self.cb_url = wx.ComboBox(self, wx.ID_ANY, choices=USER_URLS, style=wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER)
        self.cb_url.SetSelection(-1)
        toolbar_sizer.Add(self.cb_url, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        #self.button_clear = wx.Button(self, wx.ID_CLEAR, "")
        self.button_clear = wx.Button(self, wx.ID_ANY, style=wx.BU_EXACTFIT)
        self.button_clear.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_DELETE, wx.ART_BUTTON))
        self.button_clear.SetToolTip("Clear adress bar")
        toolbar_sizer.Add(self.button_clear, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        #self.button_settings = wx.Button(self, wx.ID_PREFERENCES, "")
        self.button_settings = wx.Button(self, wx.ID_ANY, style=wx.BU_EXACTFIT)
        self.button_settings.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_HELP_SETTINGS, wx.ART_BUTTON))
        self.button_settings.SetToolTip("Open settings")
        toolbar_sizer.Add(self.button_settings, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)

        #self.button_exit = wx.Button(self, wx.ID_EXIT, "")
        self.button_exit = wx.Button(self, wx.ID_ANY, style=wx.BU_EXACTFIT)
        self.button_exit.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_QUIT, wx.ART_BUTTON))
        self.button_exit.SetToolTip("Exit WDWB")
        toolbar_sizer.Add(self.button_exit, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self.view = wx.html2.WebView.New(self)
        main_sizer.Add(self.view, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        self.SetSizer(main_sizer)

        self.view.LoadURL(f'file://{os.getcwd()}/data/index.html')
        self.Layout()
        self.Centre()

        self.Bind(wx.EVT_BUTTON, self.evt_home, self.button_home)
        self.Bind(wx.EVT_BUTTON, self.evt_previous, self.button_previous)
        self.Bind(wx.EVT_BUTTON, self.evt_next, self.button_next)
        self.Bind(wx.EVT_BUTTON, self.evt_refresh, self.button_refresh)
        self.Bind(wx.EVT_COMBOBOX, self.evt_cb, self.cb_url)
        self.Bind(wx.EVT_TEXT, self.evt_cbtext, self.cb_url)
        self.Bind(wx.EVT_TEXT_ENTER, self.evt_cbtext_enter, self.cb_url)
        self.Bind(wx.EVT_BUTTON, self.evt_clear, self.button_clear)
        self.Bind(wx.EVT_BUTTON, self.evt_settings, self.button_settings)
        self.Bind(wx.EVT_BUTTON, self.evt_exit, self.button_exit)
        self.Bind(wx.EVT_CLOSE, self.evt_close, self)

    def evt_home(self, event):
        print("Event handler 'evt_home' not implemented!")
        event.Skip()

    def evt_previous(self, event):
        print("Event handler 'evt_previous' not implemented!")
        event.Skip()

    def evt_next(self, event):
        print("Event handler 'evt_next' not implemented!")
        event.Skip()

    def evt_refresh(self, event):
        print("Event handler 'evt_refresh' not implemented!")
        event.Skip()

    def evt_cb(self, event):
        print("Event handler 'evt_cb' not implemented!")
        event.Skip()

    def evt_cbtext(self, event):
        print("Event handler 'evt_cbtext' not implemented!")
        event.Skip()

    def evt_cbtext_enter(self, event):
        print("Event handler 'evt_cbtext_enter' not implemented!")
        event.Skip()

    def evt_clear(self, event):
        print("Event handler 'evt_clear' not implemented!")
        event.Skip()

    def evt_settings(self, event):
        print("Event handler 'evt_settings' not implemented!")
        event.Skip()

    def evt_exit(self, event):
        self.Close()

    def evt_close(self, event):
        print("Event handler 'evt_close' not implemented!")
        event.Skip()

class MyApp(wx.App):
    def OnInit(self):
        self.main_frame = WebDevWebBrowser(None, wx.ID_ANY, "")
        self.SetTopWindow(self.main_frame)
        self.main_frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
