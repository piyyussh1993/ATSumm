"""Example of Converting TextSum model data.
Usage:
python textsum_data_convert.py --command text_to_binary --in_directories dailymail/stories --out_files dailymail-train.bin,dailymail-validation.bin,dailymail-test.bin --split 0.8,0.15,0.05
python textsum_data_convert.py --command text_to_vocabulary --in_directories cnn/stories,dailymail/stories --out_files vocab
"""
import re
import emoji

def give_emoji_free_text(text):
    emoji_list = [c for c in text if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])
    return clean_text

def Preprocessing(text):
    text= re.sub('http://\S+|https://\S+', '', text)            # remove url
    text= " ".join(filter(lambda x:x[0]!='@', text.split()))    # remove @twitter
    text= give_emoji_free_text(text)                            # remove emotions
    text= re.sub("[\(\[].*?[\)\]]", "", text)                   # remove (..) [..]
    text= re.sub('([".:;#*!\'?()])', r' \1', text)          # remove punctuation
    text= text.lower()                                          # lower case
    text= re.sub(",", "", text) 
    return text



import collections
import struct
import sys

from os import listdir
from os.path import isfile, join

from nltk.tokenize import sent_tokenize

import tensorflow as tf
from tensorflow.core.example import example_pb2

from numpy.random import seed as random_seed
from numpy.random import shuffle as random_shuffle

random_seed(123)  # Reproducibility

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('command', 'text_to_binary',
                           'Either text_to_vocabulary or text_to_binary.'
                           'Specify FLAGS.in_directories accordingly.')
tf.app.flags.DEFINE_string('in_directories', 'C:/Users/Piyush/Desktop/Abstrcative_summarization_datasets/tranining_files_new_new', 'path to directory')
tf.app.flags.DEFINE_string('out_files', 'C:/Users/Piyush/Desktop/Abstrcative_summarization_datasets/testing_files/vocab', 'comma separated paths to files')
tf.app.flags.DEFINE_string('split', '', 'comma separated fractions of data')


def _text_to_binary(input_directories, output_filenames, split_fractions):
    filenames = _get_filenames(input_directories)

    random_shuffle(filenames)

    start_from_index = 0
    for index, output_filename in enumerate(output_filenames):
        sample_count = int(len(filenames) * split_fractions[index])
        print(output_filename + ': ' + str(sample_count))

        end_index = min(start_from_index + sample_count, len(filenames))
        _convert_files_to_binary(filenames[start_from_index:end_index], output_filename)

        start_from_index = end_index


def _text_to_vocabulary(input_directories, vocabulary_filename, max_words=200000):
    filenames = _get_filenames(input_directories)

    counter = collections.Counter()

    for filename in filenames:
        with open(filename, 'r', encoding="utf8") as f:
            document = f.read()
        print('\t',filename)
        words = document.split()
        counter.update(words)
    
    #counter.pop('<s>')
    #counter.pop('<\s>')
    with open(vocabulary_filename, 'w', encoding="utf8") as writer:
        for word, count in counter.most_common(max_words - 2):
            writer.write(word + ' ' + str(count) + '\n')
        writer.write('<s> 0\n')
        writer.write('</s> 0\n')
        writer.write('<UNK> 0\n')
        writer.write('<PAD> 0\n')
        print(vocabulary_filename)


def _get_filenames(input_directories):
    filenames = []
    for directory_name in input_directories:
        filenames.extend([join(directory_name, f) for f in listdir(directory_name) if isfile(join(directory_name, f))])
    return filenames


def _convert_files_to_binary(input_filenames, output_filename):
    with open(output_filename, 'wb') as writer:
        for filename in input_filenames:
            with open(filename, 'r', encoding="utf8") as f:
                document = f.read()

            document_parts = document.split('\n', 3)
            document_parts[0]= Preprocessing(document_parts[0])###
            #document_parts[1]= Preprocessing(document_parts[1])###
            assert len(document_parts) == 4
            title = '<s> ' + document_parts[0] + ' </s>' #####
            #title = '<d><p><s>' + document_parts[0] + '</s></p></d>'
            document_parts[3]= document_parts[3].lstrip()
            document_parts[3]= document_parts[3].rstrip()
            body = document_parts[3].encode('utf8').decode('utf8').replace('\n', ' ').replace('\t', ' ')
            #body = document_parts[1].encode('utf8').decode('utf8').replace('\n', ' <\s> <s> ').replace('\t', ' ')
            body= Preprocessing(body)###
            #sentences = sent_tokenize(body)
            #body = ' '.join(['<s>' + sentence + '</s>' for sentence in document_parts[1]])
            #body = document_parts[1]
            body = '<s> ' + body + ' </s>' #####
            body = body.encode('utf8')
            title = title.encode('utf8')
            keyphrase=document_parts[2].encode('utf8').decode('utf8')
            keyphrase=keyphrase.encode('utf8')

            tf_example = example_pb2.Example()
            tf_example.features.feature['abstract'].bytes_list.value.extend([title])
            tf_example.features.feature['article'].bytes_list.value.extend([body])
            tf_example.features.feature['keyphrase'].bytes_list.value.extend([keyphrase])
            tf_example_str = tf_example.SerializeToString()
            str_len = len(tf_example_str)
            writer.write(struct.pack('q', str_len))
            writer.write(struct.pack('%ds' % str_len, tf_example_str))


def main(unused_argv):
    assert FLAGS.command and FLAGS.in_directories and FLAGS.out_files
    output_filenames = FLAGS.out_files.split(',')
    input_directories = FLAGS.in_directories.split(',')

    if FLAGS.command == 'text_to_binary':
        assert FLAGS.split

        split_fractions = [float(s) for s in FLAGS.split.split(',')]

        #assert len(output_filenames) == len(split_fractions)

        _text_to_binary(input_directories, output_filenames, split_fractions)

    elif FLAGS.command == 'text_to_vocabulary':
        assert len(output_filenames) == 1

        _text_to_vocabulary(input_directories, output_filenames[0])


if __name__ == '__main__':
    tf.app.run()


#python bin_vocab_creation.py --command text_to_binary --in_directories dailymail/stories --out_files dailymail-train.bin,dailymail-validation.bin,dailymail-test.bin --split 0.8,0.15,0.05
#python bin_vocab_creation.py --command text_to_vocabulary --in_directories cnn/stories,dailymail/stories --out_files vocab