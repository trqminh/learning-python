# ref: https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/udacity/5_word2vec.ipynb

import numpy as np
import collections
import random
data_index = 0
def read_words(filename):
  words = []
  with open(filename, 'r') as f:
    for line  in f:
      words.append(str(line.rstrip('\n')))

  return words


def build_dataset(words, vocab_size):
  # what I want to build:
  # dictionary: 'word' rank dictionary['word'] in the data
  # dictionary['UNK'] is the rank of less popular than a threshold (for example 50000 word)
  # data[i]: word[i] rank data[i]-th in the data set
  # reverse_dictionary[data[i]] is the same as word[i]
  count = [['UNK', -1]]
  count.extend(collections.Counter(words).most_common(vocab_size - 1))

  dictionary = {}

  for word,_ in count:
    dictionary[word] = len(dictionary)

  data = []

  index = 0
  unk_cnt = 0
  for word in words:
    if word in dictionary:
      index = dictionary[word]
    else:
      index = dictionary['UNK'] # = 0
      unk_cnt += 1

    data.append((index))


  count[0][1] = unk_cnt #count[0] is tuple ['UNK', -1]
  reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))

  return data,count,dictionary,reverse_dictionary


def generate_cbow_batch(batch_size, num_cbows, cbow_window, data):
  global data_index
  assert batch_size % num_cbows == 0
  assert num_cbows <= 2*cbow_window

  batch = np.ndarray(shape=(batch_size // num_cbows, num_cbows), dtype=np.int32)
  labels = np.ndarray(shape=(batch_size // num_cbows, 1), dtype=np.int32)

  span = 2*cbow_window+1
  buffer = collections.deque(maxlen=span)

  for _ in range(span):
    buffer.append(data[data_index])
    data_index = (data_index+1) % len(data)


  for i in range(batch_size // num_cbows):
    target = cbow_window
    target_to_avoid = [cbow_window]

    labels[i,0] = buffer[cbow_window]

    for j in range(num_cbows):
      while target in target_to_avoid:
        target = random.randint(0, span - 1)

      target_to_avoid.append(target)

      batch[i, j] = buffer[target]


    buffer.append(data[data_index])
    data_index = (data_index + 1) % len(data)


  return batch, labels


def generate_batch(batch_size, num_skips, skip_window, data):
  global data_index
  assert batch_size % num_skips == 0
  assert num_skips <= 2 * skip_window
  batch = np.ndarray(shape=(batch_size), dtype=np.int32)
  labels = np.ndarray(shape=(batch_size, 1), dtype=np.int32)
  span = 2 * skip_window + 1 # [ skip_window target skip_window ]

  buffer = collections.deque(maxlen=span) # mind blow

  for _ in range(span):
    buffer.append(data[data_index])
    data_index = (data_index + 1) % len(data)
  for i in range(batch_size // num_skips):
    target = skip_window  # target label at the center of the buffer
    targets_to_avoid = [ skip_window ]
    for j in range(num_skips):
      while target in targets_to_avoid:
        target = random.randint(0, span - 1)
      targets_to_avoid.append(target)
      batch[i * num_skips + j] = buffer[skip_window]
      labels[i * num_skips + j, 0] = buffer[target]
    buffer.append(data[data_index])
    data_index = (data_index + 1) % len(data)

  return batch, labels





def main():
  words = read_words('text.txt')
  vocab_size = 25

  data, count, dictionary, reverse_dictionary = build_dataset(words,vocab_size)

  del words # because now we have reverse_dictionary and data

  print('Most common words: ', count[:5])
  print('Words data (first five words): ', [reverse_dictionary[data_i] for data_i in data[:5]])
  print('Rank of the word shit: ', dictionary['shit'])

  print('data:', [reverse_dictionary[di] for di in data[:8]])

  # for num_skips, skip_window in [(2, 1)]:
  #   data_index = 0
  #   batch, labels = generate_batch(batch_size=8, num_skips=num_skips, skip_window=skip_window, data= data)
  #   print('\nwith num_skips = %d and skip_window = %d:' % (num_skips, skip_window))
  #   print('    batch:', [reverse_dictionary[bi] for bi in batch])
  #   print('    labels:', [reverse_dictionary[li] for li in labels.reshape(8)])


  for num_cbows, cbow_window in [(2,1)]:
    data_index = 0
    batch, labels = generate_cbow_batch(batch_size=8,num_cbows=num_cbows, cbow_window=cbow_window, data = data)
    print('\nwith num_cbow = %d and cbow_window = %d: ' %(num_cbows, cbow_window))
    print('    batch:', [[reverse_dictionary[bij] for bij in bi] for bi in batch])
	
    print('    labels:', [[reverse_dictionary[lij] for lij in li] for li in labels])


if __name__ == '__main__':
    main()