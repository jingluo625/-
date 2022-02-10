import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import Slot
from crawingUI import Ui_imgDownload
from imageCrawling_plus_plus_plus import img_download, selectType


class View(QtWidgets.QWidget, Ui_imgDownload):
    def __init__(self, opt):
        super().__init__()
        self.setupUi(self)
        self.opt = opt

    @Slot()
    def on_lineEdit_editingFinished(self):
        self.opt = int(self.lineEdit.text())
        # print(f'我的选择是{opt}')

    @Slot()
    def on_pushButton_clicked(self):
        self.pushButton.setText('正在下载中...')
        type, page = selectType(self.opt)
        # print(self.opt,type,page)
        img_download(type, page)
        self.pushButton.setText('下载完成！！')


class QSSLoader:
    def __init__(self):
        pass

    @staticmethod
    def read_qss_file(qss_file_name):
        with open(qss_file_name, 'r', encoding='UTF-8') as file:
            return file.read()


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    view = View(0)

    style_file = './UIStyle.qss'
    style_sheet = QSSLoader.read_qss_file(style_file)
    view.setStyleSheet(style_sheet)

    view.show()
    sys.exit(app.exec())
