
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import sys
import requests
import urllib
import ctypes
import os

numpic = 0   
genres = ["Action","Adventure","Animation","Comedy","Crime","Documentary","Drama","Family","Fantasy","History","Horror","Music","Mystery","Romance","Sci-Fi","Thriller","War", "Western"]
keys = ["28","12","16","35","80","99","18","10751","14","36","27","10402","9648","10749","878","53","10752", "37"]
ordertype = ["Popularity", "Year", "Rate"]
keys_2 = ["popularity.desc", "release_date.desc", "vote_average.desc"]
dicti = dict(zip(genres,keys))
dicti_2 = dict(zip(ordertype, keys_2))
stype = "title"
curdur = "forward"
curOrder = ""
maxcur = 10
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 477)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setFixedSize(1036, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 221, 31))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 16))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 440, 290, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 20, 93, 28))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 410, 841, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 811, 331))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 440, 200, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 440, 31, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(790, 440, 31, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(518, 20, 121, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(750, 20, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 30, 55, 16))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(450, 10, 16, 41))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(860, 20, 171, 441))
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setObjectName("listWidget")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(650, 20, 91, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TY - Background Changer"))
        self.label.setText(_translate("MainWindow", "Name Of Movie :"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.pushButton.clicked.connect(self.b1clicked)
        self.pushButton_2.setText(_translate("MainWindow", "Set as Desktop Background Picture"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", ""))
        self.pushButton_2.clicked.connect(self.b2clicked)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_3.setText(_translate("MainWindow", ">"))
        self.pushButton_3.clicked.connect(self.b3clicked)
        self.pushButton_4.setText(_translate("MainWindow", "<"))
        self.pushButton_4.clicked.connect(self.b4clicked)
        self.comboBox.setCurrentText(_translate("MainWindow", "Action"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Action"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Adventure"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Animation"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Comedy"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Crime"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Documentary"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Drama"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Family"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Fantasy"))
        self.comboBox.setItemText(9, _translate("MainWindow", "History"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Horror"))
        self.comboBox.setItemText(11, _translate("MainWindow", "Music"))
        self.comboBox.setItemText(12, _translate("MainWindow", "Mystery"))
        self.comboBox.setItemText(13, _translate("MainWindow", "Romance"))
        self.comboBox.setItemText(14, _translate("MainWindow", "Sci-Fi"))
        self.comboBox.setItemText(15, _translate("MainWindow", "Thriller"))
        self.comboBox.setItemText(16, _translate("MainWindow", "War"))
        self.comboBox.setItemText(17, _translate("MainWindow", "Western"))
        self.pushButton_5.setText(_translate("MainWindow", "Search"))
        self.pushButton_5.clicked.connect(self.b5clicked)
        self.label_4.setText(_translate("MainWindow", "Genres :"))
        self.listWidget.itemClicked.connect(self.itemClicked)
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Popularity"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Year"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Rate"))
        self.lineEdit.returnPressed.connect(self.b1clicked)

    
    def b1clicked(self):
        global stype, numpic
        numpic = 0
        stype = "title"
        self.listWidget.clear()
        self.pushButton_4.setEnabled(False)
        self.executee("https://api.themoviedb.org/3/search/movie?api_key=f074077eac6b13f13cd586d06af0d486&language=en-US&query="+ self.lineEdit.text() +"&page=1&include_adult=false")
        
    def b5clicked(self):
        global dicti, stype, numpic, dicti_2, curOrder
        numpic = 0
        stype = "genres"
        self.listWidget.clear()
        curGenre = dicti[str(self.comboBox.currentText())]
        curOrder = dicti_2[str(self.comboBox_2.currentText())]
        self.pushButton_4.setEnabled(False)
        self.executee("https://api.themoviedb.org/3/discover/movie?api_key=f074077eac6b13f13cd586d06af0d486&language=en-US&sort_by="+ curOrder +"&include_adult=false&include_video=false&page=1&with_genres=" + curGenre)

    def b2clicked(self):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.getcwd() + '\\resim.jpg', 0)

    def b3clicked(self):
        global numpic,stype, curdur, dicti, curOrder, maxcur
        curdur = "forward"
        numpic += 1
        self.pushButton_4.setEnabled(True)
        if stype == "title":
            self.executee("https://api.themoviedb.org/3/search/movie?api_key=f074077eac6b13f13cd586d06af0d486&language=en-US&query="+ self.lineEdit.text() +"&page=1&include_adult=false")
        else:
            curGenre = dicti[str(self.comboBox.currentText())]
            self.executee("https://api.themoviedb.org/3/discover/movie?api_key=f074077eac6b13f13cd586d06af0d486&language=en-US&sort_by="+ curOrder +"&include_adult=false&include_video=false&page=1&with_genres=" + curGenre)
        
        if numpic == maxcur:
            self.pushButton_3.setEnabled(False)

    def b4clicked(self):
        global numpic,stype, curdur,dicti,curOrder
        curdur = "back"
        numpic -= 1
        if stype == "title":
            self.executee("https://api.themoviedb.org/3/search/movie?api_key=f074077eac6b13f13cd586d06af0d486&language=en-US&query="+ self.lineEdit.text() +"&page=1&include_adult=false")
        else:
            curGenre = dicti[str(self.comboBox.currentText())]
            self.executee("https://api.themoviedb.org/3/discover/movie?api_key=f074077eac6b13f13cd586d06af0d486&language=en-US&sort_by="+ curOrder +"&include_adult=false&include_video=false&page=1&with_genres=" + curGenre)
        
        self.pushButton_3.setEnabled(True)
        if numpic == 0:
            self.pushButton_4.setEnabled(False)
    
    def itemClicked(self):
        global numpic,dicti,curOrder
        numpic = self.listWidget.currentRow()
        if stype == "title":
            self.executee("https://api.themoviedb.org/3/search/movie?api_key=f074077eac6b13f13cd586d06af0d486&language=en-US&query="+ self.lineEdit.text() +"&page=1&include_adult=false")
        else:
            curGenre = dicti[str(self.comboBox.currentText())]
            self.executee("https://api.themoviedb.org/3/discover/movie?api_key=f074077eac6b13f13cd586d06af0d486&language=en-US&sort_by="+ curOrder +"&include_adult=false&include_video=false&page=1&with_genres=" + curGenre)

    def executee(self, curUrl):      
        try:
            self.listWidget.clear()
            response = requests.get(curUrl)
            getresults = response.json()['results']
            pictures = []
            titles = []
            global numpic, curdur, maxcur
            for d in getresults:
                try:
                    pic = d['backdrop_path'] 
                    pictures.append(pic)
                except :
                    pictures.append(None)
                        
                try:
                    title = d['title']
                except :
                    try:
                        title = d['name']
                    except :
                        title = d['original_title']
                                   
                titles.append(title)
                try:
                    self.listWidget.addItem(d['title'])
                except :
                    try:
                        title = d['name']
                    except :
                        title = d['original_title']
            

            while pictures[numpic] is None:
                if curdur == "back":
                    numpic -= 1
                else:
                    if numpic < maxcur:
                        numpic += 1                   
            
            maxcur = len(pictures)
            url = 'https://image.tmdb.org/t/p/original' + pictures[numpic]
            data = urllib.request.urlopen(url).read()
            urllib.request.urlretrieve(url,"resim.jpg")
            global pixmap
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            

            self.label_2.setPixmap(pixmap)
            self.label_5.setText(titles[numpic])
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.label_3.setText("")
        except :
            self.label_3.setText("Error !. Please enter valid value")
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            self.label_2.clear()
            self.lineEdit.setFocus()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
