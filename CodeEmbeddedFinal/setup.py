import os

os.system("sudo apt-get update")
os.system("sudo apt-get install python-pip")
os.system("sudo pip install gspread")
os.system("sudo pip install --upgrade oauth2client")
os.system("sudo pip install PyOpenSSL")
os.system("crontab -l | { cat; echo '@reboot bash ~/EL_Projects/ELSpring2018/Final_Project_2/code/getReading.sh'; } | crontab -")
os.system("python sheetReader.py")

