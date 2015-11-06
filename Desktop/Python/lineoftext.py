fh = open("hello.txt", "w")

lines_of_text = ["a line of text\n", "another line of text\n", "a third line\n"]

fh.writelines(lines_of_text)

fh.close