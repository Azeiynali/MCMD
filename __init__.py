from os import system, makedirs, path, rmdir, remove, startfile, environ
from subprocess import check_output
from shutil import copy
from zipfile import ZipFile
from hashlib import md5
from sqlite3 import connect
from urllib.request import urlretrieve
from colorama import init, Fore
from sys import exit
from prompt_toolkit import prompt as Pr
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import webbrowser
import keyword
import builtins

init()

environ['RUNAS'] = 'admin'

try:
    remove('setup.py')
except:
    pass
usernameWindow = check_output('echo %username%', shell=True).decode()[:-2]
if not path.exists(f'C:\\Users\\{usernameWindow}\\McmdTerm\\Data'):
    print(Fore.RED + 'Please run the setup.py file \nFor more information, read README in ' + Fore.BLUE + 'https://github.com/Tarrahchi/mcmd/blob/main/README.md' + Fore.RESET)
    while True:
        pass
con = connect(f'C:\\Users\\{usernameWindow}\\McmdTerm\\Data')
ISE = True
con = connect(f'C:\\Users\\{usernameWindow}\\McmdTerm\\Data')
cur = con.cursor()

global prompt
cur.execute('SELECT Value FROM Data WHERE Key = "Prompt"')
prompt = cur.fetchone()[0]
global username
cur.execute('SELECT Value FROM Data WHERE Key = "Username"')
username = cur.fetchone()[0]
global password
cur.execute('SELECT Value FROM Data WHERE Key = "Password"')
password = cur.fetchone()[0]
Wuser = check_output('echo %username%', shell=True).decode()[:-2]
global Path
Path = f'C:\\Users\\{usernameWindow}\\'
# * توابع آماده

def start(x = None):
    # ! آماده سازی ------------------------------------------------------------
    system('Title Mcmd')
    system('color E')
    system('cls')
    print('...:::Mcmd(c):::... [Version 1.1.0.0]\n      this is Modified Command Line\n')
def UpData():
    global prompt
    cur.execute('SELECT Value FROM Data WHERE Key = "Prompt"')
    prompt = cur.fetchone()[0]
    global username
    cur.execute('SELECT Value FROM Data WHERE Key = "Username"')
    username = cur.fetchone()[0]
    global password
    cur.execute('SELECT Value FROM Data WHERE Key = "Password"')
    p = cur.fetchone()[0]
    try:
        if eval(p) != None:
            password = p
        else:
            password = None
    except:
        password = p
    del p
def DIR(path_):
    if str(path_[:2].lower()) == 'c:' or str(path_[:2].lower()) == 'd:' or str(path_[:2].lower()) == 'e:'  and path.isdir(path_):
        return path_
    elif path.isdir(Path + path_):
        return Path + path_
    else:
        raise TypeError('path')
def FILE(path_):
    if path.isfile(path_):
        return path_
    elif path.isfile(Path + path_):
        return Path + path_
    else:
        raise TypeError('path')
def D7F(path_):
    if (str(path_[:2].lower()) == 'c:' or str(path_[:2].lower()) == 'd:' or str(path_[:2].lower()) == 'e:') and (path.isfile(path_) or path.isdir(path_)):
        return path_
    elif path.isdir(Path + path_) or path.isfile(Path + path_):
        return Path + path_
    else:
        raise TypeError('path')

# * پکیج دانلودر ها

def pythonPDow():
    print('Start Downloading')
    print('...')
    class_names = [name for name, obj in vars(builtins).items() if isinstance(obj, type)]
    all_keywords = keyword.kwlist + class_names
    for i in all_keywords:
        cur.execute(f'INSERT INTO completer VALUES(".py", "{i}")')
        con.commit()

# * دستورات ------------------------------------------------------------

def cls(x):
    try:
        if ''.join(x.split(' ')[1]) == '--help' or ''.join(x.split(' ')[1]) == '/?':
            print(''' SYNTAX: clear
    {for clear screen}''')
            return ''
    except:
        system('cls')
def pwd(x):
    try:
        if x.split(' ')[1] == '--help' or x.split(' ')[1] == '/?':
            print(''' SYNTAX: pwd
    {show path}''')
            return ''
    except:
        print(Path[:-1])
def cd(x, y):
    Path = y
    try:
        if path.isfile(x.split(' ')[1]):
            print('please enter a path')
            return y
        if ''.join(x.split(' ')[1]).lower() == '--help' or ''.join(x.split(' ')[1]).lower() == '/?':
            print(''' SYNTAX: cd [path]''')
        if path.isdir(y + ''.join(x.split(' ')[1])) or x.split(' ')[1][:2].lower() == 'c:' or x.split(' ')[1][:2].lower() == 'd:' or x.split(' ')[1][:2].lower() == 'e:':
            if x.split(' ')[1][:2].lower() == 'c:' or x.split(' ')[1][:2].lower() == 'd:' or x.split(' ')[1][:2].lower() == 'e:':
                    Path = x.split(' ')[1] + '\\'
                    return Path
            if x.split(' ')[1]:
                    Path += x.split(' ')[1] + '\\'
                    return Path
            else:
                return Path
        else:
            if ''.join(x.split(' ')[1]) == '..':
                return '\\'.join(Path.split('\\')[:-1]) + '\\'
            else:
                global ISE
                ISE = True
                print('mcmd: Path not found')
                return y
    except:
        print('please enter a path')
        return y
def echo(x:str):
    try:
        if ''.join(x.split(' ')[1]) == '--help' or ''.join(x.split(' ')[1]) == '/?':
            print(''' SYNTAX: echo [TEXT]
    {show text in screen}''')
            return ''
        else:
            if x.split(' ')[1] == '%username%':
                print(username)
            else:
                print(''.join(x.split(' ')[1]))
    except:
        print('')
def create(x):
    try:
        if ''.join(x.split(' ')[1]) == '--help' or ''.join(x.split(' ')[1]) == '/?':
            print('''SYNTAX: create [type] [file name]
        type{ -FL: create a file, -FO: create a folder}
        -O: Open the file for editing immediately after creating it.
        example:
            create -FL 1.txt -O''')
        if ''.join(x.split(' ')[1]) == '-FL':
            try:
                open(Path + ''.join(x.split(' ')[2]), 'a').close()
            except:
                open(Path[:-2] + '\\' + ''.join(x.split(' ')[2]), 'w').close()
        elif ''.join(x.split(' ')[1]) == '-FO':
            folder_path = Path + ''.join(x.split(' ')[2])
            if not path.exists(folder_path):
                makedirs(folder_path)
            else:
                print(f'The {folder_path} directory already exists.')
        if '-O' in x.split(' '):
            if ''.join(x.split(' ')[1]) != '-FO':
                system(Path[:-3] + '\\' + ''.join(x.split(' ')[2]))
            else:
                print('The folder does not open')
    except IndexError:
        print('create: Pleas Enter a type and file name')
def ddir(x):
    try:
        if ''.join(x.split(' ')[1]) == '--help' or ''.join(x.split(' ')[1]) == '/?':
            print(''' SYNTAX: ddir [FOLDER]
    {delet a folder}''')
            return ''
        else:
            if path.exists(Path[:-1] + '\\' + ''.join(x.split(' ')[1])):
                rmdir(Path + ''.join(x.split(' ')[1]))
            else:
                print(f'mcmd: folder not found')
    except:
        print('Pleas Enter a Folder Name')
def dfile(x):
    try:
        if ''.join(x.split(' ')[1]) == '--help' or ''.join(x.split(' ')[1]) == '/?':
            print(''' SYNTAX: dfile [FILE]
    {delet a file}''')
            return ''
        else:
            try:
                remove(FILE(x.split(' ')[1]))
            except:
                    print(f'mcmd: file not found')
    except:
        print('Pleas Enter a file Name')
def fle(x):
    if x.split(' ')[1][0] == '/':
        if x.split(' ')[1] == '/history':
            cur.execute('SELECT Value FROM Data WHERE Key = "HForFLE"')
            for i in cur.fetchall():
                if i[0]:
                    print(i[0])
        elif x.split(' ')[1] == '/clear':
            cur.execute(f"UPDATE Data SET value = '' WHERE key = 'HForFLE'")
            con.commit()
        elif x.split(' ')[1] == '/download':
            if x.split(' ')[2] in packages:
                pathh = f'C:\\Users\\{usernameWindow}\\McmdTerm\\packages'
                packages[x.split(' ')[2]]()
            else:
                print('please enter a valid package')
        return ''
    else:
        try:
            FILE(x.split(' ')[1])
            f = open(x.split(' ')[1], 'a', encoding='utf-8')
            file = open(x.split(' ')[1], 'r', encoding='utf-8').read()
        except:
            print('mcmd: file not found')
            return ''
        print(file)
        cur.execute(f'INSERT INTO Data VALUES("HForFLE", "{x.split(" ")[1]}")')
        con.commit()
        cur.execute(f'SELECT text FROM completer WHERE file = "{path.splitext(x.split(" ")[1])[1]}"')
        options = set()
        for i in cur.fetchall():
            options.add(i[0])
        completer = WordCompleter(options)
        while True:
            system('color E')
            inp = Pr('', completer=completer)
            if inp == '<save>':
                break
            if inp == '<quit>':
                f.close()
                open(x.split(' ')[1], 'w').write(file)
                break
            f.write(inp + '\n')
def ls(x):
    try:
        if x.split(' ')[1] == '/?' or x.split(' ')[1] == '--help':
            print(''' SYNTAX: ls
        {ahow all files and folders}
        /all --> show details''')
            return ''
    except:
        pass
    try:
        if x.split(' ')[1] == '/all':
            print(check_output('dir ' + Path[0:-1] + ' /all', shell=True).decode())
        else:
            print(check_output('dir ' + Path[0:-1], shell=True).decode())
    except:
        print(check_output('dir ' + Path[0:-1], shell=True).decode())
def dup(x):
    try:
        if x.split(' ')[1] == '/?' or x.split(' ')[1] == '--help':
            print(''' SYNTAX: dup [file name] [file name]
        {cope file}''')
            return ''
        if x.split(' ')[1][:3].lower() == 'c:\\' or x.split(' ')[1][:3].lower() == 'd:\\' or x.split(' ')[1][:3].lower() == 'e:\\':
            copy(Path + x.split(' ')[1], Path + x.split(' ')[2])
        else:
            copy(x.split(' ')[1], x.split(' ')[2])
    except:
        print('mcmd: syntax eror, please enter a dup --help')
def unzip(x):
    with ZipFile(Path + x.split(' ')[1], 'r') as zip_ref:
        zip_ref.extractall(Path)
def Cprompt(x):
    newprompt = x.split(' ')[1]
    cur.execute(f"UPDATE Data SET value = {newprompt} WHERE key = 'Prompt'")
    con.commit()
    UpData()
def User(x):
    i = password
    def changeP():
        if input('mcmd: your old password: ') == i:
            newpassword = input('mcmd: your new password: ')
            cur.execute(f"UPDATE Data SET value = '{newpassword}' WHERE key = 'Password'")
            con.commit()
            UpData()
            return ''
        else:
            print('password manager: please try again')
    def changeU():
        if input('mcmd: your password: ') == i:
            global username
            newusername = input('mcmd: your new username: ')
            cur.execute(f"UPDATE Data SET value = '{newusername}' WHERE key = 'Username'")
            con.commit()
            UpData()
            return ''
        else:
            print('password manager: please try again')
    def changeDP():
        cur.execute(f"UPDATE Data SET value = '{x.split(' ')[1]}' WHERE key = 'dpath'")
        con.commit()
        UpData()
    Uscript  = {
        'change password': changeP,
        'change username': changeU,
        'change default path': changeDP,
    }
    try:
        Uscript[' '.join(x.split(' ')[1:])]()
    except:
        print('mcmd: User SYNTAX Error')
def md5en(x):
    try:
        if '-F' in x:
            T = open(x.split(' ')[2]).read()
            print(md5(T.encode()).hexdigest())
            return ''
        else:
            T = x.split(' ')[1]
            print(md5(T.encode()).hexdigest())
    except:
        print('pleas Enter a text, File')
def helpp(x):
    webbrowser.open('https://github.com/Tarrahchi/mcmd/blob/main/README.md')
def move(x):
    try:
        pathfile = D7F(x.split(' ')[1])
    except:
        print('file: please enter a valid file/directory')
    try:
        pathMove = DIR(x.split(' ')[2])
    except:
        print('path: please enter a valid directory')
    system(f'move {pathfile} {pathMove}')
def download(x):
    if DIR(x.split(' ')[2]):
        url = x.split(' ')[1]
        destination = x.split(' ')[2] + path.basename(url)
        urlretrieve(url, destination)
    elif FILE(x.split(' ')[2]):
        url = x.split(' ')[1]
        destination = x.split(' ')[2]
        urlretrieve(url, destination)
def show(x):
    try:
        showfile = FILE(x.split(' ')[1])
    except:
        print('please Enter a valid file')
        return ''
    print(open(showfile, encoding='UTF-8').read())

# * دیکشنری دستورات -----------------------------------------------------

Scripts = {
    'pwd': pwd,
    'clear': cls,
    'cd': cd,
    'echo': echo,
    'mcmd': start,
    'create': create,
    'ddir': ddir,
    'dfile': dfile,
    'fle':fle,
    'ls': ls,
    'dup': dup, 
    'unzip': unzip,
    'prompt': Cprompt,
    'User': User,
    'md5en': md5en,
    'py': lambda x: system(x),
    'pip': lambda x: system(x),
    'help': helpp,
    'move': move,
    'tar': lambda x: system(x),
    'download': download,
    'ifconfig': lambda x: system('ipconfig'),
    'show': show,
    'exit': exit
}

# * پکیج ها

packages = {
    "python": pythonPDow
}

# * اجرا -----------------------------------------------------

start()

while True:
    system('color E')
    init()
    try:
        Command = input(username + '@' + Path[:-1] + '\n' + prompt)
        c = ''.join(Command.split(' ')[0])
        if Command:
            if c == 'cd':
                ISE = False
                Path = cd(Command, Path)
                continue
            if c in list(Scripts.keys()):
                # try:
                Scripts[c](Command)
                # except:
                    # if c != 'exit':
                        # print(f'mcmd: The syntax of the {c} is incorrect.')
                    # else:
                        # Scripts[c](Command)
            else:
                print(f'mcmd: {c}: command not found\n')
    except KeyboardInterrupt:
        print('\n')
        continue