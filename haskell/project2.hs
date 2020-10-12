import Data.List

data Pitch = Pitch Char Char
    deriving (Eq, Ord)

instance Show Pitch where
    show = showPitch

showPitch:: Pitch -> String
showPitch (Pitch note octave) = [note, octave]

validPitch:: Pitch -> Bool
validPitch (Pitch n o) = (elem n "ABCDEFG") && (elem o "123")

toPitch:: String -> Maybe Pitch
toPitch str
    | ((length str) /= 2)  = Nothing
    | validPitch pitch     = Just pitch
    | otherwise            = Nothing
    where pitch = Pitch note octave
          note  = str !! 0
          octave= str !! 1

-------------------------------------------
-- first is target, next is guess

feedback:: [Pitch] -> [Pitch] -> (Int,Int,Int)
feedback target guess = (pitches, notes, octaves)
                     where newTarget = target \\ guess
                           newGuess  = guess \\ target
                           pitches   = 3 - (length newTarget)
                           notes     = countElem noteFromPitch newTarget newGuess
                           octaves   = countElem octFromPitch  newTarget newGuess

-- takes in a function arg, takes in target and guess and counts
-- the matching notes or octaves depending on the passed function
countElem:: (Pitch -> Char) ->[Pitch] -> [Pitch] -> Int
countElem f newTarget newGuess = (length newTarget) - (length (a \\ b))
                            where a = map f newTarget
                                  b = map f newGuess

noteFromPitch:: Pitch -> Char
noteFromPitch (Pitch x _) = x

octFromPitch:: Pitch -> Char
octFromPitch (Pitch _ x) = x

------------------------------------------------------

-- -- records 
-- data GameState = GameState [Chord]
--                             deriving (Show)

-- initialGuess:: (Chord, GameState)
-- initialGuess = (pitch, gstate)
--              where pitch  = [Pitch 'A' '1', Pitch 'B' '1', Pitch 'C' '1']
--                    gstate = GameState 

-- idea from https://stackoverflow.com/questions/32093912/all-combinations-of-elements-of-two-lists-in-haskell
allPossibleNotes:: String -> [Pitch]
allPossibleNotes [] = []
allPossibleNotes (x:xs) = [ Pitch x y | y <- "123"] ++ allPossibleNotes xs

type Chord = [Pitch]

-- generated valid 1330 chords that are possible
allPossibleChords:: [Chord]
allPossibleChords = nub (validChord [[x, y, z] | x <- notes, y <-notes, z<-notes ])
                 where notes = allPossibleNotes "ABCDEFG"

-- filters out chords that have duplicate pitches
validChord :: [Chord] -> [Chord]
validChord [] = []
validChord (x:xs)
    | length (nub x) == 3  = (sort x):validChord xs
    | otherwise            = validChord xs

--------------------------------------------------
-- contains currently viable candidate chords
data GameState = GameState [Chord]
    deriving (Show)

initialGuess:: (Chord, GameState)
initialGuess = (pitch, gstate)
             where pitch  = [Pitch 'A' '1', Pitch 'B' '1', Pitch 'D' '2']
                   gstate = GameState allPossibleChords

