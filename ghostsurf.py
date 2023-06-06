# This Python file uses the following encoding: utf-8

# MODULES AND/OR LIBRARIES
from os import system, popen, path
from pathlib import Path
from logging import basicConfig, DEBUG, debug, disable, CRITICAL
from webbrowser import open as wbopen
from threading import Thread
from time import sleep
from bs4 import BeautifulSoup
from re import compile

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
    if 'inactive' in popen(f'echo "{user_pwd}" | sudo -S systemctl status netfilter-persistent').read():

        # Starting the netfilter-persistent service
        system(f'echo {user_pwd} | sudo -S systemctl start netfilter-persistent')

    # Checking if the netfilter-persistent service is disabled
    if 'disabled' in popen(f'echo "{user_pwd}" | sudo -S systemctl status netfilter-persistent').read():

        # Enabling the netfilter service
        system(f'echo {user_pwd} | sudo -S systemctl enable netfilter-persistent')

def wipe_the_memory():
    """A function which drops caches, wipes the memory securely and notifies the user"""

    # Creating a question dialog window
    question_dialog = QMessageBox()

    # Setting the question dialog window's icon
    question_dialog.setIcon(QMessageBox.Question)

    # Setting the dialog's window title
    question_dialog.setWindowTitle("Important")

    # Setting the question dialog's text
    question_dialog.setText("Do you want fast and less secure operation?")

    # Setting standard buttons
    question_dialog.setStandardButtons(QMessageBox.No | QMessageBox.Yes)

    # Showing the question dialog
    question_dialog.exec_()

    # Checking no button is clicked
    if question_dialog == QMessageBox.No:

        # Sending a notification to inform the user that the process is starting
        system(f'notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Trying to wipe the memory and drop caches. This might take some time!"')

        # Executing the bomb.sh file to wipe the memory securely
        system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/secure_bomb.sh"')

        # Sending a notification to let the user know what the application just did
        system(f'notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Caches are dropped and memory is wiped"')
    
    # Checking if the no button is not clicked
    else:

        # Sending a notification to inform the user that the process is starting
        system(f'notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Trying to wipe the memory and drop caches. This might take some time!"')

        # Executing the bomb.sh file to wipe the memory securely
        system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/fast_bomb.sh"')

        # Sending a notification to let the user know what the application just did
        system(f'notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Caches are dropped and memory is wiped"')


def get_the_public_ip_address():
    """A function which tries to displays the user's public ip address with notifications"""

    # Waiting for 1.5 seconds
    sleep(1.5)

    # Sending notification to let the user know that the application is trying to connect to the server
    system(f'notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Trying to connect to the server"')

    # Waiting for 1.5 seconds
    sleep(1.5)

    # Trying to execute the code block that is located inside this block
    try:
        # Sending a get request to "https://ifconfig.io" to get the public ip address.
        public_ip_address = popen(f'echo "{user_pwd}" | sudo -S curl --connect-timeout 14.15 "https://ifconfig.io"').read()[:-1]

        # Creating a pattern for ip address validation
        ip_addr_regex = compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}')
        
        # Checking if the get request's response is an ip address
        result = ip_addr_regex.search(public_ip_address).group()

        # Checking if pattern validation's result is equal to the get request's response
        if result == public_ip_address:

            # Creating a message that contain's the public ip address
            message = f'Your public ip address is {public_ip_address}'

        # Checking if the pattern validation's result is not equal to the get request's response
        else:
            
            # Creating a message that says "Couldn't connect to the server!"
            message = "Couldn't connect to the server!"


    # Instructing the computer about what to do if the application fails to send execute the code which is inside the try block
    except:

        # Creating a message that informs the user that it can't connect to the internet
        message = "Couldn't connect to the server!"

    # Sending notification
    system(f'notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "{message}"')

# Creating a dialog class called PasswordDialog
class PasswordDialog(QDialog, Ui_PasswordDialog):

    def __init__(self, *args, **kwargs):
        """An init function which makes the window self contained""" 

        # Calling super function with init
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

    def __init__(self, *args, **kwargs):
        """An init function which makes the window self contained""" 
        
        # Calling super function with init
        super().__init__(*args, **kwargs)

        # Loading the GUI
        self.setupUi(self)

        # Checking tor services status
        tor_status = popen(f'echo "{user_pwd}" | sudo -S systemctl status tor.service').read()

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
        
        # Connecting the start_stop_button with the start_stop function in a way that the function will going to trigger with a press signal
        self.start_stop_button.pressed.connect(self.start_stop)

        # Connecting the my_ip_button with the show_my_ip function in a way that the function will going to trigger with a press signal
        self.my_ip_button.pressed.connect(self.show_my_ip)

        # Connecting the status_button with the show_status function in a way that the function will going to trigger with a press signal
        self.status_button.pressed.connect(self.show_status)

        # Connecting the change_id_button with the change_id function in a way that the function will going to trigger with a press signal
        self.change_id_button.pressed.connect(self.change_id)

        # Connecting the info_button with the open_info_page function in a way that the function will going to trigger with a press signal
        self.info_button.pressed.connect(self.open_info_page) 

        # Connecting the pandora_bomb_button with the wipe_memory_securely function in a way that the function will going to trigger with a press signal
        self.pandora_bomb_button.pressed.connect(self.wipe_memory_securely)

    def wipe_memory_securely(self):
        """A function which wipes the memory securely"""

        # Creating a thread that targerts the wipe_the_memory function
        wipe_memory_thread = Thread(target=wipe_the_memory)

        # Starting the thread
        wipe_memory_thread.start()

    def open_info_page(self):
        """A function which opens the info page in the default browser"""

        # Opening the info page of this application in the default browser
        wbopen("https://www.github.com/dogaegeozden/ghostsurf")

    def start_stop(self):
        """A function which redirects all internet traffic over tor"""
        
        # Checking if the start_stop_button's text is equal to "Start"
        if self.start_stop_button.text() == "Start":

            # Printing "Start button pressed" in debug mode.
            debug("Start button pressed")

            # Creating a question dialog window
            question_dialog = QMessageBox()

            # Setting the question dialog window's icon
            question_dialog.setIcon(QMessageBox.Question)

            # Setting the dialog's window title
            question_dialog.setWindowTitle("Important")

            # Setting the question dialog's text
            question_dialog.setText("Are you allowing to killing of dangerous applications and cleaning of dangerous caches?")

            # Setting standard buttons
            question_dialog.setStandardButtons(QMessageBox.No | QMessageBox.Yes)

            # Showing the question dialog
            question_dialog.exec_()

            # Checking yes button is clicked
            if question_dialog == QMessageBox.Yes:

                # Executing the init script.
                system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/init.sh"')

                # Executing the start script.
                system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/start_transparent_proxy.sh"')
            
            # Checking if the yes button is not clicked
            else:

                # Executing the start script.
                system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/start_transparent_proxy.sh"')

            # Changing the start_stop_button's text value to Stop.
            self.start_stop_button.setText("Stop")
        
        # Checking if the start_stop_button's text is not equal to "Start"
        else:

            # Printing "Stop button pressed" in debug mode
            debug("Stop button pressed")

            # Creating a question dialog window
            question_dialog = QMessageBox()

            # Setting the question dialog window's icon
            question_dialog.setIcon(QMessageBox.Question)

            # Setting the dialog's window title
            question_dialog.setWindowTitle("Important")

            # Setting the question dialog's text
            question_dialog.setText("Are you allowing to killing of dangerous applications and cleaning of dangerous caches?")

            # Setting standard buttons
            question_dialog.setStandardButtons(QMessageBox.No | QMessageBox.Yes)

            # Showing the question dialog
            question_dialog.exec_()

            # Checking yes button is clicked
            if question_dialog == QMessageBox.Yes:

                # Executing the init script.
                system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/init.sh"')

                # Executing the stop script.
                system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/stop_transparent_proxy.sh"')

            # Checking if the yes button is not clicked
            else:

                # Executing the stop script.
                system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/stop_transparent_proxy.sh"')

            # Changing the start_stop_button's text value to Stop.
            self.start_stop_button.setText("Start")

        # Reading the tor service's status by running a system command.
        tor_status = popen(f'echo "{user_pwd}" | sudo -S systemctl status tor.service').read()

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
        
        # Creating a thread start uses the get_the_public_ip_address function 
        public_ip_thread = Thread(target=get_the_public_ip_address)

        # Starting the thread
        public_ip_thread.start()

    def show_status(self):
        """A function which shows the tor service's status"""

        # Reading tor services status from a system command
        tor_status = popen(f'echo "{user_pwd}" | sudo -S systemctl status tor.service').read()

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

        # Restarting the tor service to change the ip address.
        system(f'echo "{user_pwd}" | sudo -S systemctl restart tor')

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
