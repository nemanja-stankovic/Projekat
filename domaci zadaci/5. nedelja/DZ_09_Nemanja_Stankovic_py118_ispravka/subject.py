class Subject:

    def __init__(self,name_of_subject: str,subject_ID: str):
        self.name_of_subject=name_of_subject
        self.subject_ID=subject_ID

    def __str__(self):
        return f"{self.name_of_subject}, {self.subject_ID}"

