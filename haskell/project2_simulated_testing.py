
import itertools

list1 = map(lambda x:x.upper(), ['a', 'b', 'c', 'd', 'e', 'f', 'g','a', 'b', 'c', 'd', 'e', 'f', 'g','a', 'b', 'c', 'd', 'e', 'f', 'g'])
list2 = [1,1,1,2,2,2,3,3,3]

combinations = list(set(list(itertools.combinations(list1, 3))))
# Get all permutations of `list1` with length 2
combinations2 = list(set(list(itertools.combinations(list2, 3))))

# print(list(combinations))
# print(list(combinations2))
# print(list(itertools.product(combinations, combinations2)))

all_set = list(itertools.product(combinations, combinations2))
new_set = set()
for s in all_set:
	temp = []
	for i in range(3):
		temp.append(str(s[0][i] + str(s[1][i])))

	if len(set(temp)) == 3:
		new_set.add(tuple(sorted(temp)))

final = sorted(new_set)
# print(final)
# print(len(final), type(final[0]))

def feedback(target, guess):
	ans = [0,0,0]

	# pitches
	for g in guess:
		ans[0] += (g in target)

	t = list(target)
	g = list(guess)

	pitch_int = list(set(t) & set(g))
	for item in pitch_int:
		t.remove(item)
		g.remove(item)

	target = t
	guess = g

	# print(target, guess)
	# # notes
	notes_t = [x[0] for x in target]
	notes_g = [x[0] for x in guess]

	# print(notes_t, notes_g)

	count_t = {}
	for note in notes_t:
		if note in count_t:
			count_t[note] +=1
		else:
			count_t[note] = 1

	count_g = {}
	for note in notes_g:
		if note in count_g:
			count_g[note] +=1
		else:
			count_g[note] = 1


	sum1 = 0
	for key in count_g:
		if key in count_t:
			sum1 += min(count_g[key], count_t[key])

	ans[1] = sum1

	# these are octaves
	notes_t = [x[1] for x in target]
	notes_g = [x[1] for x in guess]
	
	count_t = {}
	for note in notes_t:
		if note in count_t:
			count_t[note] +=1
		else:
			count_t[note] = 1

	count_g = {}
	for note in notes_g:
		if note in count_g:
			count_g[note] +=1
		else:
			count_g[note] = 1

	sum1 = 0
	for key in count_g:
		if key in count_t:
			sum1 += min(count_g[key], count_t[key])

	ans[2] = sum1

	return ans

# target = ("a3", "b2", "c1")
# guess = ("c3", "a2", "b1")
# print(feedback(target, guess))


# Main function trying to emulate point 6
# we never used the feedback score
def guess_func(final):

	feedbacks = []
	avgs = []

	# for each distinct possible combination of chords
	for s in final:

		distinct_fb = {}

		# check every possible combination of chords
		# record its feedback assuming that original picked
		# s chord is the target
		for t in final:

			fb = tuple(feedback(s,t))

			# count number of t guess chords that have the
			# same feedback scores
			if fb not in distinct_fb:
				distinct_fb[fb] = 1
			else:
				distinct_fb[fb] +=1
			feedbacks.append([s,t,fb])
			if fb==(3,0,0):
				print("match")

		# calculate average number of remaining chord candidates
		# given the computation on grok
		# sum of (count^2 / total) for each target s chord

		avg = 0
		denom = sum(list(distinct_fb.values()))
		for key in distinct_fb:
			avg += ((distinct_fb[key]**2)/denom)

		avgs.append([avg,s])

		# if counter >= 100:
		# 	break

	# return list of average remaining candidates and corresponding
	# simulated target
	return sorted(avgs)

# best = guess_funcss_func(final)
# # print(best)
# best = best[0][-1]
# print("Best guess is: " + str(best))

TARGET = ("A3", "E1", "G2")
GUESS = ("D3", "F1", "G3")
# GUESS = best

def guess_func2(final):

	fb = feedback(TARGET, GUESS)
	guess = GUESS

	counter = 0
	candidates = []
	while len(candidates)!= 1:
		candidates = []
		for potential in final:
			if feedback(potential, guess) == fb:
				candidates.append(potential)

		guess = guess_func(candidates)
		guess = guess[0][-1]
		
		fb = feedback(TARGET, guess)
		final = candidates
		counter+=1

	return candidates,counter

print(guess_func2(final))

# print sorted list of remaining candidates and target list
# print(sorted(ans))
# print(final)

# print("[[A1,A2,A3],[A1,A2,B1],[A1,A2,B2],[A1,A2,B3],[A1,A2,C1],[A1,A2,C2],[A1,A2,C3],[A1,A2,D1],[A1,A2,D2],[A1,A2,D3],[A1,A2,E1],[A1,A2,E2],[A1,A2,E3],[A1,A2,F1],[A1,A2,F2],[A1,A2,F3],[A1,A2,G1],[A1,A2,G2],[A1,A2,G3],[A1,A3,B1],[A1,A3,B2],[A1,A3,B3],[A1,A3,C1],[A1,A3,C2],[A1,A3,C3],[A1,A3,D1],[A1,A3,D2],[A1,A3,D3],[A1,A3,E1],[A1,A3,E2],[A1,A3,E3],[A1,A3,F1],[A1,A3,F2],[A1,A3,F3],[A1,A3,G1],[A1,A3,G2],[A1,A3,G3],[A1,B1,B2],[A1,B1,B3],[A1,B1,C1],[A1,B1,C2],[A1,B1,C3],[A1,B1,D1],[A1,B1,D2],[A1,B1,D3],[A1,B1,E1],[A1,B1,E2],[A1,B1,E3],[A1,B1,F1],[A1,B1,F2],[A1,B1,F3],[A1,B1,G1],[A1,B1,G2],[A1,B1,G3],[A1,B2,B3],[A1,B2,C1],[A1,B2,C2],[A1,B2,C3],[A1,B2,D1],[A1,B2,D2],[A1,B2,D3],[A1,B2,E1],[A1,B2,E2],[A1,B2,E3],[A1,B2,F1],[A1,B2,F2],[A1,B2,F3],[A1,B2,G1],[A1,B2,G2],[A1,B2,G3],[A1,B3,C1],[A1,B3,C2],[A1,B3,C3],[A1,B3,D1],[A1,B3,D2],[A1,B3,D3],[A1,B3,E1],[A1,B3,E2],[A1,B3,E3],[A1,B3,F1],[A1,B3,F2],[A1,B3,F3],[A1,B3,G1],[A1,B3,G2],[A1,B3,G3],[A1,C1,C2],[A1,C1,C3],[A1,C1,D1],[A1,C1,D2],[A1,C1,D3],[A1,C1,E1],[A1,C1,E2],[A1,C1,E3],[A1,C1,F1],[A1,C1,F2],[A1,C1,F3],[A1,C1,G1],[A1,C1,G2],[A1,C1,G3],[A1,C2,C3],[A1,C2,D1],[A1,C2,D2],[A1,C2,D3],[A1,C2,E1],[A1,C2,E2],[A1,C2,E3],[A1,C2,F1],[A1,C2,F2],[A1,C2,F3],[A1,C2,G1],[A1,C2,G2],[A1,C2,G3],[A1,C3,D1],[A1,C3,D2],[A1,C3,D3],[A1,C3,E1],[A1,C3,E2],[A1,C3,E3],[A1,C3,F1],[A1,C3,F2],[A1,C3,F3],[A1,C3,G1],[A1,C3,G2],[A1,C3,G3],[A1,D1,D2],[A1,D1,D3],[A1,D1,E1],[A1,D1,E2],[A1,D1,E3],[A1,D1,F1],[A1,D1,F2],[A1,D1,F3],[A1,D1,G1],[A1,D1,G2],[A1,D1,G3],[A1,D2,D3],[A1,D2,E1],[A1,D2,E2],[A1,D2,E3],[A1,D2,F1],[A1,D2,F2],[A1,D2,F3],[A1,D2,G1],[A1,D2,G2],[A1,D2,G3],[A1,D3,E1],[A1,D3,E2],[A1,D3,E3],[A1,D3,F1],[A1,D3,F2],[A1,D3,F3],[A1,D3,G1],[A1,D3,G2],[A1,D3,G3],[A1,E1,E2],[A1,E1,E3],[A1,E1,F1],[A1,E1,F2],[A1,E1,F3],[A1,E1,G1],[A1,E1,G2],[A1,E1,G3],[A1,E2,E3],[A1,E2,F1],[A1,E2,F2],[A1,E2,F3],[A1,E2,G1],[A1,E2,G2],[A1,E2,G3],[A1,E3,F1],[A1,E3,F2],[A1,E3,F3],[A1,E3,G1],[A1,E3,G2],[A1,E3,G3],[A1,F1,F2],[A1,F1,F3],[A1,F1,G1],[A1,F1,G2],[A1,F1,G3],[A1,F2,F3],[A1,F2,G1],[A1,F2,G2],[A1,F2,G3],[A1,F3,G1],[A1,F3,G2],[A1,F3,G3],[A1,G1,G2],[A1,G1,G3],[A1,G2,G3],[A2,A3,B1],[A2,A3,B2],[A2,A3,B3],[A2,A3,C1],[A2,A3,C2],[A2,A3,C3],[A2,A3,D1],[A2,A3,D2],[A2,A3,D3],[A2,A3,E1],[A2,A3,E2],[A2,A3,E3],[A2,A3,F1],[A2,A3,F2],[A2,A3,F3],[A2,A3,G1],[A2,A3,G2],[A2,A3,G3],[A2,B1,B2],[A2,B1,B3],[A2,B1,C1],[A2,B1,C2],[A2,B1,C3],[A2,B1,D1],[A2,B1,D2],[A2,B1,D3],[A2,B1,E1],[A2,B1,E2],[A2,B1,E3],[A2,B1,F1],[A2,B1,F2],[A2,B1,F3],[A2,B1,G1],[A2,B1,G2],[A2,B1,G3],[A2,B2,B3],[A2,B2,C1],[A2,B2,C2],[A2,B2,C3],[A2,B2,D1],[A2,B2,D2],[A2,B2,D3],[A2,B2,E1],[A2,B2,E2],[A2,B2,E3],[A2,B2,F1],[A2,B2,F2],[A2,B2,F3],[A2,B2,G1],[A2,B2,G2],[A2,B2,G3],[A2,B3,C1],[A2,B3,C2],[A2,B3,C3],[A2,B3,D1],[A2,B3,D2],[A2,B3,D3],[A2,B3,E1],[A2,B3,E2],[A2,B3,E3],[A2,B3,F1],[A2,B3,F2],[A2,B3,F3],[A2,B3,G1],[A2,B3,G2],[A2,B3,G3],[A2,C1,C2],[A2,C1,C3],[A2,C1,D1],[A2,C1,D2],[A2,C1,D3],[A2,C1,E1],[A2,C1,E2],[A2,C1,E3],[A2,C1,F1],[A2,C1,F2],[A2,C1,F3],[A2,C1,G1],[A2,C1,G2],[A2,C1,G3],[A2,C2,C3],[A2,C2,D1],[A2,C2,D2],[A2,C2,D3],[A2,C2,E1],[A2,C2,E2],[A2,C2,E3],[A2,C2,F1],[A2,C2,F2],[A2,C2,F3],[A2,C2,G1],[A2,C2,G2],[A2,C2,G3],[A2,C3,D1],[A2,C3,D2],[A2,C3,D3],[A2,C3,E1],[A2,C3,E2],[A2,C3,E3],[A2,C3,F1],[A2,C3,F2],[A2,C3,F3],[A2,C3,G1],[A2,C3,G2],[A2,C3,G3],[A2,D1,D2],[A2,D1,D3],[A2,D1,E1],[A2,D1,E2],[A2,D1,E3],[A2,D1,F1],[A2,D1,F2],[A2,D1,F3],[A2,D1,G1],[A2,D1,G2],[A2,D1,G3],[A2,D2,D3],[A2,D2,E1],[A2,D2,E2],[A2,D2,E3],[A2,D2,F1],[A2,D2,F2],[A2,D2,F3],[A2,D2,G1],[A2,D2,G2],[A2,D2,G3],[A2,D3,E1],[A2,D3,E2],[A2,D3,E3],[A2,D3,F1],[A2,D3,F2],[A2,D3,F3],[A2,D3,G1],[A2,D3,G2],[A2,D3,G3],[A2,E1,E2],[A2,E1,E3],[A2,E1,F1],[A2,E1,F2],[A2,E1,F3],[A2,E1,G1],[A2,E1,G2],[A2,E1,G3],[A2,E2,E3],[A2,E2,F1],[A2,E2,F2],[A2,E2,F3],[A2,E2,G1],[A2,E2,G2],[A2,E2,G3],[A2,E3,F1],[A2,E3,F2],[A2,E3,F3],[A2,E3,G1],[A2,E3,G2],[A2,E3,G3],[A2,F1,F2],[A2,F1,F3],[A2,F1,G1],[A2,F1,G2],[A2,F1,G3],[A2,F2,F3],[A2,F2,G1],[A2,F2,G2],[A2,F2,G3],[A2,F3,G1],[A2,F3,G2],[A2,F3,G3],[A2,G1,G2],[A2,G1,G3],[A2,G2,G3],[A3,B1,B2],[A3,B1,B3],[A3,B1,C1],[A3,B1,C2],[A3,B1,C3],[A3,B1,D1],[A3,B1,D2],[A3,B1,D3],[A3,B1,E1],[A3,B1,E2],[A3,B1,E3],[A3,B1,F1],[A3,B1,F2],[A3,B1,F3],[A3,B1,G1],[A3,B1,G2],[A3,B1,G3],[A3,B2,B3],[A3,B2,C1],[A3,B2,C2],[A3,B2,C3],[A3,B2,D1],[A3,B2,D2],[A3,B2,D3],[A3,B2,E1],[A3,B2,E2],[A3,B2,E3],[A3,B2,F1],[A3,B2,F2],[A3,B2,F3],[A3,B2,G1],[A3,B2,G2],[A3,B2,G3],[A3,B3,C1],[A3,B3,C2],[A3,B3,C3],[A3,B3,D1],[A3,B3,D2],[A3,B3,D3],[A3,B3,E1],[A3,B3,E2],[A3,B3,E3],[A3,B3,F1],[A3,B3,F2],[A3,B3,F3],[A3,B3,G1],[A3,B3,G2],[A3,B3,G3],[A3,C1,C2],[A3,C1,C3],[A3,C1,D1],[A3,C1,D2],[A3,C1,D3],[A3,C1,E1],[A3,C1,E2],[A3,C1,E3],[A3,C1,F1],[A3,C1,F2],[A3,C1,F3],[A3,C1,G1],[A3,C1,G2],[A3,C1,G3],[A3,C2,C3],[A3,C2,D1],[A3,C2,D2],[A3,C2,D3],[A3,C2,E1],[A3,C2,E2],[A3,C2,E3],[A3,C2,F1],[A3,C2,F2],[A3,C2,F3],[A3,C2,G1],[A3,C2,G2],[A3,C2,G3],[A3,C3,D1],[A3,C3,D2],[A3,C3,D3],[A3,C3,E1],[A3,C3,E2],[A3,C3,E3],[A3,C3,F1],[A3,C3,F2],[A3,C3,F3],[A3,C3,G1],[A3,C3,G2],[A3,C3,G3],[A3,D1,D2],[A3,D1,D3],[A3,D1,E1],[A3,D1,E2],[A3,D1,E3],[A3,D1,F1],[A3,D1,F2],[A3,D1,F3],[A3,D1,G1],[A3,D1,G2],[A3,D1,G3],[A3,D2,D3],[A3,D2,E1],[A3,D2,E2],[A3,D2,E3],[A3,D2,F1],[A3,D2,F2],[A3,D2,F3],[A3,D2,G1],[A3,D2,G2],[A3,D2,G3],[A3,D3,E1],[A3,D3,E2],[A3,D3,E3],[A3,D3,F1],[A3,D3,F2],[A3,D3,F3],[A3,D3,G1],[A3,D3,G2],[A3,D3,G3],[A3,E1,E2],[A3,E1,E3],[A3,E1,F1],[A3,E1,F2],[A3,E1,F3],[A3,E1,G1],[A3,E1,G2],[A3,E1,G3],[A3,E2,E3],[A3,E2,F1],[A3,E2,F2],[A3,E2,F3],[A3,E2,G1],[A3,E2,G2],[A3,E2,G3],[A3,E3,F1],[A3,E3,F2],[A3,E3,F3],[A3,E3,G1],[A3,E3,G2],[A3,E3,G3],[A3,F1,F2],[A3,F1,F3],[A3,F1,G1],[A3,F1,G2],[A3,F1,G3],[A3,F2,F3],[A3,F2,G1],[A3,F2,G2],[A3,F2,G3],[A3,F3,G1],[A3,F3,G2],[A3,F3,G3],[A3,G1,G2],[A3,G1,G3],[A3,G2,G3],[B1,B2,B3],[B1,B2,C1],[B1,B2,C2],[B1,B2,C3],[B1,B2,D1],[B1,B2,D2],[B1,B2,D3],[B1,B2,E1],[B1,B2,E2],[B1,B2,E3],[B1,B2,F1],[B1,B2,F2],[B1,B2,F3],[B1,B2,G1],[B1,B2,G2],[B1,B2,G3],[B1,B3,C1],[B1,B3,C2],[B1,B3,C3],[B1,B3,D1],[B1,B3,D2],[B1,B3,D3],[B1,B3,E1],[B1,B3,E2],[B1,B3,E3],[B1,B3,F1],[B1,B3,F2],[B1,B3,F3],[B1,B3,G1],[B1,B3,G2],[B1,B3,G3],[B1,C1,C2],[B1,C1,C3],[B1,C1,D1],[B1,C1,D2],[B1,C1,D3],[B1,C1,E1],[B1,C1,E2],[B1,C1,E3],[B1,C1,F1],[B1,C1,F2],[B1,C1,F3],[B1,C1,G1],[B1,C1,G2],[B1,C1,G3],[B1,C2,C3],[B1,C2,D1],[B1,C2,D2],[B1,C2,D3],[B1,C2,E1],[B1,C2,E2],[B1,C2,E3],[B1,C2,F1],[B1,C2,F2],[B1,C2,F3],[B1,C2,G1],[B1,C2,G2],[B1,C2,G3],[B1,C3,D1],[B1,C3,D2],[B1,C3,D3],[B1,C3,E1],[B1,C3,E2],[B1,C3,E3],[B1,C3,F1],[B1,C3,F2],[B1,C3,F3],[B1,C3,G1],[B1,C3,G2],[B1,C3,G3],[B1,D1,D2],[B1,D1,D3],[B1,D1,E1],[B1,D1,E2],[B1,D1,E3],[B1,D1,F1],[B1,D1,F2],[B1,D1,F3],[B1,D1,G1],[B1,D1,G2],[B1,D1,G3],[B1,D2,D3],[B1,D2,E1],[B1,D2,E2],[B1,D2,E3],[B1,D2,F1],[B1,D2,F2],[B1,D2,F3],[B1,D2,G1],[B1,D2,G2],[B1,D2,G3],[B1,D3,E1],[B1,D3,E2],[B1,D3,E3],[B1,D3,F1],[B1,D3,F2],[B1,D3,F3],[B1,D3,G1],[B1,D3,G2],[B1,D3,G3],[B1,E1,E2],[B1,E1,E3],[B1,E1,F1],[B1,E1,F2],[B1,E1,F3],[B1,E1,G1],[B1,E1,G2],[B1,E1,G3],[B1,E2,E3],[B1,E2,F1],[B1,E2,F2],[B1,E2,F3],[B1,E2,G1],[B1,E2,G2],[B1,E2,G3],[B1,E3,F1],[B1,E3,F2],[B1,E3,F3],[B1,E3,G1],[B1,E3,G2],[B1,E3,G3],[B1,F1,F2],[B1,F1,F3],[B1,F1,G1],[B1,F1,G2],[B1,F1,G3],[B1,F2,F3],[B1,F2,G1],[B1,F2,G2],[B1,F2,G3],[B1,F3,G1],[B1,F3,G2],[B1,F3,G3],[B1,G1,G2],[B1,G1,G3],[B1,G2,G3],[B2,B3,C1],[B2,B3,C2],[B2,B3,C3],[B2,B3,D1],[B2,B3,D2],[B2,B3,D3],[B2,B3,E1],[B2,B3,E2],[B2,B3,E3],[B2,B3,F1],[B2,B3,F2],[B2,B3,F3],[B2,B3,G1],[B2,B3,G2],[B2,B3,G3],[B2,C1,C2],[B2,C1,C3],[B2,C1,D1],[B2,C1,D2],[B2,C1,D3],[B2,C1,E1],[B2,C1,E2],[B2,C1,E3],[B2,C1,F1],[B2,C1,F2],[B2,C1,F3],[B2,C1,G1],[B2,C1,G2],[B2,C1,G3],[B2,C2,C3],[B2,C2,D1],[B2,C2,D2],[B2,C2,D3],[B2,C2,E1],[B2,C2,E2],[B2,C2,E3],[B2,C2,F1],[B2,C2,F2],[B2,C2,F3],[B2,C2,G1],[B2,C2,G2],[B2,C2,G3],[B2,C3,D1],[B2,C3,D2],[B2,C3,D3],[B2,C3,E1],[B2,C3,E2],[B2,C3,E3],[B2,C3,F1],[B2,C3,F2],[B2,C3,F3],[B2,C3,G1],[B2,C3,G2],[B2,C3,G3],[B2,D1,D2],[B2,D1,D3],[B2,D1,E1],[B2,D1,E2],[B2,D1,E3],[B2,D1,F1],[B2,D1,F2],[B2,D1,F3],[B2,D1,G1],[B2,D1,G2],[B2,D1,G3],[B2,D2,D3],[B2,D2,E1],[B2,D2,E2],[B2,D2,E3],[B2,D2,F1],[B2,D2,F2],[B2,D2,F3],[B2,D2,G1],[B2,D2,G2],[B2,D2,G3],[B2,D3,E1],[B2,D3,E2],[B2,D3,E3],[B2,D3,F1],[B2,D3,F2],[B2,D3,F3],[B2,D3,G1],[B2,D3,G2],[B2,D3,G3],[B2,E1,E2],[B2,E1,E3],[B2,E1,F1],[B2,E1,F2],[B2,E1,F3],[B2,E1,G1],[B2,E1,G2],[B2,E1,G3],[B2,E2,E3],[B2,E2,F1],[B2,E2,F2],[B2,E2,F3],[B2,E2,G1],[B2,E2,G2],[B2,E2,G3],[B2,E3,F1],[B2,E3,F2],[B2,E3,F3],[B2,E3,G1],[B2,E3,G2],[B2,E3,G3],[B2,F1,F2],[B2,F1,F3],[B2,F1,G1],[B2,F1,G2],[B2,F1,G3],[B2,F2,F3],[B2,F2,G1],[B2,F2,G2],[B2,F2,G3],[B2,F3,G1],[B2,F3,G2],[B2,F3,G3],[B2,G1,G2],[B2,G1,G3],[B2,G2,G3],[B3,C1,C2],[B3,C1,C3],[B3,C1,D1],[B3,C1,D2],[B3,C1,D3],[B3,C1,E1],[B3,C1,E2],[B3,C1,E3],[B3,C1,F1],[B3,C1,F2],[B3,C1,F3],[B3,C1,G1],[B3,C1,G2],[B3,C1,G3],[B3,C2,C3],[B3,C2,D1],[B3,C2,D2],[B3,C2,D3],[B3,C2,E1],[B3,C2,E2],[B3,C2,E3],[B3,C2,F1],[B3,C2,F2],[B3,C2,F3],[B3,C2,G1],[B3,C2,G2],[B3,C2,G3],[B3,C3,D1],[B3,C3,D2],[B3,C3,D3],[B3,C3,E1],[B3,C3,E2],[B3,C3,E3],[B3,C3,F1],[B3,C3,F2],[B3,C3,F3],[B3,C3,G1],[B3,C3,G2],[B3,C3,G3],[B3,D1,D2],[B3,D1,D3],[B3,D1,E1],[B3,D1,E2],[B3,D1,E3],[B3,D1,F1],[B3,D1,F2],[B3,D1,F3],[B3,D1,G1],[B3,D1,G2],[B3,D1,G3],[B3,D2,D3],[B3,D2,E1],[B3,D2,E2],[B3,D2,E3],[B3,D2,F1],[B3,D2,F2],[B3,D2,F3],[B3,D2,G1],[B3,D2,G2],[B3,D2,G3],[B3,D3,E1],[B3,D3,E2],[B3,D3,E3],[B3,D3,F1],[B3,D3,F2],[B3,D3,F3],[B3,D3,G1],[B3,D3,G2],[B3,D3,G3],[B3,E1,E2],[B3,E1,E3],[B3,E1,F1],[B3,E1,F2],[B3,E1,F3],[B3,E1,G1],[B3,E1,G2],[B3,E1,G3],[B3,E2,E3],[B3,E2,F1],[B3,E2,F2],[B3,E2,F3],[B3,E2,G1],[B3,E2,G2],[B3,E2,G3],[B3,E3,F1],[B3,E3,F2],[B3,E3,F3],[B3,E3,G1],[B3,E3,G2],[B3,E3,G3],[B3,F1,F2],[B3,F1,F3],[B3,F1,G1],[B3,F1,G2],[B3,F1,G3],[B3,F2,F3],[B3,F2,G1],[B3,F2,G2],[B3,F2,G3],[B3,F3,G1],[B3,F3,G2],[B3,F3,G3],[B3,G1,G2],[B3,G1,G3],[B3,G2,G3],[C1,C2,C3],[C1,C2,D1],[C1,C2,D2],[C1,C2,D3],[C1,C2,E1],[C1,C2,E2],[C1,C2,E3],[C1,C2,F1],[C1,C2,F2],[C1,C2,F3],[C1,C2,G1],[C1,C2,G2],[C1,C2,G3],[C1,C3,D1],[C1,C3,D2],[C1,C3,D3],[C1,C3,E1],[C1,C3,E2],[C1,C3,E3],[C1,C3,F1],[C1,C3,F2],[C1,C3,F3],[C1,C3,G1],[C1,C3,G2],[C1,C3,G3],[C1,D1,D2],[C1,D1,D3],[C1,D1,E1],[C1,D1,E2],[C1,D1,E3],[C1,D1,F1],[C1,D1,F2],[C1,D1,F3],[C1,D1,G1],[C1,D1,G2],[C1,D1,G3],[C1,D2,D3],[C1,D2,E1],[C1,D2,E2],[C1,D2,E3],[C1,D2,F1],[C1,D2,F2],[C1,D2,F3],[C1,D2,G1],[C1,D2,G2],[C1,D2,G3],[C1,D3,E1],[C1,D3,E2],[C1,D3,E3],[C1,D3,F1],[C1,D3,F2],[C1,D3,F3],[C1,D3,G1],[C1,D3,G2],[C1,D3,G3],[C1,E1,E2],[C1,E1,E3],[C1,E1,F1],[C1,E1,F2],[C1,E1,F3],[C1,E1,G1],[C1,E1,G2],[C1,E1,G3],[C1,E2,E3],[C1,E2,F1],[C1,E2,F2],[C1,E2,F3],[C1,E2,G1],[C1,E2,G2],[C1,E2,G3],[C1,E3,F1],[C1,E3,F2],[C1,E3,F3],[C1,E3,G1],[C1,E3,G2],[C1,E3,G3],[C1,F1,F2],[C1,F1,F3],[C1,F1,G1],[C1,F1,G2],[C1,F1,G3],[C1,F2,F3],[C1,F2,G1],[C1,F2,G2],[C1,F2,G3],[C1,F3,G1],[C1,F3,G2],[C1,F3,G3],[C1,G1,G2],[C1,G1,G3],[C1,G2,G3],[C2,C3,D1],[C2,C3,D2],[C2,C3,D3],[C2,C3,E1],[C2,C3,E2],[C2,C3,E3],[C2,C3,F1],[C2,C3,F2],[C2,C3,F3],[C2,C3,G1],[C2,C3,G2],[C2,C3,G3],[C2,D1,D2],[C2,D1,D3],[C2,D1,E1],[C2,D1,E2],[C2,D1,E3],[C2,D1,F1],[C2,D1,F2],[C2,D1,F3],[C2,D1,G1],[C2,D1,G2],[C2,D1,G3],[C2,D2,D3],[C2,D2,E1],[C2,D2,E2],[C2,D2,E3],[C2,D2,F1],[C2,D2,F2],[C2,D2,F3],[C2,D2,G1],[C2,D2,G2],[C2,D2,G3],[C2,D3,E1],[C2,D3,E2],[C2,D3,E3],[C2,D3,F1],[C2,D3,F2],[C2,D3,F3],[C2,D3,G1],[C2,D3,G2],[C2,D3,G3],[C2,E1,E2],[C2,E1,E3],[C2,E1,F1],[C2,E1,F2],[C2,E1,F3],[C2,E1,G1],[C2,E1,G2],[C2,E1,G3],[C2,E2,E3],[C2,E2,F1],[C2,E2,F2],[C2,E2,F3],[C2,E2,G1],[C2,E2,G2],[C2,E2,G3],[C2,E3,F1],[C2,E3,F2],[C2,E3,F3],[C2,E3,G1],[C2,E3,G2],[C2,E3,G3],[C2,F1,F2],[C2,F1,F3],[C2,F1,G1],[C2,F1,G2],[C2,F1,G3],[C2,F2,F3],[C2,F2,G1],[C2,F2,G2],[C2,F2,G3],[C2,F3,G1],[C2,F3,G2],[C2,F3,G3],[C2,G1,G2],[C2,G1,G3],[C2,G2,G3],[C3,D1,D2],[C3,D1,D3],[C3,D1,E1],[C3,D1,E2],[C3,D1,E3],[C3,D1,F1],[C3,D1,F2],[C3,D1,F3],[C3,D1,G1],[C3,D1,G2],[C3,D1,G3],[C3,D2,D3],[C3,D2,E1],[C3,D2,E2],[C3,D2,E3],[C3,D2,F1],[C3,D2,F2],[C3,D2,F3],[C3,D2,G1],[C3,D2,G2],[C3,D2,G3],[C3,D3,E1],[C3,D3,E2],[C3,D3,E3],[C3,D3,F1],[C3,D3,F2],[C3,D3,F3],[C3,D3,G1],[C3,D3,G2],[C3,D3,G3],[C3,E1,E2],[C3,E1,E3],[C3,E1,F1],[C3,E1,F2],[C3,E1,F3],[C3,E1,G1],[C3,E1,G2],[C3,E1,G3],[C3,E2,E3],[C3,E2,F1],[C3,E2,F2],[C3,E2,F3],[C3,E2,G1],[C3,E2,G2],[C3,E2,G3],[C3,E3,F1],[C3,E3,F2],[C3,E3,F3],[C3,E3,G1],[C3,E3,G2],[C3,E3,G3],[C3,F1,F2],[C3,F1,F3],[C3,F1,G1],[C3,F1,G2],[C3,F1,G3],[C3,F2,F3],[C3,F2,G1],[C3,F2,G2],[C3,F2,G3],[C3,F3,G1],[C3,F3,G2],[C3,F3,G3],[C3,G1,G2],[C3,G1,G3],[C3,G2,G3],[D1,D2,D3],[D1,D2,E1],[D1,D2,E2],[D1,D2,E3],[D1,D2,F1],[D1,D2,F2],[D1,D2,F3],[D1,D2,G1],[D1,D2,G2],[D1,D2,G3],[D1,D3,E1],[D1,D3,E2],[D1,D3,E3],[D1,D3,F1],[D1,D3,F2],[D1,D3,F3],[D1,D3,G1],[D1,D3,G2],[D1,D3,G3],[D1,E1,E2],[D1,E1,E3],[D1,E1,F1],[D1,E1,F2],[D1,E1,F3],[D1,E1,G1],[D1,E1,G2],[D1,E1,G3],[D1,E2,E3],[D1,E2,F1],[D1,E2,F2],[D1,E2,F3],[D1,E2,G1],[D1,E2,G2],[D1,E2,G3],[D1,E3,F1],[D1,E3,F2],[D1,E3,F3],[D1,E3,G1],[D1,E3,G2],[D1,E3,G3],[D1,F1,F2],[D1,F1,F3],[D1,F1,G1],[D1,F1,G2],[D1,F1,G3],[D1,F2,F3],[D1,F2,G1],[D1,F2,G2],[D1,F2,G3],[D1,F3,G1],[D1,F3,G2],[D1,F3,G3],[D1,G1,G2],[D1,G1,G3],[D1,G2,G3],[D2,D3,E1],[D2,D3,E2],[D2,D3,E3],[D2,D3,F1],[D2,D3,F2],[D2,D3,F3],[D2,D3,G1],[D2,D3,G2],[D2,D3,G3],[D2,E1,E2],[D2,E1,E3],[D2,E1,F1],[D2,E1,F2],[D2,E1,F3],[D2,E1,G1],[D2,E1,G2],[D2,E1,G3],[D2,E2,E3],[D2,E2,F1],[D2,E2,F2],[D2,E2,F3],[D2,E2,G1],[D2,E2,G2],[D2,E2,G3],[D2,E3,F1],[D2,E3,F2],[D2,E3,F3],[D2,E3,G1],[D2,E3,G2],[D2,E3,G3],[D2,F1,F2],[D2,F1,F3],[D2,F1,G1],[D2,F1,G2],[D2,F1,G3],[D2,F2,F3],[D2,F2,G1],[D2,F2,G2],[D2,F2,G3],[D2,F3,G1],[D2,F3,G2],[D2,F3,G3],[D2,G1,G2],[D2,G1,G3],[D2,G2,G3],[D3,E1,E2],[D3,E1,E3],[D3,E1,F1],[D3,E1,F2],[D3,E1,F3],[D3,E1,G1],[D3,E1,G2],[D3,E1,G3],[D3,E2,E3],[D3,E2,F1],[D3,E2,F2],[D3,E2,F3],[D3,E2,G1],[D3,E2,G2],[D3,E2,G3],[D3,E3,F1],[D3,E3,F2],[D3,E3,F3],[D3,E3,G1],[D3,E3,G2],[D3,E3,G3],[D3,F1,F2],[D3,F1,F3],[D3,F1,G1],[D3,F1,G2],[D3,F1,G3],[D3,F2,F3],[D3,F2,G1],[D3,F2,G2],[D3,F2,G3],[D3,F3,G1],[D3,F3,G2],[D3,F3,G3],[D3,G1,G2],[D3,G1,G3],[D3,G2,G3],[E1,E2,E3],[E1,E2,F1],[E1,E2,F2],[E1,E2,F3],[E1,E2,G1],[E1,E2,G2],[E1,E2,G3],[E1,E3,F1],[E1,E3,F2],[E1,E3,F3],[E1,E3,G1],[E1,E3,G2],[E1,E3,G3],[E1,F1,F2],[E1,F1,F3],[E1,F1,G1],[E1,F1,G2],[E1,F1,G3],[E1,F2,F3],[E1,F2,G1],[E1,F2,G2],[E1,F2,G3],[E1,F3,G1],[E1,F3,G2],[E1,F3,G3],[E1,G1,G2],[E1,G1,G3],[E1,G2,G3],[E2,E3,F1],[E2,E3,F2],[E2,E3,F3],[E2,E3,G1],[E2,E3,G2],[E2,E3,G3],[E2,F1,F2],[E2,F1,F3],[E2,F1,G1],[E2,F1,G2],[E2,F1,G3],[E2,F2,F3],[E2,F2,G1],[E2,F2,G2],[E2,F2,G3],[E2,F3,G1],[E2,F3,G2],[E2,F3,G3],[E2,G1,G2],[E2,G1,G3],[E2,G2,G3],[E3,F1,F2],[E3,F1,F3],[E3,F1,G1],[E3,F1,G2],[E3,F1,G3],[E3,F2,F3],[E3,F2,G1],[E3,F2,G2],[E3,F2,G3],[E3,F3,G1],[E3,F3,G2],[E3,F3,G3],[E3,G1,G2],[E3,G1,G3],[E3,G2,G3],[F1,F2,F3],[F1,F2,G1],[F1,F2,G2],[F1,F2,G3],[F1,F3,G1],[F1,F3,G2],[F1,F3,G3],[F1,G1,G2],[F1,G1,G3],[F1,G2,G3],[F2,F3,G1],[F2,F3,G2],[F2,F3,G3],[F2,G1,G2],[F2,G1,G3],[F2,G2,G3],[F3,G1,G2],[F3,G1,G3],[F3,G2,G3],[G1,G2,G3]]" == \
# 	"[[A1,A2,A3],[A1,A2,B1],[A1,A2,B2],[A1,A2,B3],[A1,A2,C1],[A1,A2,C2],[A1,A2,C3],[A1,A2,D1],[A1,A2,D2],[A1,A2,D3],[A1,A2,E1],[A1,A2,E2],[A1,A2,E3],[A1,A2,F1],[A1,A2,F2],[A1,A2,F3],[A1,A2,G1],[A1,A2,G2],[A1,A2,G3],[A1,A3,B1],[A1,A3,B2],[A1,A3,B3],[A1,A3,C1],[A1,A3,C2],[A1,A3,C3],[A1,A3,D1],[A1,A3,D2],[A1,A3,D3],[A1,A3,E1],[A1,A3,E2],[A1,A3,E3],[A1,A3,F1],[A1,A3,F2],[A1,A3,F3],[A1,A3,G1],[A1,A3,G2],[A1,A3,G3],[A1,B1,B2],[A1,B1,B3],[A1,B1,C1],[A1,B1,C2],[A1,B1,C3],[A1,B1,D1],[A1,B1,D2],[A1,B1,D3],[A1,B1,E1],[A1,B1,E2],[A1,B1,E3],[A1,B1,F1],[A1,B1,F2],[A1,B1,F3],[A1,B1,G1],[A1,B1,G2],[A1,B1,G3],[A1,B2,B3],[A1,B2,C1],[A1,B2,C2],[A1,B2,C3],[A1,B2,D1],[A1,B2,D2],[A1,B2,D3],[A1,B2,E1],[A1,B2,E2],[A1,B2,E3],[A1,B2,F1],[A1,B2,F2],[A1,B2,F3],[A1,B2,G1],[A1,B2,G2],[A1,B2,G3],[A1,B3,C1],[A1,B3,C2],[A1,B3,C3],[A1,B3,D1],[A1,B3,D2],[A1,B3,D3],[A1,B3,E1],[A1,B3,E2],[A1,B3,E3],[A1,B3,F1],[A1,B3,F2],[A1,B3,F3],[A1,B3,G1],[A1,B3,G2],[A1,B3,G3],[A1,C1,C2],[A1,C1,C3],[A1,C1,D1],[A1,C1,D2],[A1,C1,D3],[A1,C1,E1],[A1,C1,E2],[A1,C1,E3],[A1,C1,F1],[A1,C1,F2],[A1,C1,F3],[A1,C1,G1],[A1,C1,G2],[A1,C1,G3],[A1,C2,C3],[A1,C2,D1],[A1,C2,D2],[A1,C2,D3],[A1,C2,E1],[A1,C2,E2],[A1,C2,E3],[A1,C2,F1],[A1,C2,F2],[A1,C2,F3],[A1,C2,G1],[A1,C2,G2],[A1,C2,G3],[A1,C3,D1],[A1,C3,D2],[A1,C3,D3],[A1,C3,E1],[A1,C3,E2],[A1,C3,E3],[A1,C3,F1],[A1,C3,F2],[A1,C3,F3],[A1,C3,G1],[A1,C3,G2],[A1,C3,G3],[A1,D1,D2],[A1,D1,D3],[A1,D1,E1],[A1,D1,E2],[A1,D1,E3],[A1,D1,F1],[A1,D1,F2],[A1,D1,F3],[A1,D1,G1],[A1,D1,G2],[A1,D1,G3],[A1,D2,D3],[A1,D2,E1],[A1,D2,E2],[A1,D2,E3],[A1,D2,F1],[A1,D2,F2],[A1,D2,F3],[A1,D2,G1],[A1,D2,G2],[A1,D2,G3],[A1,D3,E1],[A1,D3,E2],[A1,D3,E3],[A1,D3,F1],[A1,D3,F2],[A1,D3,F3],[A1,D3,G1],[A1,D3,G2],[A1,D3,G3],[A1,E1,E2],[A1,E1,E3],[A1,E1,F1],[A1,E1,F2],[A1,E1,F3],[A1,E1,G1],[A1,E1,G2],[A1,E1,G3],[A1,E2,E3],[A1,E2,F1],[A1,E2,F2],[A1,E2,F3],[A1,E2,G1],[A1,E2,G2],[A1,E2,G3],[A1,E3,F1],[A1,E3,F2],[A1,E3,F3],[A1,E3,G1],[A1,E3,G2],[A1,E3,G3],[A1,F1,F2],[A1,F1,F3],[A1,F1,G1],[A1,F1,G2],[A1,F1,G3],[A1,F2,F3],[A1,F2,G1],[A1,F2,G2],[A1,F2,G3],[A1,F3,G1],[A1,F3,G2],[A1,F3,G3],[A1,G1,G2],[A1,G1,G3],[A1,G2,G3],[A2,A3,B1],[A2,A3,B2],[A2,A3,B3],[A2,A3,C1],[A2,A3,C2],[A2,A3,C3],[A2,A3,D1],[A2,A3,D2],[A2,A3,D3],[A2,A3,E1],[A2,A3,E2],[A2,A3,E3],[A2,A3,F1],[A2,A3,F2],[A2,A3,F3],[A2,A3,G1],[A2,A3,G2],[A2,A3,G3],[A2,B1,B2],[A2,B1,B3],[A2,B1,C1],[A2,B1,C2],[A2,B1,C3],[A2,B1,D1],[A2,B1,D2],[A2,B1,D3],[A2,B1,E1],[A2,B1,E2],[A2,B1,E3],[A2,B1,F1],[A2,B1,F2],[A2,B1,F3],[A2,B1,G1],[A2,B1,G2],[A2,B1,G3],[A2,B2,B3],[A2,B2,C1],[A2,B2,C2],[A2,B2,C3],[A2,B2,D1],[A2,B2,D2],[A2,B2,D3],[A2,B2,E1],[A2,B2,E2],[A2,B2,E3],[A2,B2,F1],[A2,B2,F2],[A2,B2,F3],[A2,B2,G1],[A2,B2,G2],[A2,B2,G3],[A2,B3,C1],[A2,B3,C2],[A2,B3,C3],[A2,B3,D1],[A2,B3,D2],[A2,B3,D3],[A2,B3,E1],[A2,B3,E2],[A2,B3,E3],[A2,B3,F1],[A2,B3,F2],[A2,B3,F3],[A2,B3,G1],[A2,B3,G2],[A2,B3,G3],[A2,C1,C2],[A2,C1,C3],[A2,C1,D1],[A2,C1,D2],[A2,C1,D3],[A2,C1,E1],[A2,C1,E2],[A2,C1,E3],[A2,C1,F1],[A2,C1,F2],[A2,C1,F3],[A2,C1,G1],[A2,C1,G2],[A2,C1,G3],[A2,C2,C3],[A2,C2,D1],[A2,C2,D2],[A2,C2,D3],[A2,C2,E1],[A2,C2,E2],[A2,C2,E3],[A2,C2,F1],[A2,C2,F2],[A2,C2,F3],[A2,C2,G1],[A2,C2,G2],[A2,C2,G3],[A2,C3,D1],[A2,C3,D2],[A2,C3,D3],[A2,C3,E1],[A2,C3,E2],[A2,C3,E3],[A2,C3,F1],[A2,C3,F2],[A2,C3,F3],[A2,C3,G1],[A2,C3,G2],[A2,C3,G3],[A2,D1,D2],[A2,D1,D3],[A2,D1,E1],[A2,D1,E2],[A2,D1,E3],[A2,D1,F1],[A2,D1,F2],[A2,D1,F3],[A2,D1,G1],[A2,D1,G2],[A2,D1,G3],[A2,D2,D3],[A2,D2,E1],[A2,D2,E2],[A2,D2,E3],[A2,D2,F1],[A2,D2,F2],[A2,D2,F3],[A2,D2,G1],[A2,D2,G2],[A2,D2,G3],[A2,D3,E1],[A2,D3,E2],[A2,D3,E3],[A2,D3,F1],[A2,D3,F2],[A2,D3,F3],[A2,D3,G1],[A2,D3,G2],[A2,D3,G3],[A2,E1,E2],[A2,E1,E3],[A2,E1,F1],[A2,E1,F2],[A2,E1,F3],[A2,E1,G1],[A2,E1,G2],[A2,E1,G3],[A2,E2,E3],[A2,E2,F1],[A2,E2,F2],[A2,E2,F3],[A2,E2,G1],[A2,E2,G2],[A2,E2,G3],[A2,E3,F1],[A2,E3,F2],[A2,E3,F3],[A2,E3,G1],[A2,E3,G2],[A2,E3,G3],[A2,F1,F2],[A2,F1,F3],[A2,F1,G1],[A2,F1,G2],[A2,F1,G3],[A2,F2,F3],[A2,F2,G1],[A2,F2,G2],[A2,F2,G3],[A2,F3,G1],[A2,F3,G2],[A2,F3,G3],[A2,G1,G2],[A2,G1,G3],[A2,G2,G3],[A3,B1,B2],[A3,B1,B3],[A3,B1,C1],[A3,B1,C2],[A3,B1,C3],[A3,B1,D1],[A3,B1,D2],[A3,B1,D3],[A3,B1,E1],[A3,B1,E2],[A3,B1,E3],[A3,B1,F1],[A3,B1,F2],[A3,B1,F3],[A3,B1,G1],[A3,B1,G2],[A3,B1,G3],[A3,B2,B3],[A3,B2,C1],[A3,B2,C2],[A3,B2,C3],[A3,B2,D1],[A3,B2,D2],[A3,B2,D3],[A3,B2,E1],[A3,B2,E2],[A3,B2,E3],[A3,B2,F1],[A3,B2,F2],[A3,B2,F3],[A3,B2,G1],[A3,B2,G2],[A3,B2,G3],[A3,B3,C1],[A3,B3,C2],[A3,B3,C3],[A3,B3,D1],[A3,B3,D2],[A3,B3,D3],[A3,B3,E1],[A3,B3,E2],[A3,B3,E3],[A3,B3,F1],[A3,B3,F2],[A3,B3,F3],[A3,B3,G1],[A3,B3,G2],[A3,B3,G3],[A3,C1,C2],[A3,C1,C3],[A3,C1,D1],[A3,C1,D2],[A3,C1,D3],[A3,C1,E1],[A3,C1,E2],[A3,C1,E3],[A3,C1,F1],[A3,C1,F2],[A3,C1,F3],[A3,C1,G1],[A3,C1,G2],[A3,C1,G3],[A3,C2,C3],[A3,C2,D1],[A3,C2,D2],[A3,C2,D3],[A3,C2,E1],[A3,C2,E2],[A3,C2,E3],[A3,C2,F1],[A3,C2,F2],[A3,C2,F3],[A3,C2,G1],[A3,C2,G2],[A3,C2,G3],[A3,C3,D1],[A3,C3,D2],[A3,C3,D3],[A3,C3,E1],[A3,C3,E2],[A3,C3,E3],[A3,C3,F1],[A3,C3,F2],[A3,C3,F3],[A3,C3,G1],[A3,C3,G2],[A3,C3,G3],[A3,D1,D2],[A3,D1,D3],[A3,D1,E1],[A3,D1,E2],[A3,D1,E3],[A3,D1,F1],[A3,D1,F2],[A3,D1,F3],[A3,D1,G1],[A3,D1,G2],[A3,D1,G3],[A3,D2,D3],[A3,D2,E1],[A3,D2,E2],[A3,D2,E3],[A3,D2,F1],[A3,D2,F2],[A3,D2,F3],[A3,D2,G1],[A3,D2,G2],[A3,D2,G3],[A3,D3,E1],[A3,D3,E2],[A3,D3,E3],[A3,D3,F1],[A3,D3,F2],[A3,D3,F3],[A3,D3,G1],[A3,D3,G2],[A3,D3,G3],[A3,E1,E2],[A3,E1,E3],[A3,E1,F1],[A3,E1,F2],[A3,E1,F3],[A3,E1,G1],[A3,E1,G2],[A3,E1,G3],[A3,E2,E3],[A3,E2,F1],[A3,E2,F2],[A3,E2,F3],[A3,E2,G1],[A3,E2,G2],[A3,E2,G3],[A3,E3,F1],[A3,E3,F2],[A3,E3,F3],[A3,E3,G1],[A3,E3,G2],[A3,E3,G3],[A3,F1,F2],[A3,F1,F3],[A3,F1,G1],[A3,F1,G2],[A3,F1,G3],[A3,F2,F3],[A3,F2,G1],[A3,F2,G2],[A3,F2,G3],[A3,F3,G1],[A3,F3,G2],[A3,F3,G3],[A3,G1,G2],[A3,G1,G3],[A3,G2,G3],[B1,B2,B3],[B1,B2,C1],[B1,B2,C2],[B1,B2,C3],[B1,B2,D1],[B1,B2,D2],[B1,B2,D3],[B1,B2,E1],[B1,B2,E2],[B1,B2,E3],[B1,B2,F1],[B1,B2,F2],[B1,B2,F3],[B1,B2,G1],[B1,B2,G2],[B1,B2,G3],[B1,B3,C1],[B1,B3,C2],[B1,B3,C3],[B1,B3,D1],[B1,B3,D2],[B1,B3,D3],[B1,B3,E1],[B1,B3,E2],[B1,B3,E3],[B1,B3,F1],[B1,B3,F2],[B1,B3,F3],[B1,B3,G1],[B1,B3,G2],[B1,B3,G3],[B1,C1,C2],[B1,C1,C3],[B1,C1,D1],[B1,C1,D2],[B1,C1,D3],[B1,C1,E1],[B1,C1,E2],[B1,C1,E3],[B1,C1,F1],[B1,C1,F2],[B1,C1,F3],[B1,C1,G1],[B1,C1,G2],[B1,C1,G3],[B1,C2,C3],[B1,C2,D1],[B1,C2,D2],[B1,C2,D3],[B1,C2,E1],[B1,C2,E2],[B1,C2,E3],[B1,C2,F1],[B1,C2,F2],[B1,C2,F3],[B1,C2,G1],[B1,C2,G2],[B1,C2,G3],[B1,C3,D1],[B1,C3,D2],[B1,C3,D3],[B1,C3,E1],[B1,C3,E2],[B1,C3,E3],[B1,C3,F1],[B1,C3,F2],[B1,C3,F3],[B1,C3,G1],[B1,C3,G2],[B1,C3,G3],[B1,D1,D2],[B1,D1,D3],[B1,D1,E1],[B1,D1,E2],[B1,D1,E3],[B1,D1,F1],[B1,D1,F2],[B1,D1,F3],[B1,D1,G1],[B1,D1,G2],[B1,D1,G3],[B1,D2,D3],[B1,D2,E1],[B1,D2,E2],[B1,D2,E3],[B1,D2,F1],[B1,D2,F2],[B1,D2,F3],[B1,D2,G1],[B1,D2,G2],[B1,D2,G3],[B1,D3,E1],[B1,D3,E2],[B1,D3,E3],[B1,D3,F1],[B1,D3,F2],[B1,D3,F3],[B1,D3,G1],[B1,D3,G2],[B1,D3,G3],[B1,E1,E2],[B1,E1,E3],[B1,E1,F1],[B1,E1,F2],[B1,E1,F3],[B1,E1,G1],[B1,E1,G2],[B1,E1,G3],[B1,E2,E3],[B1,E2,F1],[B1,E2,F2],[B1,E2,F3],[B1,E2,G1],[B1,E2,G2],[B1,E2,G3],[B1,E3,F1],[B1,E3,F2],[B1,E3,F3],[B1,E3,G1],[B1,E3,G2],[B1,E3,G3],[B1,F1,F2],[B1,F1,F3],[B1,F1,G1],[B1,F1,G2],[B1,F1,G3],[B1,F2,F3],[B1,F2,G1],[B1,F2,G2],[B1,F2,G3],[B1,F3,G1],[B1,F3,G2],[B1,F3,G3],[B1,G1,G2],[B1,G1,G3],[B1,G2,G3],[B2,B3,C1],[B2,B3,C2],[B2,B3,C3],[B2,B3,D1],[B2,B3,D2],[B2,B3,D3],[B2,B3,E1],[B2,B3,E2],[B2,B3,E3],[B2,B3,F1],[B2,B3,F2],[B2,B3,F3],[B2,B3,G1],[B2,B3,G2],[B2,B3,G3],[B2,C1,C2],[B2,C1,C3],[B2,C1,D1],[B2,C1,D2],[B2,C1,D3],[B2,C1,E1],[B2,C1,E2],[B2,C1,E3],[B2,C1,F1],[B2,C1,F2],[B2,C1,F3],[B2,C1,G1],[B2,C1,G2],[B2,C1,G3],[B2,C2,C3],[B2,C2,D1],[B2,C2,D2],[B2,C2,D3],[B2,C2,E1],[B2,C2,E2],[B2,C2,E3],[B2,C2,F1],[B2,C2,F2],[B2,C2,F3],[B2,C2,G1],[B2,C2,G2],[B2,C2,G3],[B2,C3,D1],[B2,C3,D2],[B2,C3,D3],[B2,C3,E1],[B2,C3,E2],[B2,C3,E3],[B2,C3,F1],[B2,C3,F2],[B2,C3,F3],[B2,C3,G1],[B2,C3,G2],[B2,C3,G3],[B2,D1,D2],[B2,D1,D3],[B2,D1,E1],[B2,D1,E2],[B2,D1,E3],[B2,D1,F1],[B2,D1,F2],[B2,D1,F3],[B2,D1,G1],[B2,D1,G2],[B2,D1,G3],[B2,D2,D3],[B2,D2,E1],[B2,D2,E2],[B2,D2,E3],[B2,D2,F1],[B2,D2,F2],[B2,D2,F3],[B2,D2,G1],[B2,D2,G2],[B2,D2,G3],[B2,D3,E1],[B2,D3,E2],[B2,D3,E3],[B2,D3,F1],[B2,D3,F2],[B2,D3,F3],[B2,D3,G1],[B2,D3,G2],[B2,D3,G3],[B2,E1,E2],[B2,E1,E3],[B2,E1,F1],[B2,E1,F2],[B2,E1,F3],[B2,E1,G1],[B2,E1,G2],[B2,E1,G3],[B2,E2,E3],[B2,E2,F1],[B2,E2,F2],[B2,E2,F3],[B2,E2,G1],[B2,E2,G2],[B2,E2,G3],[B2,E3,F1],[B2,E3,F2],[B2,E3,F3],[B2,E3,G1],[B2,E3,G2],[B2,E3,G3],[B2,F1,F2],[B2,F1,F3],[B2,F1,G1],[B2,F1,G2],[B2,F1,G3],[B2,F2,F3],[B2,F2,G1],[B2,F2,G2],[B2,F2,G3],[B2,F3,G1],[B2,F3,G2],[B2,F3,G3],[B2,G1,G2],[B2,G1,G3],[B2,G2,G3],[B3,C1,C2],[B3,C1,C3],[B3,C1,D1],[B3,C1,D2],[B3,C1,D3],[B3,C1,E1],[B3,C1,E2],[B3,C1,E3],[B3,C1,F1],[B3,C1,F2],[B3,C1,F3],[B3,C1,G1],[B3,C1,G2],[B3,C1,G3],[B3,C2,C3],[B3,C2,D1],[B3,C2,D2],[B3,C2,D3],[B3,C2,E1],[B3,C2,E2],[B3,C2,E3],[B3,C2,F1],[B3,C2,F2],[B3,C2,F3],[B3,C2,G1],[B3,C2,G2],[B3,C2,G3],[B3,C3,D1],[B3,C3,D2],[B3,C3,D3],[B3,C3,E1],[B3,C3,E2],[B3,C3,E3],[B3,C3,F1],[B3,C3,F2],[B3,C3,F3],[B3,C3,G1],[B3,C3,G2],[B3,C3,G3],[B3,D1,D2],[B3,D1,D3],[B3,D1,E1],[B3,D1,E2],[B3,D1,E3],[B3,D1,F1],[B3,D1,F2],[B3,D1,F3],[B3,D1,G1],[B3,D1,G2],[B3,D1,G3],[B3,D2,D3],[B3,D2,E1],[B3,D2,E2],[B3,D2,E3],[B3,D2,F1],[B3,D2,F2],[B3,D2,F3],[B3,D2,G1],[B3,D2,G2],[B3,D2,G3],[B3,D3,E1],[B3,D3,E2],[B3,D3,E3],[B3,D3,F1],[B3,D3,F2],[B3,D3,F3],[B3,D3,G1],[B3,D3,G2],[B3,D3,G3],[B3,E1,E2],[B3,E1,E3],[B3,E1,F1],[B3,E1,F2],[B3,E1,F3],[B3,E1,G1],[B3,E1,G2],[B3,E1,G3],[B3,E2,E3],[B3,E2,F1],[B3,E2,F2],[B3,E2,F3],[B3,E2,G1],[B3,E2,G2],[B3,E2,G3],[B3,E3,F1],[B3,E3,F2],[B3,E3,F3],[B3,E3,G1],[B3,E3,G2],[B3,E3,G3],[B3,F1,F2],[B3,F1,F3],[B3,F1,G1],[B3,F1,G2],[B3,F1,G3],[B3,F2,F3],[B3,F2,G1],[B3,F2,G2],[B3,F2,G3],[B3,F3,G1],[B3,F3,G2],[B3,F3,G3],[B3,G1,G2],[B3,G1,G3],[B3,G2,G3],[C1,C2,C3],[C1,C2,D1],[C1,C2,D2],[C1,C2,D3],[C1,C2,E1],[C1,C2,E2],[C1,C2,E3],[C1,C2,F1],[C1,C2,F2],[C1,C2,F3],[C1,C2,G1],[C1,C2,G2],[C1,C2,G3],[C1,C3,D1],[C1,C3,D2],[C1,C3,D3],[C1,C3,E1],[C1,C3,E2],[C1,C3,E3],[C1,C3,F1],[C1,C3,F2],[C1,C3,F3],[C1,C3,G1],[C1,C3,G2],[C1,C3,G3],[C1,D1,D2],[C1,D1,D3],[C1,D1,E1],[C1,D1,E2],[C1,D1,E3],[C1,D1,F1],[C1,D1,F2],[C1,D1,F3],[C1,D1,G1],[C1,D1,G2],[C1,D1,G3],[C1,D2,D3],[C1,D2,E1],[C1,D2,E2],[C1,D2,E3],[C1,D2,F1],[C1,D2,F2],[C1,D2,F3],[C1,D2,G1],[C1,D2,G2],[C1,D2,G3],[C1,D3,E1],[C1,D3,E2],[C1,D3,E3],[C1,D3,F1],[C1,D3,F2],[C1,D3,F3],[C1,D3,G1],[C1,D3,G2],[C1,D3,G3],[C1,E1,E2],[C1,E1,E3],[C1,E1,F1],[C1,E1,F2],[C1,E1,F3],[C1,E1,G1],[C1,E1,G2],[C1,E1,G3],[C1,E2,E3],[C1,E2,F1],[C1,E2,F2],[C1,E2,F3],[C1,E2,G1],[C1,E2,G2],[C1,E2,G3],[C1,E3,F1],[C1,E3,F2],[C1,E3,F3],[C1,E3,G1],[C1,E3,G2],[C1,E3,G3],[C1,F1,F2],[C1,F1,F3],[C1,F1,G1],[C1,F1,G2],[C1,F1,G3],[C1,F2,F3],[C1,F2,G1],[C1,F2,G2],[C1,F2,G3],[C1,F3,G1],[C1,F3,G2],[C1,F3,G3],[C1,G1,G2],[C1,G1,G3],[C1,G2,G3],[C2,C3,D1],[C2,C3,D2],[C2,C3,D3],[C2,C3,E1],[C2,C3,E2],[C2,C3,E3],[C2,C3,F1],[C2,C3,F2],[C2,C3,F3],[C2,C3,G1],[C2,C3,G2],[C2,C3,G3],[C2,D1,D2],[C2,D1,D3],[C2,D1,E1],[C2,D1,E2],[C2,D1,E3],[C2,D1,F1],[C2,D1,F2],[C2,D1,F3],[C2,D1,G1],[C2,D1,G2],[C2,D1,G3],[C2,D2,D3],[C2,D2,E1],[C2,D2,E2],[C2,D2,E3],[C2,D2,F1],[C2,D2,F2],[C2,D2,F3],[C2,D2,G1],[C2,D2,G2],[C2,D2,G3],[C2,D3,E1],[C2,D3,E2],[C2,D3,E3],[C2,D3,F1],[C2,D3,F2],[C2,D3,F3],[C2,D3,G1],[C2,D3,G2],[C2,D3,G3],[C2,E1,E2],[C2,E1,E3],[C2,E1,F1],[C2,E1,F2],[C2,E1,F3],[C2,E1,G1],[C2,E1,G2],[C2,E1,G3],[C2,E2,E3],[C2,E2,F1],[C2,E2,F2],[C2,E2,F3],[C2,E2,G1],[C2,E2,G2],[C2,E2,G3],[C2,E3,F1],[C2,E3,F2],[C2,E3,F3],[C2,E3,G1],[C2,E3,G2],[C2,E3,G3],[C2,F1,F2],[C2,F1,F3],[C2,F1,G1],[C2,F1,G2],[C2,F1,G3],[C2,F2,F3],[C2,F2,G1],[C2,F2,G2],[C2,F2,G3],[C2,F3,G1],[C2,F3,G2],[C2,F3,G3],[C2,G1,G2],[C2,G1,G3],[C2,G2,G3],[C3,D1,D2],[C3,D1,D3],[C3,D1,E1],[C3,D1,E2],[C3,D1,E3],[C3,D1,F1],[C3,D1,F2],[C3,D1,F3],[C3,D1,G1],[C3,D1,G2],[C3,D1,G3],[C3,D2,D3],[C3,D2,E1],[C3,D2,E2],[C3,D2,E3],[C3,D2,F1],[C3,D2,F2],[C3,D2,F3],[C3,D2,G1],[C3,D2,G2],[C3,D2,G3],[C3,D3,E1],[C3,D3,E2],[C3,D3,E3],[C3,D3,F1],[C3,D3,F2],[C3,D3,F3],[C3,D3,G1],[C3,D3,G2],[C3,D3,G3],[C3,E1,E2],[C3,E1,E3],[C3,E1,F1],[C3,E1,F2],[C3,E1,F3],[C3,E1,G1],[C3,E1,G2],[C3,E1,G3],[C3,E2,E3],[C3,E2,F1],[C3,E2,F2],[C3,E2,F3],[C3,E2,G1],[C3,E2,G2],[C3,E2,G3],[C3,E3,F1],[C3,E3,F2],[C3,E3,F3],[C3,E3,G1],[C3,E3,G2],[C3,E3,G3],[C3,F1,F2],[C3,F1,F3],[C3,F1,G1],[C3,F1,G2],[C3,F1,G3],[C3,F2,F3],[C3,F2,G1],[C3,F2,G2],[C3,F2,G3],[C3,F3,G1],[C3,F3,G2],[C3,F3,G3],[C3,G1,G2],[C3,G1,G3],[C3,G2,G3],[D1,D2,D3],[D1,D2,E1],[D1,D2,E2],[D1,D2,E3],[D1,D2,F1],[D1,D2,F2],[D1,D2,F3],[D1,D2,G1],[D1,D2,G2],[D1,D2,G3],[D1,D3,E1],[D1,D3,E2],[D1,D3,E3],[D1,D3,F1],[D1,D3,F2],[D1,D3,F3],[D1,D3,G1],[D1,D3,G2],[D1,D3,G3],[D1,E1,E2],[D1,E1,E3],[D1,E1,F1],[D1,E1,F2],[D1,E1,F3],[D1,E1,G1],[D1,E1,G2],[D1,E1,G3],[D1,E2,E3],[D1,E2,F1],[D1,E2,F2],[D1,E2,F3],[D1,E2,G1],[D1,E2,G2],[D1,E2,G3],[D1,E3,F1],[D1,E3,F2],[D1,E3,F3],[D1,E3,G1],[D1,E3,G2],[D1,E3,G3],[D1,F1,F2],[D1,F1,F3],[D1,F1,G1],[D1,F1,G2],[D1,F1,G3],[D1,F2,F3],[D1,F2,G1],[D1,F2,G2],[D1,F2,G3],[D1,F3,G1],[D1,F3,G2],[D1,F3,G3],[D1,G1,G2],[D1,G1,G3],[D1,G2,G3],[D2,D3,E1],[D2,D3,E2],[D2,D3,E3],[D2,D3,F1],[D2,D3,F2],[D2,D3,F3],[D2,D3,G1],[D2,D3,G2],[D2,D3,G3],[D2,E1,E2],[D2,E1,E3],[D2,E1,F1],[D2,E1,F2],[D2,E1,F3],[D2,E1,G1],[D2,E1,G2],[D2,E1,G3],[D2,E2,E3],[D2,E2,F1],[D2,E2,F2],[D2,E2,F3],[D2,E2,G1],[D2,E2,G2],[D2,E2,G3],[D2,E3,F1],[D2,E3,F2],[D2,E3,F3],[D2,E3,G1],[D2,E3,G2],[D2,E3,G3],[D2,F1,F2],[D2,F1,F3],[D2,F1,G1],[D2,F1,G2],[D2,F1,G3],[D2,F2,F3],[D2,F2,G1],[D2,F2,G2],[D2,F2,G3],[D2,F3,G1],[D2,F3,G2],[D2,F3,G3],[D2,G1,G2],[D2,G1,G3],[D2,G2,G3],[D3,E1,E2],[D3,E1,E3],[D3,E1,F1],[D3,E1,F2],[D3,E1,F3],[D3,E1,G1],[D3,E1,G2],[D3,E1,G3],[D3,E2,E3],[D3,E2,F1],[D3,E2,F2],[D3,E2,F3],[D3,E2,G1],[D3,E2,G2],[D3,E2,G3],[D3,E3,F1],[D3,E3,F2],[D3,E3,F3],[D3,E3,G1],[D3,E3,G2],[D3,E3,G3],[D3,F1,F2],[D3,F1,F3],[D3,F1,G1],[D3,F1,G2],[D3,F1,G3],[D3,F2,F3],[D3,F2,G1],[D3,F2,G2],[D3,F2,G3],[D3,F3,G1],[D3,F3,G2],[D3,F3,G3],[D3,G1,G2],[D3,G1,G3],[D3,G2,G3],[E1,E2,E3],[E1,E2,F1],[E1,E2,F2],[E1,E2,F3],[E1,E2,G1],[E1,E2,G2],[E1,E2,G3],[E1,E3,F1],[E1,E3,F2],[E1,E3,F3],[E1,E3,G1],[E1,E3,G2],[E1,E3,G3],[E1,F1,F2],[E1,F1,F3],[E1,F1,G1],[E1,F1,G2],[E1,F1,G3],[E1,F2,F3],[E1,F2,G1],[E1,F2,G2],[E1,F2,G3],[E1,F3,G1],[E1,F3,G2],[E1,F3,G3],[E1,G1,G2],[E1,G1,G3],[E1,G2,G3],[E2,E3,F1],[E2,E3,F2],[E2,E3,F3],[E2,E3,G1],[E2,E3,G2],[E2,E3,G3],[E2,F1,F2],[E2,F1,F3],[E2,F1,G1],[E2,F1,G2],[E2,F1,G3],[E2,F2,F3],[E2,F2,G1],[E2,F2,G2],[E2,F2,G3],[E2,F3,G1],[E2,F3,G2],[E2,F3,G3],[E2,G1,G2],[E2,G1,G3],[E2,G2,G3],[E3,F1,F2],[E3,F1,F3],[E3,F1,G1],[E3,F1,G2],[E3,F1,G3],[E3,F2,F3],[E3,F2,G1],[E3,F2,G2],[E3,F2,G3],[E3,F3,G1],[E3,F3,G2],[E3,F3,G3],[E3,G1,G2],[E3,G1,G3],[E3,G2,G3],[F1,F2,F3],[F1,F2,G1],[F1,F2,G2],[F1,F2,G3],[F1,F3,G1],[F1,F3,G2],[F1,F3,G3],[F1,G1,G2],[F1,G1,G3],[F1,G2,G3],[F2,F3,G1],[F2,F3,G2],[F2,F3,G3],[F2,G1,G2],[F2,G1,G3],[F2,G2,G3],[F3,G1,G2],[F3,G1,G3],[F3,G2,G3],[G1,G2,G3]]")

