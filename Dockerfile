FROM python:3.8

ADD tester.py /

ENTRYPOINT ["python"]
CMD ["./tester.py"]