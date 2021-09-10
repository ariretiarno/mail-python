FROM python

WORKDIR /app

ADD mail.py .

CMD ["python", "-u", "mail.py"]