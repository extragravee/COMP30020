

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