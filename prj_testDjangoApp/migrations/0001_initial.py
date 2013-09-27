# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poll'
        db.create_table(u'prj_testDjangoApp_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'prj_testDjangoApp', ['Poll'])

        # Adding model 'Choice'
        db.create_table(u'prj_testDjangoApp_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['prj_testDjangoApp.Poll'])),
            ('choice', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('votes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'prj_testDjangoApp', ['Choice'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table(u'prj_testDjangoApp_poll')

        # Deleting model 'Choice'
        db.delete_table(u'prj_testDjangoApp_choice')


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