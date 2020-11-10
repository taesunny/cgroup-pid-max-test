FROM python:3.8

ADD tester.py /

CMD [ "python", "./tester.py" ]