#!/usr/bin/python

import teek

window = teek.Window("Pack Example")
teek.Label(window, "One").pack()
teek.Label(window, "Two").pack()


def updateTime():


window.on_delete_window.connect(teek.quit)
teek.run()
