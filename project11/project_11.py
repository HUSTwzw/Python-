def get_name(first,last,middle=""):
    if middle:
        username=f"{first} {middle} {last}"
    else:
        username=f"{first} {last}"
    return username


class survey:
    def __init__(self,question):
        self.question=question
        self.response=[]
    def ask_question(self):
        self.answer=input(self.question)
    def store_answer(self):
        self.response.append(self.answer)
    def show_result(self):
        print(self.response)