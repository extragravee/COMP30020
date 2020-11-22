import Data.List

-- LINKED LIST SUMMING UP
data List a = ListNode a (List a) | ListEnd

sumLinkedList :: Num a => List a -> a
sumLinkedList ListEnd = 0
sumLinkedList (ListNode a lst) = a + sumLinkedList lst 

data MyBool = MyTrue | MyFalse
            deriving(Eq, Show)


-- TREE FUNCTIONS
-- size of tree (total number of nodes)
data Tree a = Node a (Tree a) (Tree a) | Empty

size:: Tree a-> Int
size Empty = 0
size (Node _ left right) = 1 + size left + size right

-- -- count leaves tree
-- countleaves:: Tree -> Int
-- countleaves Leaf = 1
-- countleaves (Node _ _ l r) = countleaves l + countleaves r

tree = Node 3 (Node 9 (Node 10 Empty Empty) (Node 5 Empty Empty)) (Node 7 Empty Empty)

-- height of the tree
height :: Tree a -> Int
height Empty = 0
height (Node _ l r) = max (1 + height l) (1 + height r)

-- diameter of the tree
-- maximum width of the tree (farther left <-> farthest right)

left :: Tree a -> Int
left Empty = 0
left (Node _ l r) = max (1 + left l) (-1 + left r)

right :: Tree a -> Int
right Empty = 0
right (Node _ r l) = max (1 + right l) (-1 + right r)

diameter:: Tree a -> Int
diameter t = abs $ right t - (left t)

-- in order traversal bst
elements:: Tree a -> [a]
elements Empty = []
elements (Node x left right) = elements left ++ [x] ++ elements right

-- search bst function
search :: Ord a => a -> Tree a -> Bool
search _ Empty = False 
search elt (Node x l r)
    | elt == x = True 
    | elt < x  = search elt l
    | otherwise = search elt r

-- insert item into bst
insertt:: Ord a => a -> Tree a -> Tree a
insertt x Empty = (Node x Empty Empty)
insertt x (Node y l r)
    | x == y = Node y l r
    | x < y  = Node y (insertt x l) r
    | otherwise = Node y l (insertt x r)

-- build a bst, inserts right most item first
buildtree:: Ord a => [a] -> Tree a
buildtree [] = Empty
buildtree (x:xs) = insertt x (buildtree xs)

-- tally bst (add one to target in bst)
tally_bst :: Tree -> String -> Tree
tally_bst (Node key value left right) target
    | target < key = (Node key value (tally_bst left) right)
    | target > key = (Node key value left (tally_bst right))
    | otherwise = (Node key (value+1) left right

tally_bst Leaf target = Node target 1 Leaf Leaf

-- big bst function TREESORT------------------------------
data Tree a = Empty | Node a (Tree a) (Tree a)

insert :: Ord a => a -> Tree a -> Tree a
insert x Empty = Node x Empty Empty
insert x (Node y l r)
    | x == y = Node y l (insert x r)
    | x < y  = Node y (insert x l) r
    | x > y  = Node y l (insert x r)
    
buildtree:: Ord a => [a] -> Tree a
buildtree []     = Empty
buildtree (x:xs) = insert x (buildtree xs)

flatten:: Ord a => Tree a -> [a]
flatten Empty = []
flatten (Node x l r) = flatten l ++ (x:flatten r)

treesort:: Ord a => [a] -> [a]
treesort [] = []
treesort lst = flatten (buildtree lst)
-------------------------------------------------------------------

-- Create sublists of some list (all combinations)
sublists:: [a] -> [[a]]
sublists [] = [[]]
sublists (x:xs) = (map (x:) (sublists xs)) ++ sublists xs



-- TYPES HASKELL TYPES
data ChessPiece = ChessPiece Color Rank

data Color = Black | White
data Rank  = King | Queen | Rook | Bishop | Knight | Pawn

instance Show ChessPiece where
    show = showPiece
    
instance Show Color where
    show = showColor

instance Show Rank where
    show = showRank
    
showPiece:: ChessPiece -> String
showPiece (ChessPiece c r) = show c ++ show r

showColor:: Color -> String
showColor Black = "B"
showColor White = "W"

showRank:: Rank -> String
showRank King  = "K"
showRank Queen = "Q"
showRank Rook  = "R"
showRank Bishop= "B"
showRank Knight= "N"
showRank Pawn  = "P"

toColor:: Char -> Maybe Color
toColor 'W' = Just White
toColor 'B' = Just Black
toColor _ = Nothing

toRank:: Char -> Maybe Rank
toRank 'K' = Just King
toRank 'Q' = Just Queen
toRank 'R' = Just Rook
toRank 'B' = Just Bishop
toRank 'P' = Just Pawn
toRank 'N' = Just Knight
toRank _ = Nothing

toChessPiece :: String -> Maybe ChessPiece
toChessPiece str = do
    case something str of
        [c,r] -> do
            color <- toColor c
            rank <-  toRank r
            return $ ChessPiece color rank
        _ -> Nothing

    
something str = filter (/= ' ') str