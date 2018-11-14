def get_value(name):
    # return the value of given name
    return sum([ord(i.lower()) - 96 for i in name if i != "-"])

def get_name_list():
    name_list = []
    fin = open('roster.txt')
    for line in fin:
        word = line.strip()
        name_list.append(word)
        name_list = [line.split(None, 1)[0] for line in fin]
    return name_list

def who_has_highest_value(name_list):
    #return the name with highest value among the given name_list
    """I used this function to find the highest scorer & the score associated with said person. So it returns both values together"""
    onset_score = 0
    highest_value = ""
    fin = open('roster.txt')
    data = fin.readlines()
    for x in data:
        first_name = x.split()[0] #Split so that only first name is returned
        if get_value(first_name) > onset_score: #if the value returned for the current name is higher than onset score than 
            onset_score = get_value(first_name) # the new score becomes the score value of the name
            highest_value = first_name #highest_value become current highest name
    return "Highest is {} and has score {}". format(highest_value, onset_score)
    
def get_words_with_same_value(value):
    # return a list of matched words
    matches = []
    positive = get_words()
    for word in positive:
        numeric_value = get_value(word)
        if numeric_value == value:
            matches.append(word)
    else:
        return matches

def get_words():
    # return a list of words
    with open("./positive-words.txt") as x:
        words = x.readlines()
    words = [x.strip() for x in words] 
    return words

def main():
    roster = get_name_list()
    valued = who_has_highest_value(roster)
    print(valued)
    # Get the value of my name and see if there are matching words
    
    mine = "Siddhanth"
    print("My score was", get_value(mine))  
    
    # Find matching words
    self_value = get_value(mine)
    matching_words = get_words_with_same_value(self_value)
    print(" The matches for " +  mine + " are " + str(matching_words))
    
if __name__ == '__main__':
    main()