import typing as t

def sort_two_lists_by_first(number_of_words: list, number_of_chapters: list) -> t.Tuple[list,list]:
    """"function for sorting first list by descending order
    and then second list by the order of elements in first list
     it returns tuple of two sorted lists"""
    try:
        if len(number_of_words)!=len(number_of_chapters):
            number_of_words="type error"
        for i in range(len(number_of_words)):
            for j in range(len(number_of_words)):
                if number_of_words[j] > number_of_words[i] and j > i:
                    temp = number_of_words[i]
                    number_of_words[i] = number_of_words[j]
                    number_of_words[j] = temp
                    temp2 = number_of_chapters[i]
                    number_of_chapters[i] = number_of_chapters[j]
                    number_of_chapters[j] = temp2
                if type(number_of_words[i]) != int or type(number_of_chapters[i])!=str:
                   number_of_words="type error"
        output = (number_of_words, number_of_chapters)
        return output
    except TypeError:
        print("Type error - function sort_two_lists_by_first requiers two lists of the same lenght as arguments ")
    except Exception as e:
        print(e)

