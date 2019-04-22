import random

def gen_text_from_words(words):
  newwords = []
  for word in words:
    appear = random.randint(1,30)
    for i in range(appear):
      newwords.append(word)


  random.shuffle(newwords)

  with open('text.txt', 'w') as f:
    for word in newwords:
      f.write(word)
      f.write('\n')




words = ['visual', 'minh', 'the', 'word2vec', 'pycharm', 'pytorch', 'tensorflow',
        'mac', 'bow', 'skip', 'mai', 'dog', 'translate', 'fold', 'dame',
        'bitch', 'choke', 'shit', 'man', 'you', 'smile', 'are', 'operation',
         'kill', 'this', 'sad', 'bomb', 'game', 'of', 'throne']

gen_text_from_words(words)

