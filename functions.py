from variables import *
import tkinter as tk
from tkinter import ttk

TITLE = "Title"
COL_HEADING = "Heading"

MENU_LIST = ["1. Print Scores", 
              "2. Print Teams",
              "3. Print a team's records", 
              "4. Find a matching Game ID", 
              "0. Exit"]

file = open("formatted_scores.txt", "r")

#submit button

root = tk



def get_ready():
  print(TITLE)
  print(COL_HEADING)
  empty_lists()
#end get_ready() funcion

def menu_input():
  print("Select from the list below:\n")
  pos = 0
  for x in MENU_LIST:
    print(MENU_LIST[pos])
    pos += 1
  user_select = int(input("Your choice: >>"))
  print()
  return user_select

def duplicate_function(x):
    return list(dict.fromkeys(x))
#end duplicate_function() funcion

def empty_lists(): # empty all the items in the list
  sports_teams_dict.clear()
  GAME_ID.clear()
  TEAM_ID.clear()
  GAME_DATE_EST.clear()
  TEAM_ABBREVIATION.clear()
  TEAM_CITY_NAME.clear()
  TEAM_WINS_LOSSES.clear()
  PTS_QTR1.clear()
  PTS_QTR2.clear()
  PTS_QTR3.clear()
  PTS_QTR4.clear()
  PTS.clear()
  FG_PCT.clear()
  FT_PCT.clear()
  FG3_PCT.clear()
  AST.clear()
  REB.clear()
  TOV.clear()
#end empty list() funcion

def split_code(line):
  splitLine = line.split(",")
  GAME_ID.append(splitLine[0])
  TEAM_ID.append(splitLine[1])
  GAME_DATE_EST.append(splitLine[2])
  TEAM_ABBREVIATION.append(splitLine[3])
  TEAM_CITY_NAME.append(splitLine[4])
  TEAM_WINS_LOSSES.append(splitLine[5])
  PTS_QTR1.append(splitLine[6])
  PTS_QTR2.append(splitLine[7])
  PTS_QTR3.append(splitLine[8])
  PTS_QTR4.append(splitLine[9])
  PTS.append(splitLine[10])
  FG_PCT.append(splitLine[11])
  FT_PCT.append(splitLine[12])
  FG3_PCT.append(splitLine[13])
  AST.append(splitLine[14])
  REB.append(splitLine[15])
  TOV.append(splitLine[16])

def remove_team_duplicates():
  teams_abb = []
  teams_city = []
  array_loop = 0
  for x in TEAM_CITY_NAME: 
    teams_city.append(TEAM_CITY_NAME[array_loop])
    teams_abb.append(TEAM_ABBREVIATION[array_loop])
    array_loop += 1

  mylist1 = duplicate_function(teams_city) # Create a Dictionary to remove the duplicates
  mylist2 = duplicate_function(teams_abb) # Create a Dictionary to remove the duplicates
  mylist1.pop(0)
  mylist2.pop(0)
  #print("City Names (duplicates removed): ", mylist1)
  #print("City Names (duplicates removed): ", mylist2)

  array_loop = 0
  for x in mylist1:
    sports_teams_dict[mylist2[array_loop]] = mylist1[array_loop]
    array_loop += 1
  #print("In a dictionary: ", thisdict)

def print_teams_abb():
  print("Dic ABB: ", sorted(sports_teams_dict))

def print_records(item_arr, match):
  array_loop = 0
  for x in item_arr:
    if item_arr[array_loop] == match:
      print("Record: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(GAME_ID[array_loop], TEAM_ID[array_loop], GAME_DATE_EST[array_loop], 
              TEAM_ABBREVIATION[array_loop], TEAM_CITY_NAME [array_loop], TEAM_WINS_LOSSES [array_loop], PTS_QTR1 [array_loop], 
              PTS_QTR2 [array_loop], PTS_QTR3 [array_loop], PTS_QTR4 [array_loop], PTS [array_loop], FG_PCT [array_loop], 
              FT_PCT [array_loop], FG3_PCT [array_loop], AST [array_loop], REB [array_loop], TOV [array_loop]))  
    array_loop += 1
#end print_record() function

def find_team_abb():
  print("Which team would you like?")
  print_teams_abb()
  team1 = input("Enter TEAM_ABBREVIATION:>>").upper()
  #print("\nTEAM_ABBREVIATION is: " + team1)
  print()
  print_records(TEAM_ABBREVIATION, team1)
# end find_team_abb() function



def find_match():
  f = open("formatted_scores.txt", "r")
  #read data
  pos = 0
  for line in f:
    split_code(line)
    
    old_game_id = GAME_ID[pos-1]
    #print("Test old game id: ", old_game_id, " is == to ", GAME_ID[pos-1])
    if old_game_id == GAME_ID[pos]:
      print("----------------------------")
      print("There is a match")
      print_records(GAME_ID, GAME_ID[pos])
      print("----------------------------")
    pos += 1

def control_break(id,match_arr):
  if id == match_arr[pos]:
    print("There is a match")
    print_records(id, match)

def read_file():
  #read data
  pos = 0
  for line in file:
    split_code(line)
#end read_file() function

def print_scores_file():
  f = open("formatted_scores.txt", "r")
  for x in f:
    print(x)



def finish_up():
  print("\nEnd of Program")