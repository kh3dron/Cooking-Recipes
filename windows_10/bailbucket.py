from _winreg import *

print """
_______  _______  ___   ___        _______  __   __  _______  ___   _  _______  _______
|  _    ||   _   ||   | |   |      |  _    ||  | |  ||       ||   | | ||       ||       |
| |_|   ||  |_|  ||   | |   |      | |_|   ||  | |  ||       ||   |_| ||    ___||_     _|
|       ||       ||   | |   |      |       ||  |_|  ||       ||      _||   |___   |   |
|  _   | |       ||   | |   |___   |  _   | |       ||      _||     |_ |    ___|  |   |
| |_|   ||   _   ||   | |       |  | |_|   ||       ||     |_ |    _  ||   |___   |   |
|_______||__| |__||___| |_______|  |_______||_______||_______||___| |_||_______|  |___|

-------------------------
BAILBUCKET 0.1.0
WINDOWS 10 MASS REGISTRY EDITING TOOL
by KHEDRON
-------------------------
"""

def brief (name, value):
    print name, "set to ", value


keyVal = r'Software\Microsoft\Internet Explorer\Main'
#Some reg keys have bad defaults, but some don't exist- change, or create
try:
    key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
except:
    key = CreateKey(HKEY_CURRENT_USER, keyVal)

SetValueEx(key, "Start Page", 0, REG_SZ, "https://careers.godaddy.com/")
#please hire me
CloseKey(key)
brief(keyVal, key)
