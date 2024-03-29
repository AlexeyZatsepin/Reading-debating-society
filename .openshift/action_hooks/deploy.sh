#!/bin/bash
#this one is the deploy hook .openshift/action_hooks/deploy
source $OPENSHIFT_HOMEDIR/python/virtenv/bin/activate
cd $OPENSHIFT_REPO_DIR
echo "Executing 'python manage.py migrate'"
python manage.py makemigrations
python manage.py migrate
echo "Executing 'python manage.py collectstatic --noinput'"
python manage.py collectstatic --noinput

########################### end of file
