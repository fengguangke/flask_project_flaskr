#coding=utf-8
from flask.views import View,MethodView
from flask import render_template,request,jsonify,redirect,url_for

class ListView(View):

    def dispatch_request(self):
        data = [{'title':'python3 dict','text':'python dictionary object'},
                {'title':'selenium python','text':'selenium python library and robotframework'},
                {'title':'python nose test','text':'nose test framework'}
        ]
        return render_template('show_entries.html',entries=data)


class UserView(MethodView):

    users = [{'user_id':'20071991','name':'fengguangke'},
            {'user_id':'20081992','name':'xiao ning'}
            ]

    def get(self,user_id):
        if user_id is None:
            return jsonify(self.users)
        else:
            for user in self.users:
                if user['user_id'] == str(user_id):
                    return jsonify(user)
            else:
                return jsonify(code=400,error='user not exists')

    def post(self):
        if not request.form['user_id']:
            return jsonify(code=400,error='user_id required')
        if not request.form['name']:
            return jsonify(code=400 , error='name required')

        self.users.append({'user_id':request.form['user_id'],'name':request.form['name']})
        return jsonify(code=200 , error='',msg='添加用户成功')

    def delete(self,user_id):
        if user_id is None:
            return jsonify(code=400 , error='user_id required')

        else:
            for user in self.users:
                if user['user_id'] == user_id:
                    self.users.remove(user)
                    return jsonify(code=200,error='',msg='删除用户成功')
            else:
                return jsonify(code=400,error='user not exists'),400

    def put(self,user_id):
        # update a single user
        pass





