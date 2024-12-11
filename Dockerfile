
FROM public.ecr.aws/lambda/python:3.11

RUN mkdir -p /app
COPY . app.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["app.py"]
ENTRYPOINT ["python"]