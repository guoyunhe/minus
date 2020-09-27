#!/usr/bin/python3

"""
App Main Function
"""
import os
import sys
from qtpy.QtCore import Qt
from qtpy.QtGui import QGuiApplication
from qtpy.QtQml import QQmlApplicationEngine
from tasks.task import Task


def __main():
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()

    task = Task()
    context = engine.rootContext()
    context.setContextProperty("task", task)

    rootdir = os.path.dirname(__file__)
    engine.load(os.path.join(rootdir, "qml", "MainWindow.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())


if __name__ == "__main__":
    __main()
