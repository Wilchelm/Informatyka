CC=g++
CFLAGS=-c -Wall
OBJDIR:=obj
BINDIR:=bin
SRCDIR:=src

$(BINDIR)/main: $(OBJDIR)/main.o $(OBJDIR)/nazwa_krotka.o $(OBJDIR)/nazwa_dluga.o |$(BINDIR) $(OBJDIR)
	$(CC) $^ -o $@

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp $(SRCDIR)/%.hpp |$(BINDIR) $(OBJDIR) $(SRCDIR)
	$(CC) $(CFLAGS) $< -o $@

$(BINDIR):
	mkdir -p $(BINDIR)

$(OBJDIR):
	mkdir -p $(OBJDIR)

$(SRCDIR):
	mkdir -p $(SRCDIR)


.PHONY: clean
clean:
	rm -rf $(BINDIR) $(OBJDIR)
