
clean:
	rm -fv *~ ?.out

run:
	@python xmas1 > 1.out
	@python xmas2 > 2.out
	@sh xmas3 > 3.out
	@python xmas4 > 4.out
	@./whitespace.pl xmas5 > 5.out

sizes:
	@./size.py xmas1
	@./size.py xmas2
	@./size.py xmas3
	@./size.py xmas4
	@./size.py xmas5

compare: run
	@diff -B 1.out full-lyrics.txt
	@diff -B 2.out full-lyrics.txt
	@diff -B 3.out full-lyrics.txt
	@diff -B 4.out full-lyrics.txt
	@diff -B 5.out full-lyrics.txt
