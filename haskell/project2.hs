

data Pitch = Pitch Char Char
    deriving (Eq)

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

feedback :: [Pitch] -> [Pitch] -> (Int, Int, Int)
feedback target guess = (pitches, notes, octaves)
                     where pitches = countMatches target guess --change to remove matched pitch
                           notes   = countMatches (map noteFromPitch target) (map noteFromPitch guess)
                           octaves = countMatches (map octFromPitch target) (map octFromPitch guess)
--countPitches [Pitch 'A' '1',Pitch 'B' '2',Pitch 'A' '3'] [Pitch 'A' '1',Pitch 'A' '2',Pitch 'B' '1']

noteFromPitch:: Pitch -> Char
noteFromPitch (Pitch x _) = x

octFromPitch:: Pitch -> Char
octFromPitch (Pitch _ x) = x


countMatches:: Eq a => [a] -> [a] -> Int
countMatches _ [] = 0
countMatches target (x:xs)
    | elem x target = 1 + countMatches target xs
    | otherwise     = countMatches target xs
