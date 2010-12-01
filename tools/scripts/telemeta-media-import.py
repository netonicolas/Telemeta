#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010 Guillaume Pellerin
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://svn.parisson.org/telemeta/TelemetaLicense.
#
# Author: Guillaume Pellerin <yomguy@parisson.com>
#

import os
import sys
import logging
import datetime
from django.core.management import setup_environ
from django.core.files.base import ContentFile


class Logger:

    def __init__(self, file):
        self.logger = logging.getLogger('myapp')
        self.hdlr = logging.FileHandler(file)
        self.formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.hdlr.setFormatter(self.formatter)
        self.logger.addHandler(self.hdlr)
        self.logger.setLevel(logging.INFO)

    def write_info(self, prefix, message):
        self.logger.info(' ' + prefix + ' : ' + message.decode('utf8'))

    def write_error(self, prefix, message):
        self.logger.error(prefix + ' : ' + message.decode('utf8'))


class TelemetaMediaImport:

    def __init__(self, media_dir, log_file):
        self.logger = Logger(log_file)
        self.media_dir = media_dir + os.sep + 'items'
        self.medias = os.listdir(self.media_dir)
        self.buffer_size = 0x1000
        
    def set_collection(self, collection_name):
        collections = telemeta.models.media.MediaCollection.objects.filter(code=collection_name)
        if not collections:
            c = telemeta.models.media.MediaCollection(code=collection_name)
            c.title = collection_name
            c.save()
            msg = 'added'
            self.logger.write_info(collection_name, msg)
            collection = c
        else:
            collection = collections[0]
        return collection

    def media_import(self):
        import telemeta.models
        self.collection_name = 'awdio'
        self.collection = self.set_collection(self.collection_name)

        for media in self.medias:
            filename,  ext = os.path.splitext(media)
            item = telemeta.models.media.MediaItem.objects.filter(code=filename)
            if not item:
                print media
                item = telemeta.models.media.MediaItem(collection=self.collection, code=filename)
                item.title = filename
                item.file = media
                item.save()
                msg = 'added item : ' + filename
                self.logger.write_info(self.collection_name, msg)


def run():
    project_dir = sys.argv[-2]
    log_file = sys.argv[-1]
    sys.path.append(project_dir)
    import settings
    setup_environ(settings)
    media_dir = settings.MEDIA_ROOT
    t = TelemetaMediaImport(media_dir, log_file)
    t.media_import()

if __name__ == '__main__':
    run()
