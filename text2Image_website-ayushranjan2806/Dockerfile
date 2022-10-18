FROM python
EXPOSE 80
WORKDIR /webapp
COPY . .
RUN pip install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0","--port=80"]
