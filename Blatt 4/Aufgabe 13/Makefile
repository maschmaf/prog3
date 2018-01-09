NAME=a13

$(NAME):$(NAME).c
	cc -g -ansi -pedantic -Wall $(NAME).c -o $(NAME)
	
run: $(NAME)
		./$(NAME)
		
clean:
		-/bin/rm $(NAME) $(NAME).o
