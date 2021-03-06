import string

def replace(sentence, search_word, replace_word):
#take sentence, search_word, replace_word as inputs
#if search_word in sentence is equal to replace_word, replace it with replace_word

    result = []
    i = 0
    while i + len(search_word) <= len(sentence):
        #print sentence[i:i+len(search_word)]
        if sentence[i:i+len(search_word)] == search_word:
            result.append(replace_word)
            i += len(search_word)
        else:
            result.append(sentence[i])
            i += 1

    result.append(sentence[i:])

    return "".join(result)

def blank_quiz(sample, answer) :
#take sample and answer as inputs
#replace blank with answer if the prompted user_answer is equal to the answer

    i = 0
    search_word = ["[__1__]", "[__2__]","[__3__]","[__4__]"]
    while i < len(answer):
        #initialize guess_left
        guess_left = 2
        while guess_left > 0 :
            print sample
            user_answer= raw_input("Answer for blank " + str(i+1) + " : ")
            if answer[i] == user_answer :
                print "Good job! :)"
                print ''
                #replace it with the answer!
                sample = replace(sample, search_word[i], answer[i])
                i += 1
                break;
            else :
                print "wrong answer...."
                print ''
                guess_left -= 1
                print "no. of guess left " + str(guess_left)
                if guess_left == 0 :
                    print "game over! :( "
                    exit()
    print "[The Final Answer]"
    print sample
    print ''
    print "Hooray, congratulations. You won! "



print """
###################################
Welcome to the Python Challenger!
Quiz Level (0-2)
0 - easy
1 - medium
2 - hard
###################################
"""
user_input = raw_input("Choose your quiz level(0-2) : ")
if user_input != '0' and user_input != '1' and user_input != '2' :
    print "Choose a level among 0,1,2 :)"
    exit()

print "You chose level " + user_input + "."
print "You have 4 blanks and 2 guesses for each blank."

sample_0 = '''There are many programming [__1__] to learn as a web developer.
[__2__] is an interpreted [__1__] that uses datatypes like tuples, dictionaries,
and [__3__]s. [__2__]'s [__3__]s are like Javascript's arrays.
The keyword [__4__] is used to define functions/procedures in [__2__].'''

answer_0 = ["languages", "Python", "list", "def"]

sample_1 = '''Sometimes, [__1__]s in code happen - and it's not fun.
But, it's not the end of the world. One of the most important activities in a programmer's career is called [__2__].
This process involves decoding [__3__] messages and figuring out what kind of [__1__] is causing the problem.
Every program is bound to have [__1__]s. What makes a good programmer a great programmer
is being able to develop a [__4__] to systematically get rid of them.'''

answer_1 = ["bug", "debugging", "error", "strategy"]

sample_2 = '''One of the most effective ways to program is to use [__1__] thinking.
When you use [__1__] thinking, problem-solving is only a matter of [__2__]-making and [__3__].
In Python, we can use [__4__]s to help us make a [__2__]. '''

answer_2 = ["procedural", "decision", "repetition", "comparison"]


if user_input == "0" :
    blank_quiz(sample_0, answer_0)
elif user_input == "1":
    blank_quiz(sample_1, answer_1)
else :
    blank_quiz(sample_2, answer_2)
