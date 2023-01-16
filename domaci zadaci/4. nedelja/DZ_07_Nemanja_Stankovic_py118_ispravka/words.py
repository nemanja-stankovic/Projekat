
def list_of_words(data: str) -> list:
    """function that creates list of words from text"""
    try:
        list_of_words = data.split()
        list_of_words_clear = []
        for i in range(len(list_of_words)):
            word = ""
            for j in range(len(list_of_words[i])):
                if list_of_words[i][j].isalpha() or list_of_words[i][j].isnumeric() or list_of_words[i][j] == "-":
                    word += list_of_words[i][j].lower()
            list_of_words_clear.append(word)
        return list_of_words_clear
    except TypeError:
        print("Greska prilikom pozivanja funkcije make_chapter_titles, argument mora biti string")
    except Exception as e:
        print(e)

def frequency_words(list_of_words: list) -> dict:
    """function that creates dictionary from list of words
    for every word as a key in that dictionary, value is percentage of occurrences of that word"""
    try:
        dict = {}
        for i in range(len(list_of_words)):
            counter=0
            for j in range(len(list_of_words)):
                if list_of_words[i]==list_of_words[j]:
                    counter+=1
            dict[list_of_words[i]]=counter/len(list_of_words)
        return dict
    except TypeError:
        print("Type error - function fruequency_words requiers list of strings as argument")
    except Exception as e:
        print(e)

def text_all_analytics(list_1: list,list_2: list) -> str:
    """function that creates text from elements in two lists"""
    try:
        all_analytics=""
        for i in range(len(list_1)):
            all_analytics += str(list_2[i])+str(list_1[i])+"\n"
        return all_analytics
    except TypeError:
        print("Type error - function text_all_analytics requiers two lists of the same lenght as arguments")
    except Exception as e:
        print(e)

