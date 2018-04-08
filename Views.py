from flask.views import View
from flask import render_template

class ListView(View):

    def dispatch_request(self):
        data = [{'title':'python3 dict','text':'python dictionary object'},
                {'title':'selenium python','text':'selenium python library and robotframework'},
                {'title':'python nose test','text':'nose test framework'}
        ]
        return render_template('show_entries.html',entries=data)










