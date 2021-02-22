FROM bxwill/robotframework:py-chrome-allure
LABEL maintainer='v.stone@163.com'
WORKDIR /workspace
COPY config config
COPY common common
COPY elements elements
COPY pages pages
COPY keywords keywords
COPY testcase testcase
COPY kdp-robot kdp-robot
COPY requirements.txt requirements.txt
ENV PYTHONPATH=/workspace
RUN pip install -r requirements.txt
