g++ -c komputer.cpp
g++ -c main.cpp
g++ -o main main.o komputer.o
rm main.o komputer.o
./main
rm main
