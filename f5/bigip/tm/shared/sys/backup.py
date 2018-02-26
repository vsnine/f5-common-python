# Copyright 2016 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Directory: shared module: sys.

REST URI
    ``https://localhost/mgmt/tm/shared/sys/backup``

GUI Path
    ``N/A``

REST Kind
    ``tm:shared:sys:*``

Example calls:
Create a backup:
makejob = mgmt.tm.shared.sys.backups.backup.create(name="backup1",file="backup1.ucs",action="BACKUP")

Delete a backup:
bkupjob = mgmt.tm.shared.sys.backups.backup.load(name="fe6069cd-4d45-451b-8c81-2dfad02326ee")
bkupjob.delete()

Check in-progress job status:
checkjob = mgmt.tm.shared.sys.backups.backup.load(name="fe6069cd-4d45-451b-8c81-2dfad02326ee")
checkjob.refresh()


"""


from f5.bigip.resource import Collection
from f5.bigip.resource import Resource

class Backups(Collection):
    '''Manage backup worker jobs.'''
    def __init__(self, sys):
        super(Backups, self).__init__(sys)
        self._meta_data['allowed_lazy_attributes'] = [Backup]
        self._meta_data['required_json_kind'] = \
            'tm:shared:sys:backup:ucsbackuptaskcollectionstate'
        self._meta_data['attribute_registry'] =\
            {u'tm:shared:sys:backup:ucsbackuptaskitemstate': Backup}
        self._meta_data['template_generated'] = True
        self._meta_data['required_load_parameters'] = set(('id',))

class Backup(Resource):
    '''Represent individual backup tasks'''
    def __init__(self, backups):
        super(Backup, self).__init__(backups)
        self._meta_data['allowed_lazy_attributes'] = []
        self._meta_data['required_json_kind'] = \
            'tm:shared:sys:backup:ucsbackuptaskitemstate'
    def create(self, **kwargs):
        '''Start a backup job. Requires name, file, and action parameters. action should be BACKUP.'''
        self._meta_data['required_creation_parameters'].update(['action', 'file'])
        return super(Backup, self)._create(**kwargs)

