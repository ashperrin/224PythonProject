# 224PythonProject

## Author(s):

Gabe Veldboom, Thomas Lynaugh, Ashley Perrin


#### Dependencies
selenium --- pip3 install selenium <br/>
mysql connector --- sudo apt-get install python3-mysql.connector <br/>
tkinter --- sudo apt-get install python3-tk <br/>

###Mysql 
mysql needs to be installed and sql script needs to be run to use database features  


#### Example GUI Usage:
python3 gui.py <br/>

#### Command Line Flags
default behavior is 64bit chromedriver headless <br/>
-f --- Run with 32bit firefox (only works on 32bit machines) <br/>
-g --- Run with 64bit chrome but in GUI mode <br/>
-f -h --- Run with 32bit firefox but in headless mode <br/>

#### Example Terminal Usage:
python3 term.py <br/>
./term.py <br/>
./term.py -f <br/>
./term.py -h <br/>
