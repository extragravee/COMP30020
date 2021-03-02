/*
hand_value(+Hand, +Startcard, -Value)
value: int
hand: list of 4 card terms
assumes no duplicate cards dealt

hand_value([card(2, clubs), card(3, diamonds), card(king, spades), card(5, hearts)], card(10, spades),  Score).
*/

hand_value(Hand, Start_card, Score_from_15s) :-
        % check if all cards are valid
        check_card(Start_card),
        valid_cards(Hand),
        
        % get score from 15s
        fifteens([Start_card|Hand], Score_from_15s).
        
        % calculate scores
        % Value is ....
        %Value is Fifteens,
        %fifteens([Hand|Start_card], Fifteens).

% calculates distinct combinations of cards that add upto 15
% fifteens(+List, -Fifteens)
fifteens(Card_list, Score_from_15s) :-
        numerical_repn(Card_list, NumericalList),
        bagof(Comb, combs(NumericalList, Comb), Combs),
        maplist(sumlist, Combs, Sums),
        count_fifteens(Sums, 0, Num_15s),
        Score_from_15s is Num_15s * 2.

% count the number of 15s in a list
% count_fifteens(+List, +Accum, -Num_15s).
count_fifteens([], A, A).
count_fifteens([Head|Tail], Accum, Num_15s) :-
    (   Head = 15 
    ->  A1 is Accum + 1,
        count_fifteens(Tail, A1, Num_15s)
    ;   count_fifteens(Tail, Accum, Num_15s) ).

card_numerical_value(card(Rank, _), Val) :-
    (   integer(Rank)  
    ->  Val is Rank
    ;   Rank = ace ->
        Val is 1
    ;   memberchk(Rank, [queen, king, jack]) ->
        Val is 10).
        
    
% check if a list contains valid cards
valid_cards([]).
valid_cards([Card|Other_cards]) :-
        check_card(Card),
        valid_cards(Other_cards).

% check if a card is valid
% memberchk does not backtrack, which is what i need
check_card(card(Rank, Suit)) :-
         memberchk(Suit, [clubs, diamonds, hearts, spades]),
    (    integer(Rank)
    ->   between(2, 10, Rank)
    ;    memberchk(Rank, [ace, jack, queen, king])).

% get numerical value of a list of cards in a list
% numerical_repn(+Hand, -NumericalList).
numerical_repn(Hand, NumericalList):-
    maplist(card_numerical_value, Hand, NumericalList).
    
% build distinct combinations of items within a list
% combs(+List, -List).
combs([],[]).
combs([Head|Tail],[Head|Tail2]) :-
    combs(Tail,Tail2).
combs([_|Tail],Tail2) :-
    combs(Tail,Tail2).
