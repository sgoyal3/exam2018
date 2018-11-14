def process_file(file_name):
    folderandfile = "./babynames/" + file_name
        
    lines = []
    with open(folderandfile, 'r') as f:
        for line in f.readlines():
            l,name = line.strip().split(',')
            lines.append((l,name))



    return lines
    
    
    
print(process_file('yob1880.txt'))
