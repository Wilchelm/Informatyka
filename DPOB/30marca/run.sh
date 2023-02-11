g++ -c lista.cpp
g++ -c main.cpp
g++ -o main main.o lista.o
rm main.o lista.o
./main
rm main
