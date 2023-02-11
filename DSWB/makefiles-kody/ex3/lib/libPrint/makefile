#TODO - Add variables here - compiler, flags...
BINDIR:=bin
SRCDIR:=src
OBJDIR:=obj
DSTDIR:=..
CC=g++
CFLAGS=-c -Wall

all: build install

build: $(OBJDIR)/libPrint.o
	#TODO - FILL ME! Create library
	ar rvs libPrint.a $(OBJDIR)/libPrint.o

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp | $(OBJDIR) $(BINDIR)
	#TODO - FILL ME! Build .o file.
	$(CC) $(CFLAGS) $< -o $@

install: $(DSTDIR)/libPrint.a 

$(DSTDIR)/libPrint.a: $(OBJDIR)/libPrint.o
	#TODO - FILL ME! Copy lib from bin dir to destination directory - ../
	cp libPrint.a $(DSTDIR)/

clean:
	#TODO - FILL ME! Add removal of .o files and ./bin/*
	rm -rf $(BINDIR) $(OBJDIR)
