#!/usr/bin/env bash
set -x
rm -rf coursefinder-0.0
tar -xvzf coursefinder-0.0.tar.gz 
cd coursefinder-0.0
bash -x install.sh
cp conf/redirect.conf /etc/nginx/conf.d/
cp conf/coursefinder_nginx.conf /etc/nginx/sites-available/
cp conf/coursefinder_supervisor.conf /etc/supervisor/conf.d/
ln -fs /etc/nginx/sites-available/coursefinder_nginx.conf /etc/nginx/sites-enabled/
supervisorctl reread
supervisorctl update
supervisorctl restart all
systemctl restart nginx
