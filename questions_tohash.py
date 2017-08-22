#!/usr/bin/env python3

from bf import bloomfilter
import pickle
import sys

if len(sys.argv) != 4:
    print("Usage: questions_tohash.py input_file plk_file output_file")

if __name__ == '__main__':
    bf = bloomfilter()
    bf.load(sys.argv[2])
    out_f = open(sys.argv[3], 'wb')
    with open(sys.argv[1], 'r') as f:
        questions = []
        for line in f:
            if line.startswith(': '):
                continue
            words = line.strip().split()
            question = []
            for word in words:
                indices = bf.get_indices(word)
                question.append(indices)
            questions.append(question)
        pickle.dump(questions, out_f, protocol=2)
    out_f.close()