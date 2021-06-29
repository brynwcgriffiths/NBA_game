from variables import *
import tkinter as tk
from tkinter import ttk

file = open("formatted_scores.txt", "r")
root = tk

def read_file():
  #read data
  pos = 0
  for line in file:
    split_code(line)
#end read_file() function

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

def print_records(item_arr, match):
	array_loop = 0
	for x in item_arr:
		if item_arr[array_loop] == match:
			print_text = ("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(GAME_ID[array_loop], GAME_DATE_EST[array_loop], 
							TEAM_ABBREVIATION[array_loop], TEAM_CITY_NAME [array_loop], PTS_QTR1 [array_loop], 
							PTS_QTR2 [array_loop], PTS_QTR3 [array_loop], PTS_QTR4 [array_loop], PTS [array_loop], FG_PCT [array_loop], 
							FT_PCT [array_loop], FG3_PCT [array_loop], AST [array_loop], REB [array_loop], TOV [array_loop]))  
		array_loop += 1
	return print_text
#end print_record() function




def find_match():
  pos = 0
  for line in file:
    split_code(line)
    
    old_game_id = GAME_ID[pos-1]
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

def duplicate_function(x):
    return list(dict.fromkeys(x))
#end duplicate_function() funcion

def finish_up():
  print("\nEnd of Program")
#end finish_up() function