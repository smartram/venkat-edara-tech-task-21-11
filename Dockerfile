FROM python:3.7-alpine
MAINTAINER Venkata Edara "smart.ram856@gmail.com"
RUN mkdir /app
RUN mkdir /app/resources
COPY resources/recipes.json /app/resources/
COPY resources/ingredients.json /app/resources/
COPY requirements.txt /app/
COPY main.py /app/
COPY ingredient.py /app/
COPY chef.py /app/
RUN pip install -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8080", "main:app"]