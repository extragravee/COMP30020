
import itertools

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g','a', 'b', 'c', 'd', 'e', 'f', 'g','a', 'b', 'c', 'd', 'e', 'f', 'g']
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

target = ("a3", "b2", "c1")
guess = ("c3", "a2", "b1")
print(feedback(target, guess))


# Main function trying to emulate point 6
# we never used the feedback score
def guess_func():

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
	return avgs

ans = guess_func()

# print sorted list of remaining candidates and target list
print(sorted(ans))



