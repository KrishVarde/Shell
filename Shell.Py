import os

class shell:
    def __init__(self) -> None:
        s=shell
        dir_=os.getcwd()
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
                self.pwd_cmd



    def exit_cmd(self):
        """exits the program"""
        exit(code=0)


    def pwd_cmd(self):

        """Displays all files in the current directory"""
        

    def cd_cmd(self):
        """Switches current directory """
        

    def print_cmd(self):
        """prints the impput givven by the user when print or echo command is used"""
        words=self.cmd.split(" ")[1:]
        output="".join(words)
        print(output)