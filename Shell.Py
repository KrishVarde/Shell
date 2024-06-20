import os

class shell:
    def __init__(self) -> None:
        self.dir=os.getcwd()
    def input(self):
        """takes the imput from the user"""

        self.cmd=input(">>>$")

    def implement(self):
        """implements all the functions requested by the user"""

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
        except OSError as e:
            print(e)
        print(f"moved to: {args}")
    def print_cmd(self):
        """prints the impput givven by the user when print or echo command is used"""
        words=self.cmd.split(" ")[1:]
        output=" ".join(words)
        print(output)


# if __name__=="__main__":
Shell=shell()
Shell.implement()