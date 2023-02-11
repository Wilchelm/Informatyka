#!/usr/bin/env python

import torch
import random
from torch import nn
from torch import optim

lr = 0.0001

model=nn.Sequential(
        nn.Linear(2,3),
        nn.ReLU(),
        nn.Linear(3,1),
        nn.Sigmoid()
)

criterion = nn.MSELoss()
#optimizer = optim.SGD(
#        model.parameters(),
#        lr=lr,
#        momentum=0.9)
optimizer = optim.Adam(model.parameters())

def get_item():
    x1 = random.choice([0,1])
    x2 = random.choice([0,1])
    x = torch.tensor([x1,x2], dtype=torch.float)
    ye = torch.tensor(float(x1 ^ x2))
    return x, ye


minibatch_size = 1000
#alpha = torch.tensor(0.00000001)
for _ in range(100000):
    optimizer.zero_grad()
    minibatches = [get_item() for _ in range(minibatch_size)]
    print (minibatches[0])
    print (len(minibatches))
    break
    xb = torch.stack([x[0] for x in minibatches])
    yeb = torch.stack([y[1] for y in minibatches])
    #print(xb, yeb)
    #x, ye = get_item() 
    y = torch.squeeze(model(xb))
    loss = criterion(y,yeb)
    #print(minibatches,_, loss)
    loss.backward()

    optimizer.step()
