from datetime import datetime
now = datetime.now()
class File:

    def __init__(self, file_name: str, size: int, description: str,content: str, date_modified, type:str ):
        self.file_name=file_name
        self.type=type
        self.size=size
        self.description=description
        self.date_modified=now
        self.content=content

    def __str__(self):
        return f"{self.file_name}.{self.type},{self.size}KB,{self.description},{self.content},Date modified:{str(self.date_modified):.19s}"

    def read(self):
        return self.content

    def write(self,add_content):
        self.content+=add_content
        return self.content

    def delete_all_content(self):
        self.content=""
        return self.content


