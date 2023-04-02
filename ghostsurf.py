# This Python file uses the following encoding: utf-8

# MODULES AND/OR LIBRARIES
from os import system, popen, path
from pathlib import Path
from logging import basicConfig, DEBUG, debug, disable, CRITICAL
from time import sleep

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
# disable(CRITICAL)

# GLOBAL VARIABLES
# Creating a variable called base_dir which leads to the current working directory.
base_dir = path.dirname(__file__)

def manage_netfilter_service():
    """A function which starts and enables netfilter service if it's not"""

    # Checking if the netfilter-persistent service is inactive
    if 'inactive' in popen(f'systemctl status netfilter-persistent').read():
        # Starting the netfilter-persistent service
        system('sudo systemctl start netfilter-persistent')

    # Checking if the netfilter-persistent service is disabled
    if 'disabled' in popen(f'systemctl status netfilter-persistent').read():
        # Enabling the netfilter service
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
        
        # Creating a global variable called user_pwd
        global user_pwd
        # Initializing the user_pwd variable with the password_line_edit's text
        user_pwd = self.password_line_edit.text()
        # Getting the username and the root privileges
        user_name = popen(f'echo "{user_pwd}" | sudo -S whoami').read()
        # Checking if the username is equal to root
        if user_name == "root\n":
            # Closing password dialog window
            self.close()
            # Creating a main_window object from MainWindow class
            main_window = MainWindow()
            # Showing the main window
            main_window.show().exec_()

        # Checking if the username is not equal to root
        else:
            # Creating a warning dialog window
            warning_dialog = QMessageBox()
            # Setting the warning dialog window's icon
            warning_dialog.setIcon(QMessageBox.Critical)
            # Setting the dialog's window title
            warning_dialog.setWindowTitle("Warning")
            # Setting the warning dialog's text
            warning_dialog.setText("Couldn't get root privileges!")
            # Showing the warning dialog
            warning_dialog.exec_()

# Creating a MainWindow class
class MainWindow(QMainWindow, Ui_MainWindow):
    # Initializing the main window to make it self contained.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)

        # Checking tor services status
        tor_status = popen('systemctl status tor.service').read()

        # Checking if the tor service is inactive
        if "inactive" in tor_status:
            # Setting the status_label's stylesheet
            self.status_label.setStyleSheet(u"#status_label {color: red;}")
            # Setting the status_label's text to "inactive"
            self.status_label.setText('Inactive')

        # Checking if the tor service is active
        else:
            # Setting the status_label widget's stylesheet
            self.status_label.setStyleSheet(u"#status_label {color: green;}")
            # Setting the status_label's text to active
            self.status_label.setText('Active')
        
        # Connecting the start_stop_button with the start function in a way that the function will going to trigger with a press signal
        self.start_stop_button.pressed.connect(self.start)
        # Connecting the my_ip_button with the show_my_ip function in a way that the function will going to trigger with a press signal
        self.my_ip_button.pressed.connect(self.show_my_ip)
        # Connecting the status_button with the show_status function in a way that the function will going to trigger with a press signal
        self.status_button.pressed.connect(self.show_status)
        # Connecting the change_id_button with the change_id function in a way that the function will going to trigger with a press signal
        self.change_id_button.pressed.connect(self.change_id)

    def start(self):
        """A function which redirects all internet traffic over tor"""
        
        # Checking if the start_stop_button's text is equal to "Start"
        if self.start_stop_button.text() == "Start":
            # Printing "Start button pressed" in debug mode.
            debug("Start button pressed")
            # Executing the init script.
            system('sudo bash /opt/ghostsurf/bash_scripts/init.sh')
            # Executing the start script.
            system('sudo bash /opt/ghostsurf/bash_scripts/start_transparent_proxy.sh')
            # Changing the start_stop_button's text value to Stop.
            self.start_stop_button.setText("Stop")
        
        # Checking if the start_stop_button's text is not equal to "Start"
        else:
            # Printing "Stop button pressed" in debug mode
            debug("Stop button pressed")
            # Executing the init script.
            system('sudo bash /opt/ghostsurf/bash_scripts/init.sh')
            # Executing the stop script.
            system('sudo bash /opt/ghostsurf/bash_scripts/stop_transparent_proxy.sh')
            # Changing the start_stop_button's text value to Stop.
            self.start_stop_button.setText("Start")

        # Reading the tor service's status by running a system command.
        tor_status = popen('systemctl status tor.service').read()

        # Checking if tor service is inactive
        if "inactive" in tor_status:
            # Setting the status_label widget's stylesheet
            self.status_label.setStyleSheet(u"#status_label {color: red;}")
            # Setting the status_label's text to "Inactive"
            self.status_label.setText('Inactive')

        # Checking if tor service is active
        else:
            # Setting the status_label widget's stylesheet
            self.status_label.setStyleSheet(u"#status_label {color: green;}")
            # Setting the status_label's text to "Active"
            self.status_label.setText('Active')

    def show_my_ip(self):
        """A function which shows your public ip address"""

        # Trying to send a get request to ipinfo.io to get the device's public ip address
        try:
            # Sending a get request to "https://ifconfig.io" to get the user's public ip address.
            users_ip_address = popen("curl https://ifconfig.io").read()[:-1]

            # Checking if "Could not resolve host: ifconfig.io" is not in the users_ip_addres variable
            if "Could not resolve host: ifconfig.io" not in users_ip_address:
                # Setting the ip_address_label's text value to device's public ip address
                self.ip_address_label.setText(users_ip_address)
                # Setting the ip_address_label's stylesheet
                self.ip_address_label.setStyleSheet(u"#ip_address_label {color: white;}")

            # Checking if "Could not resolve host: ifconfig.io" is in the users_ip_addres variable
            else:
                # Setting the ip_address_label's text value to device's public ip address
                self.ip_address_label.setText(users_ip_address)
                # Setting the ip_address_label's stylesheet
                self.ip_address_label.setStyleSheet(u"#ip_address_label {color: white;}")

        # Instructing the computer about what to do if the application fails to send a post request
        except:
            # Setting the ip_address_label's text to "Request Failed"
            self.ip_address_label.setText("Request Failed")
            # Setting the ip_address_label's stylesheet
            self.ip_address_label.setStyleSheet(u"#ip_address_label {color: red;}")

    def show_status(self):
        """A function which shows the tor service's status"""

        # Reading tor services status from a system command
        tor_status = popen('systemctl status tor.service').read()

        # Checking if tor service is inactive
        if "inactive" in tor_status:
            # Setting the status_label's stylesheet
            self.status_label.setStyleSheet(u"#status_label {color: red;}")
            # Setting the status_label's text to "Inactive"
            self.status_label.setText('Inactive')
        
        # Checking if tor service is active
        else:
            # Setting the status_label's stylesheet
            self.status_label.setStyleSheet(u"#status_label {color: green;}")
            # Setting the status_label's text to "Active"
            self.status_label.setText('Active')

    def change_id(self):
        """A function which changes your ip address by restarting the transparent proxy"""

        # Executing the init script
        system('sudo bash /opt/ghostsurf/bash_scripts/init.sh')
        # Executing the stop_transparent_proxy script
        system('sudo bash /opt/ghostsurf/bash_scripts/stop_transparent_proxy.sh')
        # Executing the start_transparent_proxy script
        system('sudo bash /opt/ghostsurf/bash_scripts/start_transparent_proxy.sh')


# Evaluate if the source is being run on its own or being imported somewhere else. With this conditional in place, your code can not be imported somewhere else.
if __name__ == "__main__":
    # Creating an app object from QApplication
    app = QApplication([])
    # Creating a password_dialog object from PasswordDialog class
    password_dialog = PasswordDialog()
    # Showing the password dialog
    password_dialog.show()
    # Executing the app
    app.exec_()
