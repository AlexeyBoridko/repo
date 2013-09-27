# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Choice.votes1'
        db.delete_column(u'prj_testDjangoApp_choice', 'votes1')


    def backwards(self, orm):
        # Adding field 'Choice.votes1'
        db.add_column(u'prj_testDjangoApp_choice', 'votes1',
                      self.gf('django.db.models.fields.IntegerField')(default=2),
                      keep_default=False)


    models = {
        u'prj_testDjangoApp.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prj_testDjangoApp.Poll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {})
        },
        u'prj_testDjangoApp.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['prj_testDjangoApp']