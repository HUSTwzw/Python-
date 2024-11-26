#关于各种测试函数
from project_11 import get_name
def test_nomiddle_name():       #测试此函数在终端输入pytest project_11_extra.py::test_nomiddle_name
    username=get_name("wang","wen")
    assert username=="wang wen"

def test_middle_name():     #测试此函数在终端输入pytest project_11_extra.py::test_middle_name
    username=get_name("wang","wen","zi")
    assert username=="wang zi wen"


from project_11 import survey
def test_class():       #由于survey类中使用了input，而pytest不支持自动输入，因此测试较为特殊。测试此函数在终端输入pytest -s project_11_extra.py::test_class，并在终端输入一次survey类的input所需的输入
    researcher=survey("How old are you?")
    researcher.ask_question()
    researcher.store_answer()
    assert researcher.answer in researcher.response


from project_11 import survey
def test_classes():     #和test_class同理，测试此函数在终端输入pytest -s project_11_extra.py::test_classes,并在终端输入四次survey类的input所需的输入(因为range(1,5))
    researchers=survey("What is your name?")
    for number in range(1,5):
        researchers.ask_question()
        researchers.store_answer()
        assert researchers.answer in researchers.response


from project_11 import survey
import pytest       #应对NameError:name "pytest" is not defined
@pytest.fixture
def do_research():
    question="Where is Paris?"
    do_research=survey(question)
    return do_research      #pytest.fixture会将此函数返回值作为剩余两个函数的参数
    # 之后在终端分别输入pytest -s project_11_extra.py::test_class与pytest -s project_11_extra.py::test_classes，分别进行两个测试
def test_class(do_research):
    do_research.ask_question()
    do_research.store_answer()
    assert do_research.answer in do_research.response
def test_classes(do_research):
    for numbers in range(1,5):
        do_research.ask_question()
        do_research.store_answer()
        assert do_research.answer in do_research.response