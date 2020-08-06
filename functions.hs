{-
	INFIX functions - Functions sandwiched between two things
	eg. 7 * 8, "*" is the infix function

	PREFIX ones are like:

	succ 8
	where succ is the successor function, returns arg + 1

	min, max can be used like:
		take only two args

	min 7 8
	max 9.1 1.1

	Function application (calling a function by putting a 
	space after it and then typing out the parameters) has 
	the highest precedence of them all.

		succ 7 8 + max 9 1 - 1
		same as
		(succ 7 8) + (max 9 1) - 1

	Prefix functions > infix for clarity

		div function takes two arguments, prefix may not 
		be the most clear method

			div 90 10 returns 9
			but so does 90 `div` 10  ****

	CARE:
		foo(foo 3) doesn't mean foo is being called with
			two arguments, foo and 3, instead it means that
			first foo 3 is called, then foo is called on the
			result of that!

	FIRST FUNCTION TIME BABY
	========================

-}

doubleMe x = x * 2
-- since both ints and floats are "numbers", both can 
-- work here

doubleUs x y = x*2 + y*2
-- same with here, both ints and floats will work

doubleUs2 x y = doubleMe x + doubleMe y
-- functions can be referenced in other functions

-- order of function definition doesn't really matter,
-- unlike C

doubleSmallNumber x = if x > 100
	then x 
	else x*2
-- standard conditionals

