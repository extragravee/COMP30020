{-
COMP30020 - Declarative Programming
Project 2 - The Game of Musician

Author : Sidakpreet Mann
         921322
Purpose: This file is intended to play the game of musician, a logical guessing
         game. One player is a composer whose task is to produce a certain chord
         (comprised of three pitches, where each pitch comprises of a note and 
         an octave). The second player will then guess this chord, and receive
         feedback from player one in the form of a triple(# correct pitches, 
         # correct notes, # correct octaves).
         
         The idea is to guess the target chord (set by player one) in as few 
         guesses as possible. This code aims to probabilistically narrow down on
         a target for which a certain feedback score is received, and uses that
         to logically make a new guess. Each of these guesses aims to narrow
         down the solution space, until we are left with the ideal candidate.
         
         The big picture:
             0. At any point in time, GameState data structure tracks
                the currently viable candidate chords.
             1. Produce an initial guess found through testing and writing a 
                script for which there is a narrow solution space [initialGuess]
             2. Use the feedback produced for this initialGuess to filter chords
                that could be target chords [filterNewState] after each time a 
                new guess is made [nextGuess]
             3. This process repeats until an exact match is found.
-}
      
import Data.List
import Debug.Trace

-- check every tenth starting chord
main :: IO ()
main = putStrLn $ "Average across 1330 chords: " ++show(answer all)
    where all = allPossibleChords

-- all_answers:: Double
-- all_answers = answer (take 1 all) all
--     where all = allPossibleChords


answer:: [Chord] -> Double
answer (all) = (simulate_testing all all) / 1330 


simulate_testing :: [Chord]-> [Chord] -> Double
simulate_testing [] _ = 0
simulate_testing (target:targets) all = ans + simulate_testing targets all
--trace (show target ++ " " ++ show ans)
      where ans = keep_guessing target initialGuess

keep_guessing :: Chord -> (Chord, GameState) -> Double
keep_guessing target (chord, state)
    | fb == (3,0,0) = 1
    | otherwise     = 1 + keep_guessing target (nextGuess (chord,state) fb) 
    where fb = feedback target chord

{- 
   Pitch
   =====
   [Pitch Note Octave] data structure
   Records a note and an octave as a char and a char repectively.
   This function is used in conjunction with validPitch to ensure no invalid
   chars can be recorded in a Pitch.
-}
data Pitch = Pitch Char Char
    deriving (Eq, Ord)

-- Show a pitch as a NoteOctave String
instance Show Pitch where
    show = showPitch

showPitch:: Pitch -> String
showPitch (Pitch note octave) = [note, octave]

-- Ensure that a note is one of A-G alphabet inclusive, and an octave is 1/2/3.
validPitch:: Pitch -> Bool
validPitch (Pitch n o) = (elem n ['A'..'G']) && (elem o "123")

{-
   toPitch
   =======
   Expects a string input in the format NoteOctave and returns either a 
   Just Pitch data structure, or Nothing if input string is invalid.
-}
toPitch:: String -> Maybe Pitch
toPitch str
    | ((length str) /= 2)  = Nothing        -- if string is longer than 2 chars
    | validPitch pitch     = Just pitch     -- if string reps a valid pitch
    | otherwise            = Nothing        -- any other case
    where pitch  = Pitch note octave
          note   = str !! 0
          octave = str !! 1


{-
   feedback
   ========
   Expects a target and a guess Chord repesectively, and returns a triple of 
   feedback score in the format:
   (# correct pitches, # correct notes, # correct octaves)
   
   If a certain pitch matches, then correct notes and correct octaves do not
   count notes or octaves within that pitch again as correct notes or octaves.
-}
type Chord = [Pitch]

feedback:: Chord -> Chord -> (Int,Int,Int)
feedback target guess = (pitches, notes, octaves)
                 where newTarget = target \\ guess
                       newGuess  = guess \\ target
                       pitches   = (length target) - (length newTarget)
                       notes     = countElem noteFromPitch newTarget newGuess
                       octaves   = countElem octFromPitch  newTarget newGuess

-- Takes in an a function as an argument which extracts either a note or an 
-- octave from a pitch, receives the target and guess chords with matching
-- pitches removed, and returns length of the intersect between target and guess
-- notes or octaves.
countElem:: (Pitch -> Char) -> Chord -> Chord -> Int
countElem f newTarget newGuess = (length newTarget) - (length (a \\ b))
                            where a = map f newTarget
                                  b = map f newGuess

-- helper functions to extract a note / octave from a Pitch data structure
noteFromPitch:: Pitch -> Char
noteFromPitch (Pitch x _) = x

octFromPitch:: Pitch -> Char
octFromPitch (Pitch _ x) = x


-- Receives a list of valid notes, and produces all valid pitches
allPossiblePitches:: String -> [Pitch]
allPossiblePitches [] = []
allPossiblePitches (x:xs) = [ Pitch x y | y <- "123"] ++ allPossiblePitches xs

-- Constant that generates and records the valid distinct 1330 chords
allPossibleChords:: [Chord]
allPossibleChords = nub (validChord [[x,y,z]| x<-pitches,y<-pitches,z<-pitches])
                 where pitches = allPossiblePitches ['A'..'G']

-- filters out chords that have duplicate pitches
validChord:: [Chord] -> [Chord]
validChord [] = []
validChord (x:xs)
    | length (nub x) == 3  = (sort x):validChord xs
    | otherwise            = validChord xs

{-
   GameState
   =========
   Records currently viable candidate chords.
-}
data GameState = GameState [Chord]
    deriving (Show)


{-
   initialGuess
   ============
   Constant that recordes a tuple(initial hardcoded guess chord, GameState)
   
   Hardcoded initial guess based on a python script I created to estimate the
   guess chord with smallest solution space at the beggining.
   
   Intial GameState contains all possible chords.   
-}
 
initialGuess:: (Chord, GameState)
initialGuess = (pitch, gstate)
        --   where pitch  = [Pitch 'A' '1', Pitch 'B' '1', Pitch 'C' '2'] --4.46
    --       where pitch  = [Pitch 'B' '3', Pitch 'G' '1', Pitch 'E' '1'] --4.43
      --       where pitch  = [Pitch 'C' '2', Pitch 'F' '1', Pitch 'E' '1'] --4.45
             --where pitch  = [Pitch 'D' '3', Pitch 'G' '2', Pitch 'A' '2'] --4.43
        --     where pitch  = [Pitch 'A' '3', Pitch 'B' '2', Pitch 'C' '3'] --4.46
             --where pitch  = [Pitch 'G' '3', Pitch 'G' '2', Pitch 'A' '3'] --4.54
             -- where pitch  = [Pitch 'A' '2', Pitch 'A' '1', Pitch 'C' '1'] --4.54
             -- where pitch  = [Pitch 'D' '1', Pitch 'D' '2', Pitch 'F' '2'] -- 4.63
             -- where pitch  = [Pitch 'G' '3', Pitch 'E' '2', Pitch 'E' '3'] -- 4.60
             -- where pitch  = [Pitch 'A' '1', Pitch 'E' '1', Pitch 'G' '2'] -- 4.47
             where pitch  = [Pitch 'B' '3', Pitch 'G' '1', Pitch 'E' '1'] --
                   gstate = GameState allPossibleChords


{-
   nextGuess
   =========
   Receives the last guessed chord, and last GameState (containing all currently
   viable candidate chords) and the feedback for the last guessed chord, and
   based on the two creates a new GameState - narrows down the candidate chords
   further using the feedback produced for the last guess.
-}
nextGuess :: (Chord, GameState) -> (Int, Int, Int) -> (Chord, GameState)
nextGuess (chord, GameState (state)) fb = (newChord, GameState newState)
                                where newState = filterNewState chord fb state
                                      newChord = selectNextGuess newState
                                      --newChord = selectGuess (chord, fb) newState []
{-
-- (lastChord, fb) , lastState, accum(newstate) => (newGuess, newState)
selectGuess:: (Chord, (Int, Int Int)) -> [Chord] -> [((Int, Int, Int), Int, Chord)]
selectGuess _ [] accum = accum
selectGuess (lastChord, fblast) (x:xs) accum
    | fblast == fb && not (elem (fb, _) accum) = selectGuess (lastChord, fblast) xs (fb,0,x):accum
    | fblast == fb && (elem (fb, _) accum)     = selectGuess (lastChord, fblast) xs (addOne fb accum):accum
    where fb = feedback lastChord x
     -}    

          
-- helper function to help filter the current GameState, keeping only the
-- candidates that produced the same feedback (when tested against our last
-- guessed chord) as our last guessed chord's feedback when tested against the
-- actual target.
filterNewState :: Chord -> (Int, Int, Int) ->[Chord] -> [Chord]
filterNewState _ _ [] = []
filterNewState chord fb (x:xs)
    | feedback chord x == fb = x:filterNewState chord fb xs
    | otherwise              = filterNewState chord fb xs


{-
   selectNextGuess
   ===============
   This function contains the bulk of the logic for the selection of guesses.
   The method is as follows:
   
       1. It receives the list of Chords as recorded in the current game state
       2. Produces a list [fbs] (feedbacks) which records tuples of the feedback
          generated for each chord pair within the currently viable chords,
          and the chord that was considered as the target chord (chord x)
       3. This list of tuples is then sorted into [sortedFbs] list, so that the
          identical feedbacks are next to each other. Done so that it's easier
          to group all identical feedbacks together.
       4. Generates groups within feedbacks, now each element in [groupd] array
          is a list of tuples with the same feedback. These can be aggregated
       5. Each elemnt in the [groupd] array is then mapped to a ratio score
          of # of candidates that produced a distinct feedback squared divided 
          by the total number of candidate chords processed.
       6. The minimum of these ratios is selected into [avgs], as this is the
          element with the lowest ratio of candidate chords, hence the smallest
          solution space (locally determined)
       7. The chord with the lowest ratio [avgs] is then returned as the next
          guess to be made in the [nextGuess] function.
-}
selectNextGuess :: [Chord] -> Chord
selectNextGuess (x:xs) = snd avgs
        where fbs       = [(uncurry feedback (x,y), x)| x<-(x:xs), y<-(x:xs)]
              sortedFbs = sort fbs
              numElms   = length sortedFbs
              
              groupd    = groupBy (\a b -> fst a == fst b) sortedFbs
              
              avgs      = minimum (map helper groupd)
              helper    = \x -> ((length x^2) `div` numElms, snd (x!!0))




