# Creating a variable called username which is equal to the logged in user's username
username=${SUDO_USER:-${USER}}

echo $username
