def divideAnagramWord(word):
    if len(word) <= 1:
        return word

    midSlice = len(word) // 2
    leftHalf = word[:midSlice]
    rightHalf = word[midSlice:]

    leftReturn = divideAnagramWord(leftHalf)
    rightReturn = divideAnagramWord(rightHalf)

    return mergeStrings(leftReturn, rightReturn)


def mergeStrings(left, right):
    wordArr = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            wordArr.append(left[leftIndex])
            leftIndex += 1
        else:
            wordArr.append(right[rightIndex])
            rightIndex += 1

    wordArr += left[leftIndex:]
    wordArr += right[rightIndex:]

    # newString = wordArr.join('') igual o retorno abaixo :)
    return ''.join(wordArr)


def is_anagram(first_string, second_string):
    if len(first_string) == 0 and len(second_string) == 0:
        return first_string, second_string, False

    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string = divideAnagramWord(first_string)
    second_string = divideAnagramWord(second_string)

    if first_string == second_string:
        return first_string, second_string, True
    else:
        return first_string, second_string, False
