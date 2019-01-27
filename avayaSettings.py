#!/usr/bin/python -tt
"""
For Avaya H.323 and SIP Phones
This program creates a 46xxsettings.new file. Here's how it works.

Files required in this directory:
46xxsettings.txt <-- This is the latest available settings file from support.avaya.com
46xxsettings.old <-- This is your current 46xxsettings file from which you'll want to copy the SET lines.
                     Make sure you name this 46xxsettins.old (or change the variable below)

Output File:
46xxsettings.new <-- This file will be created by this program merging the uncommented SET lines from
                     the .old file with the downloaded (hopefully latest) 46xxsettings.txt file.

I just learned Python and this is my first attempt at writing a useful proigram. I need to add
lots of error checking, and re-examine my use of a dictionary to accomplish this task.
"""

__author__ = "Chuck Paquette"
__version__ = "0.1.0"

import sys
import re

avaya_settings_file = '46xxsettings.txt'
new_settings_file = '46xxsettings.new'
old_settings_file = '46xxsettings.old'

def print_line():
    print ('-') * 50
    return()

# Find uncommented lines in 46xxsettings.old
def find_uncomment(read_file):
  set_dict = {} #Create a dictionary of keywords and variables
  line_count = 0
  keyword_count = 0
  print('Opening ' + read_file)
  input_file = open(read_file, 'r')
  for each_line in input_file:
      test = re.search(r'^#\s', each_line) # Need to end the search here
      match = re.search(r'^SET\s', each_line) #Search for SET ...
      if test:
          print('Found single # line at ' + str(line_count)) 
          print('Found ' + str(keyword_count) + ' SET lines')
          input_file.close()
          print('Closed ' + read_file)
          print_line()
          return(set_dict)
      elif match:
          set_split = each_line.split()
          # print (set_split[1] + " ===> " + set_split[2])
          set_dict[set_split[1]] = set_split[2]
          keyword_count += 1
      else:
          line_count += 1
  print ('No single # found')
  return(set_dict)

def main():
    """ Main entry point of the app """
    end_replace = False
    print ('Please double check the 46xxsettins.new file for duplicates and errors')
    print ('Merging of the ' + old_settings_file + ' and the ' + avaya_settings_file)
    print ('will stop at the first occurrence of single hash (# ) which is where the IF statements')
    print ('are usually located. You\'ll have to move those settings manually' )
    raw_input('Press Enter to Continue')
    print_line()
    #--------------------------------------------
    settings = find_uncomment(old_settings_file)
    for key in settings:
        print (key + ' <==== ' + settings[key])
    print_line()
    #--------------------------------------------
    input_setfile = open(avaya_settings_file, 'r')
    output_setfile = open(new_settings_file, 'w+')
    for input_line in input_setfile: #Outer loop to check each line in the setting file
        test_for_end = re.search(r'^#\s', input_line)
        if test_for_end:
            end_replace = True
        # print (input_line),
        output_setfile.write(input_line)
        for key in settings: #Inner loop to check if the key should be set
            key_match = re.search(r'^## SET ' + key + r'\s',input_line) and (not end_replace)
            if key_match:
                # print ('SET ' + key + ' ' + settings[key])
                output_setfile.write('SET ' + key + ' ' + settings[key] + '\r\n')
                # print ('##')
                output_setfile.write('##')

    # Clean up the files
    input_setfile.close()
    output_setfile.close()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()