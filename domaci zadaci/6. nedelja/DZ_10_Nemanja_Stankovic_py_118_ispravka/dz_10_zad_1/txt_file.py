from file import File


class FileTxt(File):
    def __init__(self, file_name: str, size: int, description: str, content: str,date_modified,type: str,number_of_chars: int=0,):
        super().__init__(file_name, size, description,content,date_modified,type)
        self.type = "txt"
        self.number_of_chars=len(self.content)


    def __str__(self):
        return f"{self.file_name}.{self.type},{self.size}KB,{self.description},{self.content},Date modified:{str(self.date_modified):.19s} number of characters:{self.number_of_chars}"

