FROM text_service:latest as static
RUN python manage.py collectstatic --no-input


FROM nginx:latest
COPY --from=static /static /static
COPY ./infra/nginx/nginx.conf /etc/nginx/nginx.conf
