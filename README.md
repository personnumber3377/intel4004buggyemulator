# intel4004buggyemulator
This is a VERY buggy intel 4004 cpu emulator.

 It treats all registers peripherals memory etc as variables and i only put 256 bytes of available ram, because i do not even fully understand the memory architecture etc.. THIS IS STILL IN DEVELOPMENT (AND WILL BE FOR QUITE A LONG TIME, BECAUSE I AM LAZY) AND ALSO I AM VERY ANTISOCIAL SO DO NOT TAKE IT PERSONALLY IF I DO NOT ALLOW YOU TO MAKE COMMITS. (my first github repo. yeay!) Feel free to test it and report bugs. (WARNING: The code is not readable at all.)
 
 
 How to run it:
 
 just put your program in hex to the program.bin file and then run python3 simulator.py and it will run the code in the program file. (remember to put only one byte per
 line in the program file and remember to add a newline at the end of it the file. otherwise the emulator will not work properly. and also there is an example program
 already inside the file which stores three to the accumulator and increments in and then completes. the emulator stops when rip is 0xFF, so do not put any code there.)
 
 so yeah. quite the piece of spagetti code if i have ever seen one.
 
 have fun!
