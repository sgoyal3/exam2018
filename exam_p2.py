import csv
def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742
    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]
    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]
    """
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    return your_list
#Used the csv function you provided I did this (grabbed code from the site)
#print(process_file('babynames\yob1880.txt')) < this worked


def total_births(year):
    """
    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    file_name = "babynames/yob" + str(year) + ".txt"
    naming_data = process_file(file_name)
    
    total = 0
    for x in naming_data:
        total += int(x[2])
    return total

#print(total_births(1981))


def proportion(name, gender, year):
    """
    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    file_name = "babynames/yob" + str(year) + ".txt"
    naming_data = process_file(file_name)
    births = 0
    total_number_of_births = total_births(year)
    for x in naming_data:
        if x[0] == name and x[1] == gender:
            births = x[2]
    return births/total_number_of_births

#print(proportion('Siddhanth', 'M', 2000)) <- this did not work

    
def highest_year(name, gender):
    """
    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    # year_range = range(1880, 2011)
    # peak_year = 0
    # highest_proportion_initial_to_end = 0
    # for year in year_range:
    #     if proportion > highest_proportion_initial_to_end:
    #         peak_year = year
    #         highest_proportion_initial_to_end = proportion
    # return peak_year
    #Couldn't get this function to work whatsoever, so I commented it out.

def main():
    print(process_file('babynames\yob1880.txt'))
    print(total_births(1981))
    print(proportion('Siddhanth', 'M', 2000))
    print(highest_year('Siddhanth', 'M'))
    """I included these functions & testers in main, but they didn't work for the last two functions,
       which is something I couldn't figure out unfortunately. I tried to fix it, but it's already pretty late, and I don't want to spend
       too much time working on this & ignoring the other questions. Sorry about that professor"""

if __name__ == '__main__':
    main()