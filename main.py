from functions import *
from tkinter import *
from functools import partial   # To prevent unwanted windows
import re

import random

file = open("formatted_scores.txt", "r")
read_file()
remove_team_duplicates()

class results_lookup:
    def __init__(self): 
       
      #self.run = True
      # Formatting variables
      

      # Initialise list to hold results of user search
      self.all_results_list = []

      self.menubar = tk.Menu()
      self.nav = tk.Menu()
      self.menubar.add_cascade(label="File", menu=self.nav)
      

      self.nav.add_command(label="Help", command=self.help)
      self.nav.add_separator()
      self.nav.add_command(label="Exit", command= root.destroy)

      root.configure(menu=self.menubar)

      


      

      # Frame
      background_color = "light blue"
      self.lookup_frame = Frame(bg=background_color, pady=10)

      self.lookup_frame.grid()

      # Heading (row 0)
      self.sports_heading_label = Label(self.lookup_frame,
                                      text="NBA Game Finder",
                                      font="Arial 19 bold", bg=background_color,
                                      padx=10, pady=10, justify= CENTER)
      self.sports_heading_label.grid(row=0)

      # User instructions (row 1)
      self.sports_instructions_label = Label(self.lookup_frame,
                                            text="Select two teams and click submit to view the game stats for games between your selected teams during 2016-17 NBA season.",
                                            font="Arial 10 italic", wrap=290,
                                            justify=CENTER, bg=background_color,
                                            padx=10 , pady=10)
      self.sports_instructions_label.grid(row=1)





    # Combobox creation\
    
      n = tk.StringVar()
      self.team1_selected = ttk.Combobox(self.lookup_frame, width = 5, textvariable = n, state="readonly")

    # Adding combobox drop down list
      self.team1_selected['values'] = duplicate_function(TEAM_ABBREVIATION)

      self.team1_selected.grid(column = 0, row = 4, padx = 5, pady= 20)
      self.team1_selected.current()
      
    # Team input (row 5)
      self.team_input_label = Label(self.lookup_frame,
                                            text="VS",
                                            font="Arial 10 italic",
                                            justify= CENTER, bg=background_color,
                                            padx=10, pady=10)
      self.team_input_label.grid(row=4, column = 1)

    # Combobox creation
      n = tk.StringVar()
      self.team2_selected = ttk.Combobox(self.lookup_frame, width = 5, textvariable = n, state="readonly")

      # Adding combobox drop down list
      self.team2_selected['values'] = duplicate_function(TEAM_ABBREVIATION)
      self.team2_selected.grid(column = 2, row = 4, padx = 5, pady= 20)
      self.team2_selected.current()



    # Submit button
      self.submit_btn = Button(self.lookup_frame, font="Arial 12 bold",
                                            text="Submit", width=5, command=justamethod)
      self.submit_btn.grid(row=8, column=1)

#end class results lookup



























    def help(self):
      if self.run:
          get_help = Help(self)
          get_help.help_text.configure(text="Please select your teams "
                                            "and then push the submit button. \n\n"
                                            "The tabs allow you to swich between games "
                                            "making it easy to find and view the results you're looking for.  \n\n"
                                            "You can "
                                            "also export the results of "
                                            "your search to a text file if desired.")
          self.run = False

          


class Help:
    def __init__(self, partner):

        background = "orange"
        # disable help button
        partner.nav.entryconfig("Help", state="disabled")

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))


        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                             command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.nav.entryconfig("Help", state="normal")
        self.help_box.destroy()
        something.run = True

def justamethod (self): 
    print("method is called")
    print (self.team1_selected.get())
    print (self.team2_selected.get())

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("NBA Game Finder")
    something = results_lookup()
    root.mainloop()

