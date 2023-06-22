# This Python file uses the following encoding: utf-8

# MODULES AND/OR LIBRARIES
from os import system, popen, path
from pathlib import Path
from logging import basicConfig, DEBUG, debug, disable, CRITICAL
from webbrowser import open as wbopen
from threading import Thread
from time import sleep
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

def main():
    """The function which runs the entire application"""

    # Creating an app object from QApplication
    app = QApplication([])

    # Creating a password_dialog object from PasswordDialog class
    password_dialog = PasswordDialog()

    # Showing the password dialog
    password_dialog.show()

    # Executing the app
    app.exec_()
            
def reset_ghostsurf_settings():
    """A function which resets the ghostsurf settings"""

    # Sending a notification to inform the user that the operation is starting
    system('notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Executing the reset.sh script"')

    # Executing the reset.sh script.
    system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/reset.sh"')

    # Sending a notification to inform the user that the operation is done
    system('notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Reseting is done"')

def kill_log_files():
    """A function which overrides the log files in the system"""
    
    # Sending a notification to inform the user that the operation is starting
    system('notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Executing the log_shredder.sh script"')

    # Executing the mac_changer script.
    system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/mac_changer.sh"')

    # Sending a notification to inform the user that the operation is done
    system('notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Log shredding is done"')

def change_the_mac_address():
    """A function which changes the mac address"""

    def mac_changer_button_question_dialog_processor(i):
        """A function which checks the user's answer for the mac changer question and instructs the computer about what to do based on that answer"""

        # Getting the user's answer from the i's text value to identify if the user pressed to yes or no
        user_answer = i.text()

        # Checking if the user pressed to the yes button.
        if user_answer == "&Yes":
            
            # Getting the active internet adaptors name 
            internet_adaptor_name = popen("ip route show default | awk '/default/ {print $5}'").read()[:-1]

            # Executing the mac_changer script.
            system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/mac_changer.sh"')

            # Waiting for 4 seconds
            sleep(4)

            # Connecting to internet
            system(f'echo "{user_pwd}" | sudo -S nmcli d connect {internet_adaptor_name}')

            # Sending a notification to inform the user that the operation is done
            system('notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Mac address has been changed"')

        # Checking if the user pressed to the no button
        elif user_answer == "&No":
            
            # Executing the mac_changer script.
            system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/mac_changer.sh"')

            # Sending a notification to inform the user that the operation is done
            system('notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Mac Changing operation is done"')

        # Checking if the didn't pressed to bot yes and not buttons 
        else:

            # Printing "Operation canceled in debug mode"
            debug("Operation canceled")


    # Sending a notification to inform the user that the operation is starting
    system('notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Changing the mac address"')

    # Creating a question dialog window
    question_dialog = QMessageBox()

    # Setting the question dialog window's icon
    question_dialog.setIcon(QMessageBox.Question)

    # Setting the dialog's window title
    question_dialog.setWindowTitle("Important")

    # Setting the question dialog's text
    question_dialog.setText("Do you want connect back to internet?")

    # Setting standard buttons
    question_dialog.setStandardButtons(QMessageBox.No | QMessageBox.Yes)

    # Adding functionality to Yes and No buttons
    question_dialog.buttonClicked.connect(mac_changer_button_question_dialog_processor)

    # Showing the question dialog
    question_dialog.exec_()

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

    def wipe_button_question_dialog_processor(i):
        """A function which process the input coming from the dialog box that is opened after the wipe button is pressed to identify what app should do"""
        
        # Getting the user's answer from the i's text value to identify if the user pressed to yes or no
        user_answer = i.text()

        # Checking if the user pressed to the yes button.
        if user_answer == "&Yes":
            
            # Sending a notification to inform the user that the process is starting
            system(f'notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Trying to wipe the memory and drop caches. This might take some time!"')

            # Executing the bomb.sh file to wipe the memory securely
            system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/fast_bomb.sh"')

            # Sending a notification to let the user know what the application just did
            system(f'notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Caches are dropped and memory is wiped"')
            
        # Checking if the user pressed to the no button
        elif user_answer == "&No":

            # Sending a notification to inform the user that the process is starting
            system('notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Trying to wipe the memory and drop caches. This might take some time!"')

            # Executing the bomb.sh file to wipe the memory securely
            system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/secure_bomb.sh"')

            # Sending a notification to let the user know what the application just did
            system(f'notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Caches are dropped and memory is wiped"')

        # Checking if the didn't pressed to bot yes and not buttons 
        else:

            # Printing "Operation canceled in debug mode"
            debug("Operation canceled")

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

    # Adding functionality to Yes and No buttons
    question_dialog.buttonClicked.connect(wipe_button_question_dialog_processor)

    # Showing the question dialog
    question_dialog.exec_()

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
        
        # Opening the ghostsurf.conf file in reading mode
        with open("/opt/ghostsurf/configuration_files/ghostsurf.conf", "r") as c:
            
            # Reading the lines of ghostsurf.conf file
            c_contents = c.readlines()

            # Checking if "enabled_at_boot=yes" is in the line
            if "enabled_at_boot=yes\n" in c_contents:

                # Creating a variable to keep track if ghostsurf is enabled at boot
                is_ghostsurf_enabled_at_boot = True

            # Checking if "enabled_at_boot=no" is not in the line
            else:

                # Creating a variable to keep track if ghostsurf is enabled at boot
                is_ghostsurf_enabled_at_boot = False

        # Checking if is_ghostsurf_enabled_at_boot is equal to True
        if is_ghostsurf_enabled_at_boot == True: 

            # Changing the start_stop_button's text value to "Stop".
            self.start_stop_button.setText("Stop")

            # Setting the status_label widget's stylesheet
            self.status_label.setStyleSheet(u"#status_label {color: green;}")

            # Setting the status_label's text to "Active"
            self.status_label.setText('Active')
            
            # Changing the ultra_ghost_button's text to "enabled"
            self.ultra_ghost_button.setText("enabled")

            # Setting the style sheet of the ultra_ghost_button 
            self.ultra_ghost_button.setStyleSheet(u"#ultra_ghost_button {background: #00ff00; border-radius: 4px; border: 1px solid black}")

        # Checking if is_ghostsurf_enabled_at_boot is not equal to True
        else:

            # Changing the start_stop_button's text value to "Start".
            self.start_stop_button.setText("Start")

            # Setting the status_label widget's stylesheet
            self.status_label.setStyleSheet(u"#status_label {color: red;}")

            # Setting the status_label's text to "Inactive"
            self.status_label.setText('Inactive')
            
            # Changing the ultra_ghost_button's text to "disabled"
            self.ultra_ghost_button.setText("disabled")

            # Setting the style sheet of the ultra_ghost_button 
            self.ultra_ghost_button.setStyleSheet(u"#ultra_ghost_button {background: red; border-radius: 4px; border: 1px solid black}")

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

        # Connecting the change_ip_button with the change_id function in a way that the function will going to trigger with a press signal
        self.change_ip_button.pressed.connect(self.change_id)

        # Connecting the info_button with the open_info_page function in a way that the function will going to trigger with a press signal
        self.info_button.pressed.connect(self.open_info_page) 

        # Connecting the pandora_bomb_button with the wipe_memory_securely function in a way that the function will going to trigger with a press signal
        self.pandora_bomb_button.pressed.connect(self.wipe_memory_securely)

        # Connecting the ultra_ghost_button with the ultra_ghost_mode function in a way that the function will going to trigger with a press signal
        self.ultra_ghost_button.pressed.connect(self.ultra_ghost_mode)

        # Connecting the mac_changer_button with the change_mac_address function in a way that the function will going to trigger with a press signal
        self.mac_changer_button.pressed.connect(self.change_mac_address)

        # Connecting the log_shredder_button with the shred_log_files function in a way that the function will going to trigger with a press signal
        self.log_shredder_button.pressed.connect(self.shred_log_files)

        # Connecting the reset_button with the reset_settings function in a way that the function will going to trigger with a press signal
        self.reset_button.pressed.connect(self.reset_settings)

        # Connecting the dns_changer_button with the change_dns function in a way that the function will going to trigger with a press signal
        self.dns_changer_button.pressed.connect(self.change_dns)

        # Connecting the hostname_changer_button with the change_hostname function in a way that the function will going to trigger with a press signal
        self.hostname_changer_button.pressed.connect(self.change_hostname)


    def change_hostname(self):
        """A function which changes the hostname"""

        # Creating a question dialog window
        question_dialog = QMessageBox()

        # Setting the question dialog window's icon
        question_dialog.setIcon(QMessageBox.Question)

        # Setting the dialog's window title
        question_dialog.setWindowTitle("Important")

        # Setting the question dialog's text
        question_dialog.setText("This operation requires reboot. Do you allow to reboot this system?")

        # Setting standard buttons
        question_dialog.setStandardButtons(QMessageBox.No | QMessageBox.Yes)

        # Showing the question dialog
        question_dialog_answer = question_dialog.exec_()

        # Checking if the user pressed to the yes button.
        if question_dialog_answer == QMessageBox.Yes:

            # Priting what's going on in debug mode
            debug("Rebooting the system")

            # Executing the stop script
            system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/stop_transparent_proxy.sh"')

            # Executing the hostname_changer script
            system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/hostname_changer.sh"')

            # Rebooting the system
            system(f'echo "{user_pwd}" | sudo -S reboot')

        # Checking if user didn't pressed to the yes button
        else:

            # Printing "Operation canceled" in debug mode
            debug("Operation canceled")


    def change_dns(self):
        """A function which changes the nameservers in the resolv.conf file"""

        # Sending a notification to inform the user that the operation is starting
        system('notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Changing the nameservers"')

        # Getting the working status of the application from the start_stop_button's text
        working_status = self.start_stop_button.text()

        # Checking if transparent proxy is on
        if working_status == "Stop":
            
            # Copying and pasting custom nameservers for tor on resolv.conf file
            system(f'echo "{user_pwd}" | sudo -S cp "/opt/ghostsurf/configuration_files/resolv.conf.custom" "/etc/resolv.conf"')

        # Checking if transparent proxy is off
        else:

            # Copying and pasting dns_changer nameservers to on resolv.conf file
            system(f'echo "{user_pwd}" | sudo -S cp "/opt/ghostsurf/configuration_files/dns_changer.resolv.conf" "/etc/resolv.conf"')

        # Sending a notification to inform the user that the operation is done
        system('notify-send -i "/opt/ghostsurf/icons/ghostsurf.png" -t 300 "Nameservers has been changed"')

    def reset_settings(self):
        """A function which resets ghostsurf settings"""

        # Creating a thread that resets the ghostsurf settings
        reset_thread = Thread(target=reset_ghostsurf_settings)

        # Starting the thread
        reset_thread.start()


    def shred_log_files(self):
        """A function which shreds the log files"""

        # Creating a thread that kills the log files
        log_kill_thread = Thread(target=kill_log_files)

        # Starting the thread
        log_kill_thread.start()


    def change_mac_address(self):
        """A function which changes the mac address"""
        
        # Creating a thread that changes the mac address
        mac_changer_thread = Thread(target=change_the_mac_address)

        # Starting the thread
        mac_changer_thread.start()


    def ultra_ghost_mode(self):
        """A function which enables/disables ghostsurf at boot"""

        # Getting the ultra ghost mode's status from the button's text
        ultra_ghost_mode_status = self.ultra_ghost_button.text()

        # Checking if ultra_ghost_mode_status is equal to "disabled"
        if ultra_ghost_mode_status == "disabled":

            # Printing what's going on in debug mode
            debug("Enabling ghostsurf at boot")

            # Executing the start script
            system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/start_transparent_proxy.sh"')

            # Executing the save script
            system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/save_iptables_rules.sh"')

            # Opening the ghostsurf.conf file in read mode
            with open("/opt/ghostsurf/configuration_files/ghostsurf.conf", "r") as a:

                # Reading the lines of the ghostsurf.conf file
                a_contents = a.readlines()
                    
                # Checking if "enabled_at_boot=no\n"" is in the list of lines
                if "enabled_at_boot=no\n" in a_contents:
                    
                    # Finding the index number of "enabled_at_boot=no\n" string
                    line_index = a_contents.index("enabled_at_boot=no\n")

                    # Updating the a_contents list
                    a_contents[line_index]="enabled_at_boot=yes\n"

            # Opening the ghostsurf.conf file in write mode
            with open("/opt/ghostsurf/configuration_files/ghostsurf.conf", "w") as b:

                # Writing the new contents to file
                b.write('\n'.join(a_contents))

            # Changing the start_stop_button's text value to "Stop".
            self.start_stop_button.setText("Stop")

            # Setting the status_label widget's stylesheet
            self.status_label.setStyleSheet(u"#status_label {color: green;}")

            # Setting the status_label's text to "Active"
            self.status_label.setText('Active')
            
            # Changing the ultra_ghost_button's text to "enabled"
            self.ultra_ghost_button.setText("enabled")

            # Setting the style sheet of the ultra_ghost_button 
            self.ultra_ghost_button.setStyleSheet(u"#ultra_ghost_button {background: #00ff00; border-radius: 4px; border: 1px solid black}")

        # Checking if ultra_ghost_mode_status is not equal to "disabled"
        else:

            # Printing what's going on in debug mode
            debug("Disabling ghostsurf at boot")

            # Executing the stop script
            system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/stop_transparent_proxy.sh"')

            # Opening the ghostsurf.conf file in read mode
            with open("/opt/ghostsurf/configuration_files/ghostsurf.conf", "r") as a:
                
                # Reading the lines of ghostsurf.conf file and creating a list out of them
                a_contents = a.readlines()

                # Checking if "enabled_at_boot=enabled" is in the line
                if "enabled_at_boot=yes\n" in a_contents:
                    
                    # Finding the index of the line
                    line_index = a_contents.index("enabled_at_boot=yes\n")

                    # Changing the line corresponding to the index number
                    a_contents[line_index]="enabled_at_boot=no\n"

            # Opening the ghostsurf.conf file in write mode
            with open("/opt/ghostsurf/configuration_files/ghostsurf.conf", "w") as b:
                
                # Writing the new contents in to file
                b.write('\n'.join(a_contents))

            # Changing the start_stop_button's text value to "Start".
            self.start_stop_button.setText("Start")

            # Setting the status_label widget's stylesheet
            self.status_label.setStyleSheet(u"#status_label {color: red;}")

            # Setting the status_label's text to "Inactive"
            self.status_label.setText('Inactive')
            
            # Changing the ultra_ghost_button's text to "disabled"
            self.ultra_ghost_button.setText("disabled")

            # Setting the style sheet of the ultra_ghost_button 
            self.ultra_ghost_button.setStyleSheet(u"#ultra_ghost_button {background: red; border-radius: 4px; border: 1px solid black}")
            

    def wipe_memory_securely(self):
        """A function which wipes the memory securely"""

        # Creating a thread that targerts the wipe_the_memory function
        wipe_memory_thread = Thread(target=wipe_the_memory)

        # Starting the thread
        wipe_memory_thread.start()

    def open_info_page(self):
        """A function which opens the info page in the default browser"""

        # Opening the info page of this application in the default browser
        wbopen("https://www.github.com/dogaegeozden/ghostsurf#readme")


    def start_stop(self):
        """A function which redirects all internet traffic over tor"""

        def start_button_question_dialog_processor(i):
            """A function which process the input coming from the dialog box that is opened after the start button is pressed to identify what app should do"""

            # Getting the user's answer from the i's text value to identify if the user pressed to yes or no
            user_answer = i.text()

            # Checking if the user pressed to the yes button.
            if user_answer == "&Yes":

                # Printing the name of the button that is clicked in debug mode
                debug("Yes button is clicked")

                # Executing the init script.
                system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/init.sh"')

                # Executing the start script
                system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/start_transparent_proxy.sh"')

                # Changing the start_stop_button's text value to Stop.
                self.start_stop_button.setText("Stop")

            # Checking if the user pressed to the no button
            elif user_answer == "&No":

                # Printing the name of the button that is clicked in debug mode
                debug("No button is clicked")

                # Executing the start script
                system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/start_transparent_proxy.sh"')

                # Changing the start_stop_button's text value to Stop.
                self.start_stop_button.setText("Stop")

            # Checking if the didn't pressed to bot yes and not buttons 
            else:

                # Printing "Operation canceled in debug mode"
                debug("Operation canceled")

        
        def stop_button_question_dialog_processor(i):
            """A function which process the input coming from the dialog box that is opened after the stop button is pressed to identify what app should do"""

            # Getting the user's answer from the i's text value to identify if the user pressed to yes or no
            user_answer = i.text()

            # Checking if the user pressed to the yes button.
            if user_answer == "&Yes":

                 # Executing the init script.
                system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/init.sh"')

                # Executing the stop script.
                system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/stop_transparent_proxy.sh"')

                # Opening the ghostsurf.conf file in read mode
                with open("/opt/ghostsurf/configuration_files/ghostsurf.conf", "r") as d:

                    # Reading the lines of the file
                    d_contents = d.readlines()

                    # Checking if "enabled_at_boot=yes\n" in the list of lines
                    if "enabled_at_boot=yes\n" in d_contents:
                        
                        # Finding the index number of the line corresponding to the string
                        line_index = d_contents.index("enabled_at_boot=yes\n")

                        # Modiftying the list item corresponding to the index number
                        d_contents[line_index] = "enabled_at_boot=no\n"

                # Opening the ghostsurf.conf file in write mode
                with open("/opt/ghostsurf/configuration_files/ghostsurf.conf", "w") as e:

                    # Writing the new contents into file
                    e.write("\n".join(d_contents))

                # Changing the start_stop_button's text value to Stop.
                self.start_stop_button.setText("Start")

                # Changing the ultra_ghost_button's text to "disabled"
                self.ultra_ghost_button.setText("disabled")

                # Setting the style sheet of the ultra_ghost_button 
                self.ultra_ghost_button.setStyleSheet(u"#ultra_ghost_button {background: red; border-radius: 4px; border: 1px solid black}")

            # Checking if the user pressed to the no button
            elif user_answer == "&No":

                # Executing the stop script.
                system(f'echo "{user_pwd}" | sudo -S "/opt/ghostsurf/bash_scripts/stop_transparent_proxy.sh"')

                # Opening the ghostsurf.conf file in read mode
                with open("/opt/ghostsurf/configuration_files/ghostsurf.conf", "r") as d:

                    # Reading the lines of the file
                    d_contents = d.readlines()

                    # Checking if "enabled_at_boot=yes\n" in the list of lines
                    if "enabled_at_boot=yes\n" in d_contents:
                        
                        # Finding the index number of the line corresponding to the string
                        line_index = d_contents.index("enabled_at_boot=yes\n")

                        # Modiftying the list item corresponding to the index number
                        d_contents[line_index] = "enabled_at_boot=no\n"

                # Opening the ghostsurf.conf file in write mode
                with open("/opt/ghostsurf/configuration_files/ghostsurf.conf", "w") as e:

                    # Writing the new contents into file
                    e.write("\n".join(d_contents))

                # Changing the start_stop_button's text value to Stop.
                self.start_stop_button.setText("Start")

                # Changing the ultra_ghost_button's text to "disabled"
                self.ultra_ghost_button.setText("disabled")

                # Setting the style sheet of the ultra_ghost_button 
                self.ultra_ghost_button.setStyleSheet(u"#ultra_ghost_button {background: red; border-radius: 4px; border: 1px solid black}")

            # Checking if the didn't pressed to bot yes and not buttons 
            else:

                # Printing "Operation canceled in debug mode"
                debug("Operation canceled")
        
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

            # Adding functionality to Yes and No buttons
            question_dialog.buttonClicked.connect(start_button_question_dialog_processor)

            # Showing the question dialog
            question_dialog.exec_()
            
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

            # Adding functionality to Yes and No buttons
            question_dialog.buttonClicked.connect(stop_button_question_dialog_processor)

            # Showing the question dialog
            question_dialog.exec_() 


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

    # Calling the main function
    main()
