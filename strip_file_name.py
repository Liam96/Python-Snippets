# ================================ #
__author__ = "Liam Robinson"
__credits__ = ["Liam Robinson"]
__version__ = "1.0.3"
__maintainer__ = "Liam Robinson"
__email__ = "liamcsiro@gmail.com"
# ================================ #

# ================================ #
#             IMPORTS              #
# ================================ #
from tkinter import *
from tkinter.filedialog import askopenfilename
import sys

# = Use Tkinter to Select the File - CSV is Default so shouldn't have to deal with checking file formats
root = Tk()
root.filename = askopenfilename(initialdir="C:",
                                title="Choose your CSV",
                                filetypes=(("CSV Files", "*.csv"), ("All Files", "*"))
                                )

# = Remove Tk Window
root.withdraw()

# = Try Open Files - File Dialog to Select and the Write File is Made Automatically (Shouldn't get IO Error)
try:
    f = open(root.filename)
    with open("file_names.csv", 'wt', newline="") as w:

        # = Format Required for Code To Work = parameters_[Characters Required].csv - CSV also has no header
        for row in f:
          
            # = Replaces the First Part of the File Name (Still has an underscore to remove at start)
            # == Note: Underscore Could Also be Removed Here - But Inconsistent File Names in Dataset
            name = row.replace("parameters", "")

            # = Get Rid of First Character (I.E. the underscore)
            name = name[1:]

            # = Get Rid of the .csv extension
            name = name[:-5]

            # = Write Names to File (will write in project directory)
            w.write(name.lower())
            w.write('\n')
            
            # = Close the Application
            sys.exit()

    # = Call the Tk Window
    root.mainloop()

except PermissionError:
    print("Permission Denied - Couldn't Open File")
    print("Snippet Closing")
    sys.exit()
