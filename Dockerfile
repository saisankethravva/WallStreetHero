FROM centos:centos7

ENV CODE_BASE_DIR="/code"
ENV APP_NAME="wall-street-hero"
ENV SERVICE_NAME="stockapi"

USER root

RUN yum update -y && \
    yum install -y git && \
    yum install -y centos-release-scl && \
    yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm &&\
    yum install -y epel-release && \
    yum install -y llvm5.0-devel &&\
    yum install -y postgresql-devel && \
    yum install -y postgresql13 &&\
    yum install -y python3-devel && \
    yum install -y gcc && \
    yum install -y jq && \
    yum install -y python3-pip

RUN mkdir -p "${CODE_BASE_DIR}"/"${APP_NAME}"
RUN mkdir -p /creds

ADD stockapi "${CODE_BASE_DIR}"/"${APP_NAME}"/stockapi/
#ADD virtualbot "${CODE_BASE_DIR}"/"${APP_NAME}"/virtualbot/
RUN cd "${CODE_BASE_DIR}"/"${APP_NAME}"/ && \
    pwd && \
    python3 -m venv venv && \
    pip3 install --upgrade pip

COPY  stockapi/requirements.txt "${CODE_BASE_DIR}"/"${APP_NAME}"/"${SERVICE_NAME}"/
COPY  stockapi/startup_script.sh "${CODE_BASE_DIR}"/"${APP_NAME}"/"${SERVICE_NAME}"/
COPY  stockapi/config.py "${CODE_BASE_DIR}"/"${APP_NAME}"/"${SERVICE_NAME}"/
COPY  stockapi/main.py "${CODE_BASE_DIR}"/"${APP_NAME}"/"${SERVICE_NAME}"/
COPY  stockapi/README.md "${CODE_BASE_DIR}"/"${APP_NAME}"/"${SERVICE_NAME}"/



RUN ls -al /code/wall-street-hero/stockapi

RUN cd "${CODE_BASE_DIR}"/"${APP_NAME}"/"${SERVICE_NAME}"/ &&\
    pip3 install -r requirements.txt &&\
    pip3 install yfinance --upgrade --no-cache-dir

ENTRYPOINT ["/bin/bash","/code/wall-street-hero/stockapi/startup_script.sh"]


