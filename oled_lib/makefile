CFLAGS=-c -Wall -O2
LIBS = -lm -lpthread

all: liboled.a

liboled.a: fonts.o oled.o
	ar -rc liboled.a oled.o fonts.o ;

oled.o: oled.c
	$(CC) $(CFLAGS) oled.c

fonts.o: fonts.c
	$(CC) $(CFLAGS) fonts.c

clean:
	rm -rf *.o liboled.a
