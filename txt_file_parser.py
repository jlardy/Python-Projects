"""
The use of this script is to parse through text files with non-standard spacing between values and convert it to a csv. 
The script will save the parsed csv with the same file name as the input text file.

If you want to use the first row in the text file as your column titles set use_first to True 

If you want to drop repeated cells set drop_dupes to True.

Set fname as the path to the text file you want to parse without any extension. 
    
    i.e. You want to parse "input.txt", set fname = "input" 

"""

use_first = False
drop_dupes = False
fname = ''    



def get_value(s):
    # Returns the first value from the string and returns the original string without the value
    s = s.lstrip() # remove the spaces to the left
    try:
        return s[:s.index(' ')] , s[s.index(' '):] #return the value until the next whitespace and the string without the current
    except:
        return s.rstrip(), '' #once we're done return and empty string and the last value without newline

def parse_string(s):
    # Returns a list of all the values from a string seperated by spaces
    data = [] 
    while len(s): # while there is still a string parse it
        current, s = get_value(s)
        if current: data.append(current) # the last value is sometimes empty so only save good values
    return data 

output = None # no idea how many columns
with open(fname+'.txt') as txt:
    for i, line in enumerate(txt):
        if line[0] == '#': continue #pass on all the garbage 

        if not output: # if output hasnt been initialized create a dict with number of columns
            output = {i:[val] for i, val in enumerate(parse_string(line))} 
        else:
            for i, val in enumerate(parse_string(line)): #otherwise just add to those columns
                output[i].append(val)


# save as a csv
import pandas as pd 
out = pd.DataFrame(output)

if drop_dupes: out = out.drop_duplicates()

if use_first:
    # drop the repeated rows and set the column titles to the first row
    out.columns = out.iloc[0]
    out = out[1:]


out.to_csv(fname+'.csv')