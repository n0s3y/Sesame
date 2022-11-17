#!/bin/bash

mkdir ~/WorkDir
cd ~/WorkDir

IP=$(zenity --entry --title="google.nl" --text="Input Target")


# create a hashmap of the tasks name -> its command
declare -A tasks=(
  ["Sleep 3 seconds"]="nmap -A ${IP}"
  ["Check network"]="nikto -h ${IP}"
  ["List dir"]="gobuster -e -u ${IP} -w /usr/share/wordlists/dirb/common.txt"
)

# execute each task in the background, redirecting their output to a custom file descriptor
fd=10
for task in "${!tasks[@]}"; do
    script="${tasks[${task}]}"
    eval "exec $fd< <(${script} 2>&1 || (echo $task failed with exit code \${?}! && touch tasks_failed))"
    ((fd+=1))
done

# print the outputs of the tasks and wait for them to finish
fd=10
for task in "${!tasks[@]}"; do
    cat <&$fd
    ((fd+=1))
done

# determine the exit status
#   by checking whether the file "tasks_failed" has been created
if [ -e tasks_failed ]; then
    echo "Task(s) failed!"
    exit 1
else
    echo "All tasks finished without an error!"
    exit 0
fi
