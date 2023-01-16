from chapters import make_chapters, make_chapter_titles
from words import list_of_words, frequency_words, text_all_analytics
from folders import make_folder, make_n_chapter_folders_in_main_folder, make_txt_chapter_file, make_txt_analytics_file
from sort import sort_two_lists_by_first
import os


def main():
    with open("20000 leagues-under-Jules-Verne-[ebooksread.com].txt", "r") as f:
        data = f.read()
    list_of_chapters = make_chapters(data)
    title_sentences = make_chapter_titles(list_of_chapters)

    """Creating folder part I and 23 CHAPTER folders inside that folder"""
    path_part_1=make_folder("PART I")
    list_of_paths_1=make_n_chapter_folders_in_main_folder(path_part_1,23)
    number_of_words_in_chapter_list_part_1=[]
    number_of_chapter_list_1=[]

    """Creating text files inside CHAPTER folders"""
    for i in range(len(list_of_paths_1)):
        make_txt_chapter_file(list_of_paths_1[i],list_of_chapters[i],title_sentences[i])
        make_txt_analytics_file(list_of_paths_1[i],list_of_chapters[i],i)
        number_of_words_in_chapter_list_part_1.append(len(list_of_words(list_of_chapters[i])))
        number_of_chapter_list_1.append("PART_01_CHAPTER_"+str(i+1)+":")

    """Creating folder part II and 23 CHAPTER folders inside that folder"""
    path_part_2 = make_folder("PART II")
    list_of_paths_2 = make_n_chapter_folders_in_main_folder(path_part_2, 23)
    number_of_words_in_chapter_list_part_2 = []
    number_of_chapter_list_2=[]

    """Creating text files inside CHAPTER folders"""
    for i in range(len(list_of_paths_2)):
        make_txt_chapter_file(list_of_paths_2[i],list_of_chapters[i+23],title_sentences[i+23])
        make_txt_analytics_file(list_of_paths_2[i],list_of_chapters[i+23],i)
        number_of_words_in_chapter_list_part_2.append(len(list_of_words(list_of_chapters[i+23])))
        number_of_chapter_list_2.append("PART_02_CHAPTER_" + str(i + 1) + ":")

    """Creating all anallytics file"""
    path_all_analytics=make_folder("ALL_ANALYTICS")
    number_of_words_in_chapter_list=number_of_words_in_chapter_list_part_1+number_of_words_in_chapter_list_part_2
    number_of_chapter_list=number_of_chapter_list_1+number_of_chapter_list_2
    data_t = sort_two_lists_by_first(number_of_words_in_chapter_list, number_of_chapter_list)
    data_anallytics = text_all_analytics(data_t[0], data_t[1])
    make_txt_chapter_file(path_all_analytics,data_anallytics,"all_analytics.")

if __name__ == '__main__':
    main()