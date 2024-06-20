import os

class shell:
    def __init__(self) -> None:
        self.dir=os.getcwd()
    def input(self):
        """takes the imput from the user"""

        self.cmd=input(">>>$")

    def implement(self):
        """implements all the functions requested by the user"""
        self.welcome()
        while(True):
            self.input()
            if self.cmd==exit:
                self.exit_cmd()
            if self.cmd.startswith("print") or self.cmd.startswith("echo"):
                self.print_cmd()
            if self.cmd=="pwd":
                self.pwd_cmd()
            if self.cmd.startswith("cd"):
                Words=self.cmd.split(" ")[1:]
                new=" ".join(Words)
                self.cd_cmd(new)
            if self.cmd == "clear":
                self.clear()
            if self.cmd=="help":
                self.help()

    def exit_cmd(self):
        """exits the program"""
        exit(code=0)

    def pwd_cmd(self):
        """Displays all files in the current directory"""
        print(self.dir)

    def cd_cmd(self,args):
        """Switches current directory """
        try:
            os.chdir(args)
            self.dir=args
            print(f"moved to: \"{args}\"")
        except OSError as e:
            print(F"ERROR OCCURED:{e}")
    def print_cmd(self):
        """prints the impput givven by the user when print or echo command is used"""
        words=self.cmd.split(" ")[1:]
        output=" ".join(words)
        print(output)

    def welcome(self):
        print("welcome to our terminal:\nuse command \"help\" for help")
    
    def clear(self):
        os.system('cls')

    def help(self):
        print("use \"cd\" {filename} to move to another directory.\nuse \"pwd\" command to see your current directory.\nuse \"print\" {message} or \"echo\" {message} to print your messege on terminal.\nuse \"exit\" command to exit the terminal.\nuse \"clear\" command to clear he terminal")
# if __name__=="__main__":
Shell=shell()
Shell.implement()