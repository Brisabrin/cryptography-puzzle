
import time
## leave this here to allow file IO features to be tested in repl.it!
def make_files():
  open("words.txt", "w").write("""#+/084&"\n#3*#%#+\n8%203:\n,1$&\n!-*%\n.#7&33&\n#*#71%\n&-&641'2\n#))85\n9&330*""")
  open("clues.txt", "w").write("""A#\nM*\nN%""")
  open("solved.txt", "w").write("""ACQUIRED\nALMANAC\nINSULT\nJOKE\nHYMN\nGAZELLE\nAMAZON\nEYEBROWS\nAFFIX\nVELLUM""")
make_files()

## TASK 1
def open_file(filename):
  read_file= open(filename,"r").read()
  return read_file
  
code_puzzle=open_file("words.txt")

## TASK 2
PAIRINGS={}
read_lines=open("clues.txt","r")

#solution 
sol= open_file("solved.txt")
pairings={}

def initialise_pairings(clues):
  global pairings
  r=clues.readlines()
  pairings={}
  
  for i in r :
    pairings[i[1]]=i[0]
  return pairings

def display_pairings():
  for i in pairings:
    print("The letter {} has the code {}".format(pairings[i],i))
current_puzzle=open_file("words.txt")


def update_puzzle():
  global current_puzzle
  
  for i in pairings:
    current_puzzle=current_puzzle.replace(i,pairings[i])
  return current_puzzle
  
  
  
def delete_pairing(symbol,pairings):
  if any(symbol_input==i for i in pairings):
    pairings.pop(symbol_input)
    
    print("{} is removed".format(symbol_input))
    
  else:
    print("symbol not found ")
def validate_pairings(sym,lett,pair):
  if any(i==sym for i in pair ) or any(pair[i]==letter for i in pair):
      
    if any(i==sym for i in pair):
      print("symbol already used!")
    if any(pair[i]==letter for i in pair):
      print("letter already used!")
  else:
    return True 
def check_win(cur_puz,solution):
  if cur_puz==solution:
    return True 

def display_status():
  code_puzzle.strip(" ")
  char= []
  for i in code_puzzle:
    if i not in char and i!="\n" and  i not in PAIRINGS:
      char.append(i)
  for i in char:
    occur=code_puzzle.count(i)
    frequency=round(occur/(len(code_puzzle))*100)
    print("CODE SYMBOL {} IS FEATURED IN {}% OF THE PUZZLE".format(i,frequency))

## TASK 6 - loop
# game_track=True
# while game_track:

clues=open("clues.txt","r")
initialise_pairings(clues)
  ## MAIN MENU
menu_track=True
while menu_track:
  
  clues=open("clues.txt","r")
  current_puzzle=open_file("words.txt")
  update_puzzle()
  
  menu_track_input=True
  while menu_track_input:
    try:
      time.sleep(1)
      
      menu=int(input("""What do you want to do?
      1. VIEW PUZZLE
      2. ADD LETTER/SYMBOL PAIR
      3. DELETE LETTER/SYMBOL PAIR
      4. VIEW FREQUENCY STATS
      5. QUIT"""))
      
      if menu>=1 and menu<=5 and type(menu) is int:
        menu_track_input=False
    except ValueError:
      print("value error")
    
  
  if menu==1:
    display_pairings()
    print(current_puzzle)

  elif menu==2:
    print(current_puzzle)
    game_track=True
    
    while game_track:
      valid=False
      
      while valid==False:
        enter= True
        
        while enter:
            
          letter=input("WHAT LETTER?\n").upper()
          symbol=input("WHAT SYMBOL?\n").upper()
          
          if letter.isalpha():
            if len(letter)==1 and len(symbol)==1 and symbol!=" " and letter!=" ":
              enter=False
            else:
              print("retry")
        
        if validate_pairings(symbol,letter,pairings):
          valid=True
          
      pairings[symbol]=letter
      update_puzzle()
      
      print(current_puzzle)
      count=0
      
      for i in current_puzzle:
          
        if i in pairings.values():
          count+=1
      if count==len(current_puzzle)-9:
          
        if check_win(current_puzzle,sol):
          print("You have successfully solved the puzzle")
          initialise_pairings(clues)
          
          current_puzzle=open_file("words.txt")
          
          update_puzzle()
          game_track=False
          
        else:
          print("\nUnsuccessful\n")
          initialise_pairings(clues)
          current_puzzle=open_file("words.txt")
          update_puzzle()
          print(current_puzzle)
        
  elif menu==3:
      
    symbol_input=input("input a symbol that you would like to delete")
    delete_pairing(symbol_input,pairings )
    
  elif menu==4:
    display_status()

  elif menu==5:
    menu_track=False
    
    
