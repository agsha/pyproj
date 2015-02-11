# pyproj
kill bash!
Is it just me or does bash suck?
if you want to remove all *.log files, you need to type
    
    find . -type f -name "*.log" | xargs rm -rf

Yes. Even the double quotes around `*.log` is required.
Crazy! of course you can write a bash script, but who wants to learn that shitty language?
I dont want to spend hours debugging if I should use single quotes? double quotes? backquotes? 
special characters like '?', '*'
Neither do I want to use the ugly `$@` for all comman line args.
I feel like washing my hand after I type it.

The solution? pyproj!
clone it into home folder and add it to your path. 
Use python to create elegant shell scripts with loops and whatnot! 
Instantly use it as a command in your bash.

There are utility classes in the proj which help you execute a process, open pipes, capture output etc.

Down with bash!
