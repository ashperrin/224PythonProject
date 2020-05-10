# 224PythonProject

## Author(s):

Gabe Veldboom, Thomas Lynaugh, Ashley Perrin


#### Dependencies
selenium  <br/>
mysql-connector-python <br/>
tkinter <br/>
PIL <br/>

Note: These should be already included in the code directory but if you cannot get it to run you <br/>
may have to pip install these. If you run into any problems please email one of us <br/>

### Mysql 
mysql needs to be installed and sql script needs to be run to use database features  <br/>
otherwise it does not use them. If mysql is not installed flag is false by default so it does not crash <br/>

#### Example Usage:
python3 gui.py <br/>
python3 term.py <br/>

#### Command Line Flags
default behavior is 64bit chromedriver headless <br/>
-f --- Run with 32bit firefox (only works on 32bit machines) <br/>
-g --- Run with 64bit chrome but in Chrome GUI mode <br/>
-f -h --- Run with 32bit firefox but in headless mode <br/>

#### Example Terminal Usage:
python3 term.py <br/>
./term.py <br/>
./term.py -f <br/>
./term.py -g <br/>
