import gtk,glib
import subprocess
 
class CommandTextView(gtk.TextView):
    ''' NICE TEXTVIEW THAT READS THE OUTPUT OF A COMMAND SYNCRONOUSLY '''
    def __init__(self):
        print("printing SOMETHING")
        '''COMMAND : THE SHELL COMMAND TO SPAWN'''
        super(CommandTextView, self).__init__()
        self.command = "sample.py"
    def run(self):
        ''' RUNS THE PROCESS '''
        proc = subprocess.Popen(self.command, stdout = subprocess.PIPE) # SPAWNING
        glib.io_add_watch(proc.stdout, # FILE DESCRIPTOR
                          glib.IO_IN,  # CONDITION
                          self.write_to_buffer ) # CALLBACK
    def write_to_buffer(self, fd, condition):
        if condition == glib.IO_IN: #IF THERE'S SOMETHING INTERESTING TO READ
           char = fd.read(1) # WE READ ONE BYTE PER TIME, TO AVOID BLOCKING
           buf = self.get_buffer()
           buf.insert_at_cursor(char) # WHEN RUNNING DON'T TOUCH THE TEXTVIEW!!
           return True # FUNDAMENTAL, OTHERWISE THE CALLBACK ISN'T RECALLED
        else:
           return False # RAISED AN ERROR: EXIT AND I DON'T WANT TO SEE YOU ANYMORE

a = CommandTextView()