# -*- coding: utf-8 -*-
from odoo import http

class MyApp(http.Controller):
     @http.route('/my_app/my_app/', auth='public')
     def index(self, **kw):
         return "Hello, world","i m here"

     @http.route('/my_app/my_app/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('my_app.listing', {
             'root': '/my_app/my_app',
             'objects': http.request.env['my_app.my_app'].search([]),
         })

     @http.route('/my_app/my_app/objects/<model("my_app.my_app"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('my_app.object', {
             'object': obj
         })
