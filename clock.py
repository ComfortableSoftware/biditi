#!/usr/bin/python

import time

import teek

class Clock(teek.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = teek.Label(self)
        self.label.pack()
        self.updater_callback()

    def updater_callback(self):
        self.label.config['text'] = time.asctime()

        # tell tk to run this again after 1 second
        teek.after(1000, self.updater_callback)


window = teek.Window("Clock")
Clock(window).pack()
window.on_delete_window.connect(teek.quit)
teek.run()
