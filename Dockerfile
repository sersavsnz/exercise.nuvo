# build stage
FROM python:3.11 AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy files
COPY ./ /project/

# install dependencies and project into the local packages directory
WORKDIR /project
RUN mkdir __pypackages__ && pdm sync --prod --no-editable


# run stage
FROM python:3.11

# retrieve packages from build stage
ENV PYTHONPATH=/project/pkgs:/project/

COPY --from=builder /project/__pypackages__/3.11/lib /project/pkgs
COPY --from=builder /project/src /project/src
COPY --from=builder /project/demo_app /project/demo_app
COPY --from=builder /project/flask_service /project/flask_service
COPY --from=builder /project/conf.py /project/conf.py

WORKDIR /project

# retrieve executables
COPY --from=builder /project/__pypackages__/3.11/bin/* /bin/

# expose port for streamlit and flask
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# set entrypoint to run streamlit app
ENTRYPOINT ["streamlit", "run", "demo_app/demo_app.py", "--server.port", "8501", "--global.developmentMode", "false"]