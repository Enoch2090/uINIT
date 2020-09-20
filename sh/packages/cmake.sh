#----INSTALL CMAKE----
echo 'Checking Cmake...'
cmk_exists=`which cmake`
if [ ${#cmk_exists} -eq 0 ]
then
    sudo snap install cmake --classic -y
else
    echo 'Cmake already installed.'
fi
#----END INSTALLATION----
