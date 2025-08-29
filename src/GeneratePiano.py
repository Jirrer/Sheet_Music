import sys
import time
import os
from Note import Note

# To-Do
# Make time signiture
# 

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

songNotes = None

def main(): 
    if validateNotesInput(): generateNotes()
    else: exit(2)

def generateNotes():
    global songNotes

    board = [" "] * 34

    for notesIndex in songNotes: 
        for notes in notesIndex:
            createNextLine(board, notes)

        board = createNewMeasure(board)

def createNextLine(board, currentNotes):
    for row in range(len(board)):
        if row % 2 == 0 or row == len(board) / 2: note = "  "
        else: note = "--"

        printedNote = False
        for notes in currentNotes:
            if row == NotesToIndex[notes.note]:
                board[row] += lengthToSymbol[notes.lengOfNote]; printedNote = True

                if notes.sharpFlat: board[row] += notes.sharpFlat
                else: board[row] += note[0]

        if not printedNote:
            if (row < 26 and row > 8): board[row] += note
            else: board[row] += "  "


    updateBoard(board)

def createNewMeasure(newBoard):
    for row in range(len(newBoard)):
        if (row < 26 and row > 8): newBoard[row] += " | "
        else: newBoard[row] += "   "
    
    return newBoard
        
def updateBoard(newBoard):
    os.system('cls' if os.name == 'nt' else 'clear')

    sys.stdout.write(f"\033[{len(newBoard)}F")

    for line in newBoard: sys.stdout.write(f"\r{line.ljust(len(newBoard))}\n")

    sys.stdout.flush()
    time.sleep(0.2)

def validateNotesInput():
    global songNotes

    measure = lambda *ns: tuple((n,) for n in ns)

    songNotes = [
            measure(
                Note('C4', 4, ''), Note('C4', 4, ''), 
                Note('G4', 4, ''), Note('G4', 4, '')
            ),
            measure(
                Note('A4', 4, ''), Note('A4', 4, ''), 
                Note('G4', 2, '')
            ),
            measure(
                Note('F4', 4, ''), Note('F4', 4, ''), 
                Note('E4', 4, ''), Note('E4', 4, '')
            ),
            measure(
                Note('D4', 4, ''), Note('D4', 4, ''), 
                Note('C4', 2, '')
            ),
            measure(
                Note('C4', 4, ''), Note('C4', 4, ''), 
                Note('D4', 4, ''), Note('D4', 4, '')
            ),
            measure(
                Note('E4', 4, ''), Note('E4', 4, ''), 
                Note('F4', 2, '')
            ),
            measure(
                Note('G4', 4, ''), Note('G4', 4, ''), 
                Note('A4', 4, ''), Note('A4', 4, '')
            ),
            measure(
                Note('B4', 4, '#'), Note('B4', 4, 'B'), 
                Note('C5', 2, '#')
            )
        ]

    return True