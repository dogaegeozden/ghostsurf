# This Python file uses the following encoding: utf-8

# MODULES AND/OR LIBRARIES
from sys import exit
from os import system, popen
from requests import get
from pathlib import Path
from logging import basicConfig, DEBUG, debug, disable, CRITICAL
from os import path

# PySide2
from PySide2.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QLineEdit
from PySide2.QtGui import QPixmap, QIcon

# Guis
from guis.main_win_ui import Ui_MainWindow
from guis.password_win_ui import Ui_PasswordDialog

# Resources
import resources_rc

# Configuring debugging feature code
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disabling the debugging feature. Hint: Comment out this line to enable debugging.
disable(CRITICAL)

# GLOBAL VARIABLES
# Creating a variable called base_dir which leads to the current working directory.
base_dir = path.dirname(__file__)

def manage_netfilter_service():
    """A function which starts and enables netfilter service if it's not"""
    if 'inactive' in popen(f'systemctl status netfilter-persistent').read():
        system('sudo systemctl start netfilter-persistent')
    if 'disabled' in popen(f'systemctl status netfilter-persistent').read():
        system(f'sudo systemctl enable netfilter-persistent')


# Creating a dialog class called CreateNewSafeDialog
class PasswordDialog(QDialog, Ui_PasswordDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)

        # Connecting the submit button with the get_user_pwd function in a way that the function will going to trigger with a press signal.
        self.submit_button.pressed.connect(self.get_user_pwd)

        # Connecting the visibility_button with the change_echo_mode function in a way that the function will going to trigger with a press signal.
        self.visibility_button.pressed.connect(self.change_echo_mode)

    def change_echo_mode(self):
        """A function which changes the echo mode to hide and display the password"""
        # Creating a variable called echo_mode which is equal to the password_line_edit wiget's echo mode
        echo_mode = self.password_line_edit.echoMode()
        # Checking if the echo mode of the password_line_edit widget is Password
        if echo_mode == QLineEdit.EchoMode.Password:
            # Changing the widget's echo mode to Normal
            self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
            # Creating an icon
            open_eye_icon = QIcon()
            # Adding pixmap to the icon
            open_eye_icon.addPixmap(QPixmap(str(Path(base_dir, "icons", "eye_open.svg"))))
            # Setting the eye_button's icon
            self.visibility_button.setIcon(open_eye_icon)
        # Checking if the echo mode of the password_line_edit widget is not Password
        else:
            # Changing the widget's echo mode to Password
            self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
            # Creating an icon
            closed_eye_icon = QIcon()
            # Adding pixmap to the icon
            closed_eye_icon.addPixmap(QPixmap(str(Path(base_dir, "icons", "eye_closed.svg"))))
            # Setting the eye_button's icon
            self.visibility_button.setIcon(closed_eye_icon)

    def get_user_pwd(self):
        """A function which stores the password that the user entered in a global variable"""
        global user_pwd 
        user_pwd = self.password_line_edit.text()
        user_name = popen(f'echo "{user_pwd}" | sudo -S whoami').read()
        if user_name == "root\n":
            self.close()
            main_window = MainWindow()
            main_window.show().exec_()

        else:
            warning_dialog = QMessageBox()
            warning_dialog.setIcon(QMessageBox.Critical)
            warning_dialog.setWindowTitle("Warning")
            warning_dialog.setText("Couldn't get root priviledges!")
            warning_dialog.exec_()

# Creating a MainWindow class
class MainWindow(QMainWindow, Ui_MainWindow):
    # Initializing the main window to make it self contained.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)

        tor_status = popen('systemctl status tor.service').read()
        if "inactive" in tor_status:
            self.status_label.setStyleSheet(u"#status_label {color: red;}")
            self.status_label.setText('Inactive')
        else:
            self.status_label.setStyleSheet(u"#status_label {color: green;}")
            self.status_label.setText('Active')
        
        self.start_stop_button.pressed.connect(self.start)
        self.my_ip_button.pressed.connect(self.show_my_ip)
        self.status_button.pressed.connect(self.show_status)
        self.change_id_button.pressed.connect(self.change_id)

    def start(self):
        """A function which redirects all internet traffic over tor"""
        if self.start_stop_button.text() == "Start":
            # Print that the start button is pressed in debug mode.
            debug("Start button pressed")
            # Executing the init script.
            system('sudo bash /opt/ghostsurf/bash_scripts/init.sh')
            # Executing the start script.
            system('sudo bash /opt/ghostsurf/bash_scripts/start_transparent_proxy.sh')
            # Changing the start_stop_button's text value to Stop.
            self.start_stop_button.setText("Stop")
            
        else:
            debug("Stop button pressed")
            # Executing the init script.
            system('sudo bash /opt/ghostsurf/bash_scripts/init.sh')
            # Executing the stop script.
            system('sudo bash /opt/ghostsurf/bash_scripts/stop_transparent_proxy.sh')
            # Changing the start_stop_button's text value to Stop.
            self.start_stop_button.setText("Start")

        # Reading the tor service's status by running a system command.
        tor_status = popen('systemctl status tor.service').read()

        if "inactive" in tor_status:
            self.status_label.setStyleSheet(u"#status_label {color: red;}")
            self.status_label.setText('Inactive')
        else:
            self.status_label.setStyleSheet(u"#status_label {color: green;}")
            self.status_label.setText('Active')

    def show_my_ip(self):
        """A function which shows your public ip address"""
        try:
            # Sending a get request to "https://ipinfo.io" to get the user's public ip address.
            users_ip_address = get("https://ipinfo.io", headers={'Accept': 'application/json'}).json()['ip']
            # Setting the ip_address_label's text value
            self.ip_address_label.setText(users_ip_address)
            self.ip_address_label.setStyleSheet(u"#ip_address_label {color: white;}")

        except:
            self.ip_address_label.setText("Request Failed")
            self.ip_address_label.setStyleSheet(u"#ip_address_label {color: red;}")


    def show_status(self):
        """A function which shows the tor service's status"""
        tor_status = popen('systemctl status tor.service').read()

        if "inactive" in tor_status:
            self.status_label.setStyleSheet(u"#status_label {color: red;}")
            self.status_label.setText('Inactive')
        else:
            self.status_label.setStyleSheet(u"#status_label {color: green;}")
            self.status_label.setText('Active')

    def change_id(self):
        """A function which changes your ip address by restarting the tor service"""
        # Executing the init script.
        system('sudo bash /opt/ghostsurf/bash_scripts/init.sh')
        system('sudo systemctl restart tor')

if __name__ == "__main__":
    app = QApplication([])
    password_dialog = PasswordDialog()
    password_dialog.show()
    exit(app.exec_())
