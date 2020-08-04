#!bin/bash


# Start the gunicorn3 server process
echo Starting the HateSpeechFilter Gunicorn3 Server...

if [ ! -e /var/log/gunicorn ]; then
    mkdir -p /var/log/gunicorn
    touch /var/log/gunicorn/accesslog.log /var/log/gunicorn/error/log
fi
exec sudo gunicorn3 --bind 0.0.0.0:80 wsgi:app --access-logfile /var/log/gunicorn/accesslog.log  --error-logfile /var/log/gunicorn/error.log --daemon 
