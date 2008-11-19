# Copyright (C) 2008 Parisson SARL
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://svn.parisson.org/telemeta/TelemetaLicense.
#
# Author: Guillaume Pellerin <yomguy@parisson.com>

from telemeta.analysis.core import *
from telemeta.analysis.api import IMediaItemAnalyzer
import numpy

class ResolutionAnalyser(AudioProcessor):
    """Media item analyzer driver interface"""

    implements(IMediaItemAnalyzer)

    def get_id(self):
        return "resolution"

    def get_name(self):
        return "Resolution"

    def get_unit(self):
        return "bits"

    def render(self, media_item, options=None):
        self.pre_process(media_item)
        if '8' in self.encoding:
            return 8
        if '16' in self.encoding:
            return 16
        if '24' in self.encoding:
            return 24
        if '32' in self.encoding:
            return 32
        else:
            return ''