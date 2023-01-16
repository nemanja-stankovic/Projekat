import os
import typing as t
from words import list_of_words, frequency_words


def make_folder(folder_name: str) -> str:
    """function for creating folder"""
    try:
        parent_path=os.getcwd()
        path=os.path.join(parent_path,folder_name)
        if os.path.exists(path)==False:
            os.mkdir(path)
        return path
    except Exception as e:
        print(e)

def make_n_chapter_folders_in_main_folder(main_folder_path: str,number_of_chapter_folders: int)-> t.List[str]:
    """function for creating chapter folders on certain path
        It returns list of paths where folder is created"""
    try:
        list_of_paths=[]
        for i in range(number_of_chapter_folders):
            CHAPTER="CHAPTER_"+str(i+1)
            path=os.path.join(main_folder_path,CHAPTER)
            if os.path.exists(path) == False:
                os.mkdir(path)
            list_of_paths.append(path)
        return list_of_paths
    except Exception as e:
        print(e)

def make_txt_chapter_file(path: str,data: str,title: str) -> None:
    """function for creating txt chapter files """
    try:
        full_title=title+"txt"
        parent_path = path
        path = os.path.join(parent_path, full_title)
        with open(path, "w") as f:
            f.write(data)
    except Exception as e:
        print(e)

def make_txt_analytics_file(path: str,data: str,index:int) -> None:
    """function for creating txt analytic files """
    try:
        full_title = "analytics_" + str(index + 1) + ".txt"
        parent_path = path
        path_analytics = os.path.join(parent_path, full_title)
        with open(path_analytics, "w") as f:
            data_analytics = frequency_words(list_of_words(data))
            f.write(str(data_analytics))
    except Exception as e:
        print(e)

