import os, socket
from getpass import getpass

print(os.getcwd())
from scripts._utils import utils
from scripts._utils.ssh import SSH

hostname = socket.gethostname() # can use the local computer
username = 'hackerspace_admin'
default_pw = 'wolf'

def reset_password():
    student_number = utils.input_styled(
        'Enter the student number of the student whose password you want to reset to "{}": '.format(default_pw))

    password = getpass("Enter the admin password: ")
    
    ssh_connection = SSH(hostname, username, password)

    prompt_string = "{}@{}:~$".format(username, hostname)
    command_response_list = [
                                ("sudo passwd {}".format(student_number), "[sudo] password for {}:".format(username), None),
                                (password, "New password: ", None),
                                ("wolf", "Re-enter new password: ", None),
                                ("wolf", prompt_string, "password updated successfully"),
                            ]
    success = ssh_connection.send_interactive_commands(command_response_list)

    if success:
        utils.print_success("Password for {} successfully reset to {}".format(student_number, default_pw))

    ssh_connection.close()