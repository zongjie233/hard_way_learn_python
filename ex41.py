import random
from  urllib.request import urlopen
import sys

WORD_URL = "http://baidu.com"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** - %%%()":
        "Set *** to an instance of class %%%.",
    "***.*** = '***'":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."

}

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True

else:
    PHRASES_FIRST = False

#load up the words from the website
#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
# 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
#返回移除字符串头尾指定的字符生成的新字符串。
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

# snippet:片段 phrase:短语
#random.sample() 从字符串，列表，元组，或者集合中随机选择指定长度的元素返回。
def convert(snippet, phrase):
    #先运行for循环，之后调用capitalize()方法
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))

    results = []
    param_names = []


    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
#random.sample()返回list, join()返回str
        param_names.append(', '.join(
            random.sample(WORDS, param_count)

        ))

    for sentence in snippet, phrase:
        result = sentence[:]

        #fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #fake other names
        for word in other_names:
            result = result.replace("***",word, 1)

        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return  results

#keep going until the hit CTRL_D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                #对两个值进行交换操作
                question, answer = answer, question

            print(question)


            input(">")
            print(f"ANSWER:{answer}\n\n")
except EOFError:
    print("\nBye")












