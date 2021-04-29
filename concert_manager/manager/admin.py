from django.contrib import admin

from .models import Concert, ConcertLiveSet, LiveSet, SongSet, Song, ProgrammableConfiguration, NonProgrammableConfiguration
admin.site.site_header = 'Concert-manager'
admin.site.site_title = 'Concert-manager'

admin.site.register(Concert)
admin.site.register(ConcertLiveSet)
admin.site.register(LiveSet)
admin.site.register(SongSet)
admin.site.register(Song)
admin.site.register(ProgrammableConfiguration)
admin.site.register(NonProgrammableConfiguration)
