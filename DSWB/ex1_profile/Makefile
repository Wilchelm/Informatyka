SOURCES=$(wildcard *.c)
OBJECTS=$(SOURCES:.c=.o)
CFLAGS=-Wall -pg


main: $(OBJECTS)
	g++ $(CFLAGS) $^ -o $@

clean:
	rm -f $(OBJECTS) main

.PHONY: clean
