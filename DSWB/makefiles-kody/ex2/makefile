## Main makefile
#CC=g++
#CFLAGS=-c -Wall
#
#main: main.o dbgPrint.o
#	$(CC) main.o dbgPrint.o -o main
#
#main.o: main.cpp main.h
#	$(CC) $(CFLAGS) main.cpp -o main.o
#
#dbgPrint.o: dbgPrint.cpp dbgPrint.h
#	$(CC) $(CFLAGS) dbgPrint.cpp -o dbgPrint.o
#
#.PHONY: clean
#clean:
#	rm -f ./*.o main
#*/
CC=g++
CFLAGS=-c -Wall
OBJDIR:=obj
BINDIR:=bin

$(BINDIR)/main: $(OBJDIR)/main.o $(OBJDIR)/dbgPrint.o |$(BINDIR) $(OBJDIR)
	$(CC) $^ -o $@

$(OBJDIR)/%.o: %.cpp %.h |$(BINDIR) $(OBJDIR)
	$(CC) $(CFLAGS) $< -o $@

$(BINDIR):
	mkdir -p $(BINDIR)

$(OBJDIR):
	mkdir -p $(OBJDIR)



.PHONY: clean
clean:
	rm -rf $(BINDIR) $(OBJDIR)

