from file import File


class FileImg(File):
    def __init__(self,file_name, size, description, content,date_modified,type: str,dimension_picture: str):
        super().__init__(file_name, size, description,content,date_modified,type)
        self.dimension_picture=dimension_picture
        self.type = "img"

    def __str__(self):
        return f"{self.file_name}.{self.type},{self.size}KB,{self.description},{self.content},Date modified:{str(self.date_modified):.19s} dimension of picture:{self.dimension_picture}"