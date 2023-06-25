FROM python:3.6.4-alpine3.7


RUN pip install pymongo

COPY seed.py /

CMD python3 seed.py

#  docker-compose up --build
# docker image rm konebachirou/seed
# docker push konebachirou/seed    
# docker login
#  docker-compose up --build -d