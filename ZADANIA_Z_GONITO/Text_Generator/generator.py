#!/usr/bin/python3

import sys
import torch
import random

########################################################
########################################################
################# python3 generator.py #################
########################################################
########################################################

from torch import nn, optim

history_length = 32
nb_of_char_codes = 400
embedding_size = 10
history_encoded = [ord("\n")] * history_length
hidden_size = 100
criterion = nn.NLLLoss()

device = torch.device('cpu')

def char_source():
    for line in sys.stdin:
        for char in line:
            if ord(char) < nb_of_char_codes:
                yield ord(char)
 
class NGramLanguageModel(nn.Module):
    def __init__(self, nb_of_char_codes, history_length, embedding_size, hidden_size):
        super(NGramLanguageModel, self).__init__()
  
        self.embeddings = nn.Embedding(nb_of_char_codes, embedding_size).to(device)

        self.model = nn.Sequential(
            nn.Linear(history_length*embedding_size, hidden_size),
            nn.Linear(hidden_size, nb_of_char_codes),
            nn.LogSoftmax()).to(device)

    def forward(self, inputs):
        embedded_inputs = self.embeddings(inputs)
        return self.model(embedded_inputs.view(-1))

    def generate(self, to_be_continued, n):
        t = (" " * history_length + to_be_continued)[-history_length:]
        history = [ord(c) for c in t]

        with torch.no_grad():
            for _ in range(n):
                x = torch.tensor(history, dtype=torch.long)
                y = torch.exp(model(x))
                best = (sorted(range(nb_of_char_codes), key=lambda i: -y[i]))[0:10]

                yb = torch.tensor([ y[ix] if ix in best else 0.0
                                    for ix in range(nb_of_char_codes)])

                c = torch.multinomial(yb, 1)[0].item()

                t += chr(c)
                history.pop(0)
                history.append(c)

        return t
    
model = NGramLanguageModel(nb_of_char_codes,
                           history_length,
                           embedding_size,
                           hidden_size)

model.load_state_dict(torch.load('./pan_tadeusz_model'))
model.eval()

def run_generator():
    print ("Write first words: ")
    napis = input()
    if (napis == 'exit(0)'):
        exit()
    liczba = random.randint(100, 1000)
    print (model.generate(napis, liczba))
    print ("\n\nIf You would like end write exit(0)\n\n")
    run_generator()

run_generator()
