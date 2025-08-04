import sys
import time
import os
from Note import Note

#To-Do: fix middle c
# change lines

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
            for subIndex in index:
                if row == NotesToIndex[subIndex.note]:
                    board[row] += subIndex.lengOfNote; printedNote = True
                    
                    if subIndex.sharpFlat: board[row] += subIndex.sharpFlat
                    else: board[row] += note[0]
            
            if printedNote:
                continue
            
            if (row < 26 and row > 8): board[row] += note
            else: board[row] += "  "

        sys.stdout.write(f"\033[{len(board)}F")

        for line in board: sys.stdout.write(f"\r{line.ljust(len(board))}\n")

        sys.stdout.flush()
        time.sleep(0.2)


    




def validateNotesInput(input):

    
    # return input.split(',')
    note1 = Note('A5', 'O', 'b')   # C-flat 4
    note2 = Note('E4', 'O', '')    # E natural 4
    note3 = Note('F4', 'Q', '#')   # F-sharp 4
    note4 = Note('G4', 'Q', '')    # G natural 4
    note5 = Note('A4', 'H', 'b')   # A-flat 4
    note6 = Note('B4', 'H', '')    # B natural 4
    note7 = Note('D4', 'O', '#')   # D-sharp 4
    note8 = Note('E6', 'Q', '')



    return [
        (note1, note3),  # Cb4 and F#4 stacked
        (note5,),        # Ab4
        (note7,),        # D#4
        (note2, note4),  # E4 and G4 stacked
        (note6,),        # B4
        (note8, note1),  # C4 and Cb4 stacked
    ]


if __name__ == "__main__" and len(sys.argv) == 2:
    generateNotes(sys.argv[1])