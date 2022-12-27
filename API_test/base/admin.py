from django.contrib import admin

from .models import employe,test,author,Address,detail,published,Bookname
admin.site.register(employe)
admin.site.register(Address)
admin.site.register(detail)
admin.site.register(test)
admin.site.register(author)
admin.site.register(published)
admin.site.register(Bookname)
# Register your models here.
