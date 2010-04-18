from django.contrib import admin
from opag.main.models import Notice, Meeting, MeetingTalk

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible')
    list_display_links = ('title',)

class MeetingTalkInline(admin.StackedInline):
    model = MeetingTalk

class MeetingAdmin(admin.ModelAdmin):
    model = Meeting
    inlines = [ MeetingTalkInline ]
    list_display = ('date', 'firm', 'speakers_wanted')
    list_display_links = ('date',)
    list_filter = ('firm',)

admin.site.register(Notice, NoticeAdmin)
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(MeetingTalk, MeetingTalkInline)