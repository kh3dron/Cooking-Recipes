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
BAILBUCKET 0.2.0
WINDOWS 10 MASS REGISTRY EDITING TOOL
by KHEDRON
-------------------------
"""


#Works!
def regEdit(location, keyName, changeTo, dataType):

    label = location #just for readability later
    keyVal = location

    try:
        key = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, keyVal)

    SetValueEx(key, keyName, 0, dataType, changeTo)
    #please hire me
    CloseKey(key)

    print location, "set to ", changeTo

def patch(vuln):
    regEdit(vuln[0], vuln[1], vuln[2], vuln[3])

#Keyname = [Location in registry, name of flag, value to change flag to, flag type]

startpage  = [
r'Software\Microsoft\Internet Explorer\Main',
"Start Page",
"https://careers.godaddy.com/",
REG_SZ
]

stickykeys = [
r'Control Panel\Accessibility\StickyKeys',
"Flags",
"506",
REG_SZ
]

uac_on     = [
r'Software\Microsoft\Windows\CurrentVersion\Policies\System',
"EnableLUA",
"1",
REG_SZ
]

all_vulns = [startpage, stickykeys]

for n in all_vulns:
    patch(n)


notes_for_next_patch = """
Currently only works on registry keys that are based in HKEY_CURRENT_USER, and
quick attempts to add that base location as an arg in the regEdit function
haven't worked. Committing this version, which now has a more generalized
reg key editing function, patch(), as shown by the stickykeys quick add.
"""
