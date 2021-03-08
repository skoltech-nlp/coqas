import csv
import pandas as pd
import pickle

from gen import generate_one_answer

import sys
import torch
from count_rouge import simple_rouge, rouge_cos1, rouge_cos2, rouge_cos3, rouge_cos_all

def main():
    df = pd.DataFrame(columns=['Object 1', 'Object 2', 'Question', 'Best Answer',  'Answers'])

    with open('yahoo_answers_positive_questions.csv', 'r') as file:
        reader = csv.reader(file)
        for ind, row in enumerate(reader):
            d = {'Object 1': row[0], 'Object 2': row[1], 'Question': row[2], 'Best Answer': row[3],  'Answers': [elem for elem in row[3:]]}
            if (ind > 0):
                df = df.append(d, ignore_index=True)

    print ("cam_noinp_answers")   
    with open('cam_no_inp_july.pkl', 'rb') as f:
        cam_answers = pickle.load(f)
    cam_scors = rouge_cos_all(cam_answers, df['Answers'].values)
    with open('camninp_rcall_.pkl', 'wb') as f:
        pickle.dump(cam_scors, f)
                

if __name__ == "__main__":
    main()