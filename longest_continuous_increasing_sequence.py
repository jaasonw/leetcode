# Not the leetcode version but a variation i had for an interview
# Longest Continuous Increasing Sequence
'''
@description Finds the longest increasing sequence from a given array of
integers. A sequence in an array is increasing when each non-last value is
followed by a value that is greater than the previous value. If there are
multiple contenders of the same length, returns the first occurring sequence.
If no increasing sequence of length 2 or greater is found, returns an empty
array. Does not mutate the array parameter.

@param {number[]} seq An array of integers

@returns {number[]} The longest continuous increasing sequence of `seq`

@example
longestIncrSequence([1])
// returns []
@example
longestIncrSequence([3, 4, 1, 2])
// return [3, 4]
@example
longestIncrSequence([3, 0, 2, 2, 5, -43, -1, 0, 11, 9, 10])
// returns [-43, -1, 0, 11]
'''


def longestIncrSequence(seq):
    if len(seq) < 2:
        return []
    sequences = []
    currentSequence = []
    for index, element in enumerate(seq):
        if index == 0 or seq[index - 1] < element:
            currentSequence.append(element)
        else:
            sequences.append((len(currentSequence), currentSequence))
            currentSequence = [element]

    sequences.append((len(currentSequence), currentSequence))

    return max(sequences, key=lambda x : x[0])[1]
    # max()
    # return sequences

# print(longestIncrSequence([3, 0, 2, 2, 5, -43, -1, 0, 11, 9, 10]))
# print(longestIncrSequence([3, 4, 1, 2]))
# print(longestIncrSequence([1]))
# print(longestIncrSequence([3, 0, 2, 2, 5, -43, -1, 0, 11]))
