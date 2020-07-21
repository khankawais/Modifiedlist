import subprocess
import shlex
import sys

def Help():
   print("   ---------------------------------------------------------------------------------------------")
   print("   |                                                                                           |")
   print("   |    This script helps you search recently modified files in a given time and directory     |")   
   print("   |                                                                                           |")
   print("   |    Syntax :  python3 modifiedlist.py [ Directory ] [ Days ]                               |")
   print("   |                                                                                           |")
   print("   |    Example : python3 modifiedlist.py /home 10                                             |")
   print("   |                                                                                           |")
   print("   |    Written By : Awais Khan                                                                |")
   print("   |                                                                                           |")
   print("   ---------------------------------------------------------------------------------------------")
   print


if len(sys.argv) < 3:
    Help()

else:
    p=sys.argv[1]
    d=sys.argv[2]
    cmd=f"find {p} -type f -mtime -{d} -ls"
    output = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).communicate()
    output = output[0].decode("utf-8")



    for line in output.splitlines():
        line=shlex.split(line)
        print(line[2]+ " "+line[7]+ " "+line[8]+ " "+line[9]+ " "+line[10])


