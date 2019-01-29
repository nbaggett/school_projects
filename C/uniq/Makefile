CFLAGS = -Wall -ansi -pedantic

uniq: uniq.o
	gcc -o uniq uniq.o

uniq.o: uniq.c
	gcc $(CFLAGS) -c uniq.c

clean: 
	rm *.o
	echo sweep sweep

test: uniq
	echo Testing uniq
	./uniq < test.txt > myuniq.out
	uniq < test.txt > unixuniq.out
	diff myuniq.out unixuniq.out
	echo done.
