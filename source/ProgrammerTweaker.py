import os, os.path, urllib.request
def ru_settings(usernameHome):
    print("Привет! Сейчас мы будем делать вашу рабочую область более удобной!")
    print("Я создам директорию во временной папке ~/PT (линукс) или на диске, котором вы укажете (на Windows)")
    platform = os.uname()
    if platform[0] == "Linux":
        os.chdir(usernameHome)
        try:
            os.mkdir("PT")
        except Exception:
            os.rmdir("PT")
            os.mkdir("PT")
        os.chdir(os.getcwd()+"/PT")
        print("Что вы хотите установить?")
        print("""
1. VSCode (установка возможна только с использованием менеджера пакетов Snap)
2. Vim
3. NeoVim
4. Atom (аналогично, только со Snap)
5. Emacs
0. Ничего не устанавливать
        """)
        editor = ""
        while True:
            editor = input("Введите цифру:")
            if editor in {"1","2","3","4","5","0"}:
                break

        packagemanager = ""
        while True:
            print("Ваш пакетный менеджер: [A]pt, [P]acman, [D]nf:", end="")
            packagemanager = input()
            if packagemanager.lower() in {"a","p","d"}:
                break
        if packagemanager.lower() == "a":
            packagemanager = "sudo apt install "
        elif packagemanager.lower() == "p":
            packagemanager = "sudo pacman -Sy "
        else:
            packagemanager = "sudo dnf install "
        
        if editor != "0":
            if editor == "2":
                os.system(packagemanager + "vim")
                print("Скачать конфигурационные файлы к Vim?")
                inp = input("y/n").lower()
                if inp == y:
                    os.system("curl -fLo ~/.vimrc https://raw.githubusercontent.com/username77177/FastProgrammingEnvironment/master/.vimrc")
            elif editor == "3":
                os.system(packagemanager + "neovim")
            elif editor == "5":
                os.system(packagemanager + "emacs")
            elif editor == "1":
                os.system("sudo snap install code --classic")
            elif editor == "4":
                os.system("sudo snap install atom --classic")
            else:
                os.system(packagemanager + "emacs")
    elif platform[0] == "Windows":
        pass
hello = '''
\t ____                                                                       _____                         _
\t|  _ \  _ __   ___    __ _  _ __   __ _  _ __ ___   _ __ ___    ___  _ __  |_   _|__      __  ___   __ _ | | __  ___  _ __
\t| |_) || '__| / _ \  / _` || '__| / _` || '_ ` _ \ | '_ ` _ \  / _ \| '__|   | |  \ \ /\ / / / _ \ / _` || |/ / / _ \| '__|
\t|  __/ | |   | (_) || (_| || |   | (_| || | | | | || | | | | ||  __/| |      | |   \ V  V / |  __/| (_| ||   < |  __/| |
\t|_|    |_|    \___/  \__, ||_|    \__,_||_| |_| |_||_| |_| |_| \___||_|      |_|    \_/\_/   \___| \__,_||_|\_\ \___||_|
\t                     |___/

'''
print(hello)
print("Выберите язык (Choose your language) [RU,EN]:", end = "")
inp = input()
if inp.lower() == "ru":
    pwd = os.getcwd()
    userHome = os.path.expanduser("~")
    ru_settings(userHome)
else:
    en_settings()
