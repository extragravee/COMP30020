{- 
   HASKELL basics
   ==============
   -lazy compilation
   -think of program as transformations of data
   -referential transparency 
   		-functions have no side effects, all they do is
   		 do calculations and return some value
   		-so if a function is called with the same parameters
   		 it will return the same values
   		-this allows us to check function correctness 

   	-In IMPERATIVE
   		doubleMe() is a function
   		x = [1,2,3,4,5]

   		if we call doubleMe(doubleMe(x)), this will call
   			the inner doubleMe on the list, return a copy
   			of that list and then the outer double me is called

   	-In FUNCTIONAL

   	 	results are ONLY calculated when FORCED to show

   	 	when we call doubleMe(doubleMe(x))
   	 		the inner doubleMe doesn't do anything because we are
   	 		not forced to show that result yet!

   	 	but when we force it to show the result, the outer doubleMe
   	 		asks for the result NOW, now the inner double me takes one
   	 		element and reluctantly doubles it, and returns it to the outer
   	 		one, which again doubles it and returns it to the user, and so on...

   	 	this allows efficient handling of data, as only a single pass is performed 
   	 		on that list
	
	-type inferencing
		a = 4 + 5, don't have to tell compiler a is also a number

		this allows for general functions, as without defining the type
			if we send in any two parameters, they will be added together like
			numbers

	Compile programs with:
	-open terminal in same folder
		ghci (enter)
		:l fileName (loads functions from file)
		play around with stuff

		:r (reloads current script)

	- this will start off with Prelude> prompt
		to keep prompt consistent just use :set prompt "ghci> "

	- Use paranthesis with negative numbers
		otherwise u get a silly ass error

	Equality
		== equality
		/= not equal


   Boolean algebra is straightforward too
      True && False
      True || True
      not True && (False or False)

   
-}