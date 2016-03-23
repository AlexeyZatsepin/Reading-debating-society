#!/bin/bash

comfirm() {
	echo -n "Rewrite old archive?(y/n)"
	read a
	if [ "$a" == "y" ]
	then
		chmod 644 $archive_name.tar.gz
		rm $archive_name.tar.gz
		return 0
	else 
		return 1
	fi
}

user=`whoami`
echo $user

echo "Write title of your folder from ~"
read b
mydir=$HOME/
echo $mydir

archive_name=back_up_$user
echo $archive_name

cd $mydir
cd $b

if (([ ! -f $archive_name.tar.gz ]) || ( comfirm ))
then	
	tar -czvf ~/$archive_name.tar.gz *&> /dev/null
	terminal-notifier -message  "backup complete" -title "result"
else 
	terminal-notifier -message  "backup canceled" -title "result"
fi	

chmod 444 $archive_name.tar.gz 
tar -C ./ -xzvf $archive_name.tar.gz
terminal-notifier -message "Success" -title "laba6OSa"
#osascript -e 'tell Application "Finder" to display dialog "Job finished"' 
