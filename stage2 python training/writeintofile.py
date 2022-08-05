with open('testfile.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('testfile.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)




#'r' = read mode
#'w' = write mode








