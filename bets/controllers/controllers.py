# -*- coding: utf-8 -*-
from odoo import http

# class Bets(http.Controller):
#     @http.route('/bets/bets/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bets/bets/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bets.listing', {
#             'root': '/bets/bets',
#             'objects': http.request.env['bets.bets'].search([]),
#         })

#     @http.route('/bets/bets/objects/<model("bets.bets"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bets.object', {
#             'object': obj
#         })