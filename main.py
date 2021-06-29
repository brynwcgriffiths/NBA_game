from functions import *
from tkinter import *
from functools import partial  # To prevent unwanted windows

import re
import random

global results_dict
file = open("formatted_scores.txt", "r")


class Search:
    def __init__(self):

        # Formatting variables
        favicon = PhotoImage(file='nbalogo.png')

        # Setting icon of master window
        root.iconphoto(False, favicon)

        # Initialise list to hold Results of user search
        self.all_results_list = []

        self.menubar = tk.Menu()
        self.nav = tk.Menu()
        self.menubar.add_cascade(label="File", menu=self.nav)

        self.nav.add_command(label="Help", command=self.help)
        self.nav.add_separator()
        self.nav.add_command(label="Exit", command=root.destroy)

        root.configure(menu=self.menubar)

        # Frame
        background_color = "lightblue"
        self.lookup_frame = Frame(bg=background_color, pady=10)

        self.lookup_frame.grid()

        # Heading (row 0)
        self.sports_heading_label = Label(self.lookup_frame,
                                          text="NBA Game Finder",
                                          font="Arial 24 bold",
                                          bg=background_color,
                                          padx=10,
                                          pady=10,
                                          justify=CENTER)
        self.sports_heading_label.grid(row=0, column=1)

        # User instructions (row 1)
        self.sports_instructions_label = Label(
            self.lookup_frame,
            text=
            "Select two teams and click submit to view the game stats for games between your selected teams during 2016-17 NBA season.",
            font="Arial 12 italic",
            wrap=350,
            justify=CENTER,
            bg=background_color,
            padx=10,
            pady=10)
        self.sports_instructions_label.grid(row=1, column=1)

        # Combobox creation\

        n = tk.StringVar()
        self.team1_selected = ttk.Combobox(self.lookup_frame,
                                           width=5,
                                           textvariable=n,
                                           state="readonly")

        # Adding combobox drop down list
        self.team1_selected['values'] = duplicate_function(
            sorted(TEAM_ABBREVIATION))

        self.team1_selected.grid(column=0, row=5, padx=5, pady=20)
        self.team1_selected.current()

        # Team input (row 5)
        self.team_input_label = Label(self.lookup_frame,
                                      text="VS",
                                      font="Arial 10 italic bold",
                                      justify=CENTER,
                                      bg=background_color,
                                      padx=10,
                                      pady=10)
        self.team_input_label.grid(row=5, column=1)

        # Combobox creation
        n = tk.StringVar()
        self.team2_selected = ttk.Combobox(self.lookup_frame,
                                           width=5,
                                           textvariable=n,
                                           state="readonly")

        # Adding combobox drop down list
        self.team2_selected['values'] = duplicate_function(
            sorted(TEAM_ABBREVIATION))
        self.team2_selected.grid(column=2, row=5, padx=5, pady=20)
        self.team2_selected.current()

        # Submit button
        self.submit_btn = Button(self.lookup_frame,
                                 font="Arial 12 bold",
                                 text="Submit",
                                 width=5,
                                 command=self.results)
        self.submit_btn.grid(row=8, column=1, pady=15)

#end class results lookup

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(
            text="Please select your teams "
            "and then push the submit button. \n\n"
            "The tabs allow you to swich between games "
            "making it easy to find and view the Results you're looking for.  \n\n"
            "You can "
            "also export the Results of "
            "your search to a text file if desired.")
						
    def results(self):
        get_results = Results(self)


class Help:
    def __init__(self, partner):

        background = "orange"
        # disable help button
        partner.nav.entryconfig("Help", state="disabled")

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame,
                                 text="Help / Instructions",
                                 font="arial 14 bold",
                                 bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               text="",
                               justify=LEFT,
                               width=40,
                               bg=background,
                               wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame,
                                  text="Dismiss",
                                  width=10,
                                  bg="orange",
                                  font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.nav.entryconfig("Help", state="normal")
        self.help_box.destroy()

#end class help


class Results:
    def __init__(self, partner):

        background = "#a9ef69"  # Pale green

        # disable submit button
        partner.submit_btn.config(state=DISABLED)

        # Sets up child window (ie: Results box)
        self.results_box = Toplevel()

        # If users press cross at top, closes Results and 'releases' submit button
        self.results_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_results, partner))

        # Set up GUI Frame
        self.results_frame = Frame(self.results_box, width=300, bg=background)
        self.results_frame.grid()

        # Set up Results heading (row 0)
        self.how_heading = Label(self.results_frame,
                                 text="Results",
                                 font="arial 19 bold",
                                 bg=background)
        self.how_heading.grid(row=0)

        # Results text (label, row 1)
        self.results_text = Label(self.results_frame,
                                  text="Here are your Results. Please use the "
                                  "export button to create a text "
                                  "file of your search Results.",
                                  wrap=250,
                                  font="arial 10 italic",
                                  justify=LEFT,
                                  bg=background,
                                  fg="maroon",
                                  padx=10,
                                  pady=10)
        self.results_text.grid(row=1)

        # Results Output goes here.. (row 2)

        # Generate string from list of results
        submitted_results = {}
        submitted_results = submit_func()
        results_string = ""
        for item in submitted_results:
          results_string = results_string + "\n" + submitted_results[item]
        print(results_string)

        # Label to display Results to user
        self.calc_label = Label(self.results_frame,
                                text=results_string,
                                bg=background,
                                font="Arial 8",
                                justify=LEFT)
        self.calc_label.grid(row=2)

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.results_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame,
                                    text="Export",
                                    font="Arial 12 bold",
                                    command=lambda: self.export(submit_func))
        self.export_button.grid(row=0, column=0)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame,
                                     text="Dismiss",
                                     font="Arial 12 bold",
                                     command=partial(self.close_results,
                                                     partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_results(self, partner):
        # Put Results button back to normal...
        partner.submit_btn.config(state=NORMAL)
        self.results_box.destroy()

    def export(self, submit_func):
        Export(self, submit_func)

def submit_func():
    results_dict = {}

    team1 = search.team1_selected.get()
    team2 = search.team2_selected.get()
		

    if team1 == team2 or team1 == "" or team2 == "":
        #idiot_message = ("you are an idiot")
        error_message = {"Error": "You have selected the same team. Please try again."}
        return error_message
    else:
        pos = 0
        for line in file:
            split_code(line)
            old_game_id = GAME_ID[pos - 1]
            
            if old_game_id == GAME_ID[pos]:
                if (TEAM_ABBREVIATION[pos] == team1
                        or TEAM_ABBREVIATION[pos +- 1] == team1) and (
                            TEAM_ABBREVIATION[pos] == team2
                            or TEAM_ABBREVIATION[pos +- 1] == team2):
                    submit_print = print_records(GAME_ID, old_game_id)
                    print("----------------------------")
                    print("There is a match")
                    
                    # placing the Results into a dictionary to return where function is called
                    results_dict[GAME_ID[pos]]= submit_print
                    print("Results Dict: ", results_dict)
                    print("----------------------------")
            pos += 1
        return results_dict#submit_print


class Export:
    def __init__(self, partner, submit_func):

        #print(submit_func)

        background = "#a9ef99"  # Pale green

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame,
                                 text="Export / Instructions",
                                 font="arial 14 bold",
                                 bg=background)
        self.how_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a filename in the "
                                 "box below and press the "
                                 "Save button to save your "
                                 "calculation Results to a "
                                 "text file.",
                                 justify=LEFT,
                                 width=40,
                                 bg=background,
                                 wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame,
                                 text="If the filename you "
                                 "enter below already "
                                 "exists, its contents "
                                 "will be replaced with "
                                 "your calculation Results",
                                 justify=LEFT,
                                 bg="#ffafaf",
                                 fg="maroon",
                                 font="Arial 10 italic",
                                 wrap=225,
                                 padx=10,
                                 pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame,
                                    width=20,
                                    font="Arial 14 bold",
                                    justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame,
                                      text="",
                                      fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(
            self.save_cancel_frame,
            text="Save",
            command=partial(lambda: self.save_results(partner, submit_func)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame,
                                    text="Cancel",
                                    command=partial(self.close_export,
                                                    partner))
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
            self.save_error_label.config(
                text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            # If there are no errors, generate text file and then close dialogue
            # add .txt suffix!
            filename = filename + ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at end of each 
            item_results_dict = submit_func()
            print("Line 458: ", item_results_dict)
            f.write("RESULTS\n")

            #loop through item Results dictionary to print each result record
            for item in item_results_dict:
              f.write(item_results_dict[item])
            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


def control_break(id, match_arr):
    if id == match_arr[pos]:
        print("There is a match")
        print_records(id, match)


file.close()
# main routine
if __name__ == "__main__":
    root = Tk()
root.geometry("600x400")
root.minsize(510, 325)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.resizable(True, True)
root.configure(bg="lightblue")
root.title("NBA Game Finder")
search = Search()
root.mainloop()
finish_up()
