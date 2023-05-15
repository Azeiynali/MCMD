try:
    from subprocess import check_output
    from sqlite3 import connect
    from os import makedirs, rename
    usernameWindow = check_output('echo %username%', shell=True).decode()
    path = f'C:\\Users\\{usernameWindow[:-2]}\\McmdTerm\\'
    try:
        makedirs(path)
    except FileExistsError:
        pass

    con = connect(path + 'Data.db')
    con.close()
    del con
    rename(path + 'Data.db', path + 'Data')
    del makedirs, rename
    con = connect(path + 'Data')
    cur = con.cursor()
    cur.execute('CREATE TABLE Data(Key Text, Value Text)')
    con.commit()
    cur.execute('CREATE TABLE completer(file TEXT, text TEXT)')
    con.commit()
    cur.execute('INSERT INTO Data VALUES("Username", "root")')
    con.commit()
    cur.execute('INSERT INTO Data VALUES("Password", "000")')
    con.commit()
    cur.execute('INSERT INTO Data VALUES("Prompt", "$_")')
    con.commit()

except:
    pass