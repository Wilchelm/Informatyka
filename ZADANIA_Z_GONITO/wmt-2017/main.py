import torch

# German to English translation
de2en = torch.hub.load('pytorch/fairseq', 'transformer.wmt19.de-en', checkpoint_file='model1.pt:model2.pt:model3.pt:model4.pt',
                       tokenizer='moses', bpe='fastbpe')

'''
a=open('./dev-0/in.tsv','r').readlines()
b=open('./dev-0/out.tsv','w+')
length=len(a)

for i in a:
    i=i.replace('\n','')
    pom1=de2en.translate(i)
    pom2=pom1+'\n'
    b.write(pom2)
    print (length)
    length-=1
b.close()

a=open('./dev-1/in.tsv','r').readlines()
b=open('./dev-1/out.tsv','w+')
length=len(a)

for i in a:
    i=i.replace('\n','')
    pom1=de2en.translate(i)
    pom2=pom1+'\n'
    b.write(pom2)
    print (length)
    length-=1
b.close()
'''
a=open('./test-A/in.tsv','r').readlines()
b=open('./test-A/out.tsv','w+')
length=len(a)

for i in a:
    i=i.replace('\n','')
    pom1=de2en.translate(i)
    pom2=pom1+'\n'
    b.write(pom2)
    print (length)
    length-=1
b.close()
