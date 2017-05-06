# ------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedure, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be --- 
'''

data_list = sample_memo.strip().split()

words_to_guess = ["ahead", "could"]


def sampletextCleanup(sample_text):
    sampletext_list = sample_text.split()

    dict_key = []

    previous_word = ''

    for word in sampletext_list:
        cleaned_word = ''.join(st for st in word if st not in ',:/\n.!?')

        if cleaned_word.lower() != previous_word:
            dict_key.append(cleaned_word)
            previous_word = cleaned_word.lower()
        else:
            previous_word = cleaned_word.lower()

    return dict_key


def NextWordProbability(sampletext, word, previous_word=''):

    sampletext_dict = {}

    for key, value in enumerate(sampletext):
        #print "Key: %s " % key
        #print "Word: ---------------------------- %s " % word
        if word.lower() == value.lower():
            print "Value: %s " % value
            print "Sample Text: -------------------------------- %s " % sampletext[key - 1].lower()
            print "Previous Word: ---------------------------------------------- %s " % previous_word.lower()
            #if previous_word.lower() == sampletext[key - 1].lower():
            dict_key = sampletext[key + 1]
            #    print "Dict Key --------------------------------------------------------------- %s " % dict_key
            if dict_key in sampletext_dict:
                sampletext_dict[dict_key] += 1
            else:
                sampletext_dict[dict_key] = 1

    return sampletext_dict


def LaterWords(sample, word, distance):

    '''
    @param sample: a sample of text to draw from
    @param word: a word occurring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''

    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.

    sample_text = sampletextCleanup(sample)

    nwp = NextWordProbability(sample_text, word)
    nwp = [NextWordProbability(sample_text, value, word) for value in nwp]

    count = 2
    while count < distance:
        nwp = [NextWordProbability(sample, v) for value in nwp for v in value]
        count += 1

    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.

    st_prob = 0
    most_likely_word = ''

    #for k, v in nwp[0].iteritems():
    #    if v > st_prob:
    #        st_prob = v
    #        most_likely_word = k

    return most_likely_word

print LaterWords(sample_memo, "oh", 2)

