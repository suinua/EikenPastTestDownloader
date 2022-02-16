import sys

from PyQt5 import QtWidgets

from download import get_content_list
from grade import Grade
from main_screen import Ui_Form


class gui(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(gui, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.__download_grades = []
        self.__parent_folder_path = "C:/"

    def check(self):
        if self.ui.check_all.isChecked():
            self.ui.check_all.setChecked(False)

    def on_select_1(self, is_checked: bool):
        self.check()
        if is_checked:
            self.__download_grades.append(Grade.ONE)
        else:
            self.__download_grades.remove(Grade.ONE)
        print(self.__download_grades)

    def on_select_p1(self, is_checked: bool):
        self.check()
        if is_checked:
            self.__download_grades.append(Grade.PRE_ONE)
        else:
            self.__download_grades.remove(Grade.PRE_ONE)
        print(self.__download_grades)

    def on_select_2(self, is_checked: bool):
        self.check()
        if is_checked:
            self.__download_grades.append(Grade.TWO)
        else:
            self.__download_grades.remove(Grade.TWO)
        print(self.__download_grades)

    def on_select_p2(self, is_checked: bool):
        self.check()
        if is_checked:
            self.__download_grades.append(Grade.PRE_TWO)
        else:
            self.__download_grades.remove(Grade.PRE_TWO)
        print(self.__download_grades)

    def on_select_3(self, is_checked: bool):
        self.check()
        if is_checked:
            self.__download_grades.append(Grade.THREE)
        else:
            self.__download_grades.remove(Grade.THREE)
        print(self.__download_grades)

    def on_select_4(self, is_checked: bool):
        self.check()
        if is_checked:
            self.__download_grades.append(Grade.FOUR)
        else:
            self.__download_grades.remove(Grade.FOUR)
        print(self.__download_grades)

    def on_select_5(self, is_checked: bool):
        self.check()
        if is_checked:
            self.__download_grades.append(Grade.FIVE)
        else:
            self.__download_grades.remove(Grade.FIVE)
        print(self.__download_grades)

    def on_select_all(self, is_checked: bool):
        self.__download_grades = []
        if is_checked:
            if self.ui.check_1.isChecked():
                self.ui.check_1.setChecked(False)
            if self.ui.check_p1.isChecked():
                self.ui.check_p1.setChecked(False)
            if self.ui.check_2.isChecked():
                self.ui.check_2.setChecked(False)
            if self.ui.check_p2.isChecked():
                self.ui.check_p2.setChecked(False)
            if self.ui.check_3.isChecked():
                self.ui.check_3.setChecked(False)
            if self.ui.check_4.isChecked():
                self.ui.check_4.setChecked(False)
            if self.ui.check_5.isChecked():
                self.ui.check_5.setChecked(False)

    def on_click_path_selector(self):
        text = QtWidgets.QFileDialog.getExistingDirectory(self, 'select folder', 'C:/')
        print(text)
        self.__parent_folder_path = text + "/"

    def on_click_download(self):
        try:
            for grade in self.__download_grades:
                for content in get_content_list(grade):
                    content.download(self.__parent_folder_path)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = gui()
    window.show()
    sys.exit(app.exec_())
