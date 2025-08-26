import sys
import time
import os
from Note import Note

timeSignature = "4/4"

lengthToSymbol = {1:"W",
                  2:"H",
                  4:"Q",
                  8:"E",
                  16:"S"
}

NotesToIndex = {"C4":17,
                "D4":16,
                'E4':15,
                'F4':14,
                'G4':13,
                'A4':12,
                'B4':11,
                'C5':10,
                'D5':9,
                'E5':8,
                'F5':7,
                'G5':6,
                'A5':5,
                'B5':4,
                'C6':3,
                'D6':2,
                'E6':1,
                'F6':0,
                'G6':-1,
                'A6':-1,
                'B6':-1,
                'C7':-2,
                'D7':-2,
                'E7':-2,
                'F7':-2,
                'G7':-2,
                'A7':-2,
                'B7':-2,
                
              
}



def generateNotes(notesInput):
    notesArr = validateNotesInput(notesInput)

    board = [" "] * 34

    for index in notesArr:
        os.system('cls' if os.name == 'nt' else 'clear')

        for row in range(len(board)):
            if row % 2 == 0 or row == len(board) / 2: note = "  "
            else: note = "--"

            printedNote = False
            for notes in index:

                if row == NotesToIndex[notes.note]:
                    board[row] += lengthToSymbol[notes.lengOfNote]; printedNote = True

                    if notes.sharpFlat: board[row] += notes.sharpFlat
                    else: board[row] += note[0]

            if printedNote: continue

            
            if (row < 26 and row > 8): board[row] += note
            else: board[row] += "  "

        sys.stdout.write(f"\033[{len(board)}F")

        for line in board: sys.stdout.write(f"\r{line.ljust(len(board))}\n")

        sys.stdout.flush()
        time.sleep(0.2)


    




def validateNotesInput(input):

    
    # return input.split(',')
    note1 = Note('C4', 4, '')   
    note2 = Note('G4', 4, '')   
    note3 = Note('A4', 2, '')   
    note4 = Note('G4', 4, '')    
    note5 = Note('F4', 4, '')   
    note6 = Note('E4', 4, '')  
    note7 = Note('D4', 4, '')   
    note8 = Note('C4', 1, '')



    return [
        (note1,),  
        (note1,),     
        (note2,),        
        (note2,), 
        (note3,),        
        (note3,), 
        (note4,),
        (note5,),     
        (note5,),        
        (note6,), 
        (note6,),        
        (note7,), 
        (note7,),
        (note8,)
    ]


# if __name__ == "__main__" and len(sys.argv) == 2:
#     generateNotes(sys.argv[1])

if __name__ == "__main__": generateNotes(1)