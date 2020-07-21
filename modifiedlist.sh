Help()
{
   # Display Help
   echo     "   ---------------------------------------------------------------------------------------------    "
   echo     "   |                                                                                           |"
   echo     "   |    This script helps you search recently modified files in a given time and directory     |"    
   echo     "   |                                                                                           |"
   echo -e  "   |    \e[0;32mSyntax\e[0m :  ./modifiedlist.sh [ Directory ] [ Days ]                                     |"
   echo     "   |                                                                                           |"
   echo -e  "   |    \e[0;32mExample\e[0m : ./modifiedlist.sh /home 10                                                   |"
   echo     "   |                                                                                           |"
   echo -e "   |    \e[0;32mWritten By\e[0m : Awais Khan                                                                |"
   echo     "   |                                                                                           |"
   echo     "   ---------------------------------------------------------------------------------------------"
   echo
}

if [ $# -lt 2 ];then

Help

else

# find $1 -type f -mtime -$2 -ls | while read -r line ; do
find $1 -type f -mtime -$2 -exec ls -la {} \;


# info=$(echo $line | cut -d " " -f 3,8,9,10,11)

# echo $info
# done

fi


