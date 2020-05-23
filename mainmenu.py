import sys
import colorama
def mainmenu():
    print("choose:\n \033[1;33;40msingleplayer\n \033[1;30;40mmultiplayer\n \033[1;31;40mexit\33[0m")
    inputd = input("->")
    eval(inputd + "()")

def exit():
    sys.exit()

def multiplayer():
    import multiplayer

def singleplayer():
    print("choose:\n \033[1;32;40measy \n \033[1;31;40mnormal\33[0m")
    inputd = input("-->")
    if(inputd == "easy"):
        import singleplayer
    if(inputd == "normal"):
        import singleplayerH

colorama.init()
mainmenu()
