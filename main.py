from functions import *
from tkinter import *
from functools import partial   # To prevent unwanted windows
import re

import random

file = open("formatted_scores.txt", "r")
read_file()
class results_lookup:
    def __init__(self): 
      
      #p1 = PhotoImage(file = 'nbalogo.jpg')
      #self.run = True
      # Formatting variables
      p1 = PhotoImage(file = 'nbalogo.png')
 
# Setting icon of master window
      root.iconphoto(False, p1)

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
      self.team1_selected['values'] = duplicate_function(sorted(TEAM_ABBREVIATION))

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
      self.team2_selected['values'] = duplicate_function(sorted(TEAM_ABBREVIATION))
      self.team2_selected.grid(column = 2, row = 4, padx = 5, pady= 20)
      self.team2_selected.current()



    # Submit button
      self.submit_btn = Button(self.lookup_frame, font="Arial 12 bold",
                                            text="Submit", width=5, command=self.results)
      self.submit_btn.grid(row=8, column=1)

#   # results / Help button frame (row 5)
#       self.hist_help_frame = Fram(self.converter_frame)
#       self.hist_help_frame.grid(row=5, pady=10)

#       self.submit_btn = Button(self.hist_help_frame, font="Arial 12 bold",
#                                      text="Calculation results", width=15,
#                                      command=lambda: self.results(self.all_calc_list))
#       self.submit_btn.grid(row=0, column=0)

#end class results lookup

    def help(self):
      #if self.run:
          get_help = Help(self)
          get_help.help_text.configure(text="Please select your teams "
                                            "and then push the submit button. \n\n"
                                            "The tabs allow you to swich between games "
                                            "making it easy to find and view the results you're looking for.  \n\n"
                                            "You can "
                                            "also export the results of "
                                            "your search to a text file if desired.")
          #self.run = False
    def results(self):
      #if self.run:
        get_results = results(self)
          


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
#end class help



class results:
    def __init__(self, partner):

        background = "#a9ef99"     # Pale green

        # disable results button
        partner.submit_btn.config(state=DISABLED)

        # Sets up child window (ie: results box)
        self.results_box = Toplevel()

        # If users press cross at top, closes results and 'releases' results button
        self.results_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_results, partner))

        # Set up GUI Frame
        self.results_frame = Frame(self.results_box, width=300, bg=background)
        self.results_frame.grid()

        # Set up results heading (row 0)
        self.how_heading = Label(self.results_frame, text="results",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # results text (label, row 1)
        self.results_text = Label(self.results_frame,
                                  text="Here are your results. Please use the "
                                       "export button to create a text "
                                       "file of all your calculations for "
                                       "this session", wrap=250,
                                  font="arial 10 italic",
                                  justify=LEFT, bg=background, fg="maroon",
                                  padx=10, pady=10)
        self.results_text.grid(row=1)

        # results Output goes here.. (row 2)

        # Generate string from list of calculations...
        results_string = "ffff"

        # if len(calc_results) > 7:
        #     for item in range(0, 7):
        #         results_string += calc_results[len(calc_results)
        #                                        - item - 1]+"\n"

        # else:
        #     for item in calc_results:
        #         results_string += calc_results[len(calc_results) -
        #                                        calc_results.index(item) - 1] + "\n"
        #         self.results_text.config(text="Here is your calculation "
        #                                       "results.  You can use the "
        #                                       "export button to save this "
        #                                       "data to a text file if "
        #                                       "desired.")

        # Label to display calculation results to user
        self.calc_label = Label(self.results_frame, text=results_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.results_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold",
                                    command=lambda: self.export(submit_func))
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold",
                                     command=partial(self.close_results, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_results(self, partner):
        # Put results button back to normal...
        partner.submit_btn.config(state=NORMAL)
        self.results_box.destroy()

    def export(self, submit_func):
        Export(self, submit_func)


class Export:
    def __init__(self, partner, submit_func):

        print(submit_func)

        background = "#a9ef99"     # Pale green

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the "
                                                         "box below and press the "
                                                         "Save button to save your "
                                                         "calculation results to a "
                                                         "text file.",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you "
                                                         "enter below already "
                                                         "exists, its contents "
                                                         "will be replaced with "
                                                         "your calculation results",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_results(partner, submit_func)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_results(self, partner, submit_func):

        # Regular expression to check filname is valid
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each item
            for item in submit_func:
                f.write(item + "\n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()



def submit_func(): 
    team1 = something.team1_selected.get()
    team2 = something.team2_selected.get()
    f = open("formatted_scores.txt", "r")

    if team1 == team2 or team1 == "" or team2 == "":
        print("you are an idiot")
    else:
        pos = 2
        for line in f:
            split_code(line)
            old_game_id = GAME_ID[pos-1]
        #print("Test old game id: ", old_game_id, " is == to ", GAME_ID[pos-1])
            if old_game_id == GAME_ID[pos]:
                if (TEAM_ABBREVIATION[pos] == team1 or TEAM_ABBREVIATION[pos+-1] == team1) and (TEAM_ABBREVIATION[pos] == team2 or TEAM_ABBREVIATION[pos+-1] == team2):
                    print("----------------------------")
                    print("There is a match")
                    print_records(GAME_ID, old_game_id)
                    print("----------------------------")     
            pos += 1

     
            


def control_break(id,match_arr):
    if id == match_arr[pos]:
        print("There is a match")
        print_records(id, match)
file.close()
finish_up()
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("NBA Game Finder")
    something = results_lookup()
    root.mainloop()

