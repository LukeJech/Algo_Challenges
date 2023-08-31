# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false


def generate_hashtag(s):
    if not (s):
        return False
    # Split string into list of words without spaces
    word_list = s.split()
    # Capitalize first letter and lowercase rest of word
    for i in range(len(word_list)):
        word_list[i] = word_list[i].lower()
        word_list[i] = word_list[i].capitalize()
    # Add all words to a final string starting with a #
    hashtag = '#'
    for word in word_list:
        hashtag += word
    if (len(hashtag) > 140 or len(hashtag) < 0):
        return False
    return hashtag

print(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
print(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
# (generate_hashtag('      Codewars'), '#Codewars', 'Should handle leading whitespace.')
print(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
# (generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
print(generate_hashtag('CoDeWaRs is niCe'), '#CodewarsIsNice', 'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.')
# (generate_hashtag('c i n'), '#CIN', 'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.')
# (generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
        