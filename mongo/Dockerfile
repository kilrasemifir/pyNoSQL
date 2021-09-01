FROM python

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY api.py api.py

CMD ["python", "api.py"]