import typing as t

def make_chapters(data: str) -> t.List[str]:
    """Creating list of separate chapters from text """
    try:
        if "CHAPTER" in data:
            chapters=data.split("CHAPTER")
            chapters_c=[]
            for element in chapters:
                element_1 = "CHAPTER" + element
                if element!="":
                    chapters_c.append(element_1)
            return chapters_c
        else:
            return []
    except TypeError:
        print("Type Error - function requiers list of strings as argument")
    except Exception as e:
        print(e)

def make_chapter_titles(chapter: t.List[str]) -> t.List[str]:
    """Creating list of title sentences """
    try:
        title_sentences=[]
        for element in chapter:
            counter=0
            start=0
            end=0
            for i in range(len(element)):
                if element[i]=="." and counter<3:
                    counter+=1
                    if counter==1:
                        start=i+1
                    else:
                        if counter==2:
                            end=i+1
            sentence=element[start:end]
            sentence=sentence.lstrip()
            title_sentences.append(sentence)
        return title_sentences
    except TypeError:
        print("Type Error - function requiers string as argument")
    except Exception as e:
        print(e)
