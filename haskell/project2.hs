

data Note = A|B|C|D|E|F|G
    deriving (Show, Eq)

data Octave = O1|O2|O3
    deriving (Eq)

instance Show Octave where
    show = showOctave

showOctave :: Octave -> String
showOctave O1 = "1"
showOctave O2 = "2"
showOctave O3 = "3"


data Pitch = Pitch Note Octave
    deriving (Eq)

instance Show Pitch where
    show = showPitch

showPitch:: Pitch -> String
showPitch (Pitch n o) = show n ++ showOctave o 
