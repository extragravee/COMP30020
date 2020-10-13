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

allPossiblePitches:: String -> [Pitch]
allPossiblePitches [] = []
allPossiblePitches (x:xs) = [ Pitch x y | y <- "123"] ++ allPossiblePitches xs

type Chord = [Pitch]

-- generated valid 1330 chords that are possible
allPossibleChords:: [Chord]
allPossibleChords = nub (validChord [[x, y, z] | x <- pitches, y <-pitches, z<-pitches ])
                 where pitches = allPossiblePitches "ABCDEFG"

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

-- hardcoded initial guess
-- found via a python script that generated avg # of targets for all chords 
initialGuess:: (Chord, GameState)
initialGuess = (pitch, gstate)
             where pitch  = [Pitch 'D' '3', Pitch 'F' '1', Pitch 'G' '3']
                   gstate = GameState allPossibleChords

-- inherently being handled by the testing script
nextGuess :: (Chord, GameState) -> (Int, Int, Int) -> (Chord, GameState)
nextGuess (chord, GameState (state)) fb = (newChord, GameState newState)
                                        where newState = filterNewState chord fb state
                                              newChord = selectNextGuess newState

filterNewState :: Chord -> (Int, Int, Int) ->[Chord] -> [Chord]
filterNewState _ _ [] = []
filterNewState chord fb (x:xs)
    | feedback chord x == fb = x:filterNewState chord fb xs
    | otherwise              = filterNewState chord fb xs

-- takes in prev GameState:[Chord]
-- produces all possible feedbacks for remaining targets
selectNextGuess :: [Chord] -> Chord
selectNextGuess (x:xs) = snd (avgs!!0)
                where groupd  = groupBy (\a b -> fst a == fst b) fbs
                      fbs     = sort (map helper allSets)
                      allSets = [(x,y) | x <- (x:xs), y <- (x:xs)]
                      numElms = length allSets
                      helper  = \x -> (uncurry feedback x, x)
                      avgs    = sort (map (\x -> (((length x)*(length x)) `div` numElms, fst (snd (x!!0)))) groupd)
 
--temp = selectNextGuess [[Pitch 'A' '1', Pitch 'B' '1', Pitch 'C' '1'], [Pitch 'A' '1', Pitch 'F' '1', Pitch 'C' '2']]
-- *Main> temp2
-- [((1,1,1),([A1,B1,C1],[A1,F1,C2])),((3,0,0),([A1,B1,C1],[A1,B1,C1])),((3,0,0),([A1,F1,C2],[A1,F1,C2])),((3,0,0),([A1,F1,C2],[A1,F1,C2]))]
-- *Main> temp3 = groupBy (\a b -> fst a == fst b) temp2
-- *Main> temp3
-- [[((1,1,1),([A1,B1,C1],[A1,F1,C2]))],[((3,0,0),([A1,B1,C1],[A1,B1,C1])),((3,0,0),([A1,F1,C2],[A1,F1,C2])),((3,0,0),([A1,F1,C2],[A1,F1,C2]))]]
-- *Main> map length temp3
-- [1,3]
-- *Main> 
