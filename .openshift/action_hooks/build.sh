#!/bin/bash
#is is .openshift/action/hooks/build
#remember to make it +x so openshift can run it.
if [ ! -d $OPENSHIFT_DATA_DIR/media ]; then
    mkdir -p $OPENSHIFT_DATA_DIR/media
fi
ln -snf $OPENSHIFT_DATA_DIR/media $OPENSHIFT_REPO_DIR/wsgi/static/media

######################### end of file
