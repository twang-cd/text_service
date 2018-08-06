FROM python:3-stretch as builder
WORKDIR /src
COPY requirements.txt /src
RUN pip install --upgrade pip wheel
RUN mkdir .wheels
RUN pip wheel --wheel-dir .wheels -r requirements.txt


FROM python:3-slim-stretch
ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/opt/app
WORKDIR $APP_HOME
COPY --from=builder /src/.wheels /build/.wheels
COPY requirements.txt $APP_HOME
RUN pip install --no-index --find-links=/build/.wheels -r requirements.txt
COPY . $APP_HOME
