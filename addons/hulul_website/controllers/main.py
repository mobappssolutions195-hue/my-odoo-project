
from odoo import http
from odoo.http import request
class HululWebsite(http.Controller):
    @http.route('/hulul-it-development', type='http', auth='public', website=True)
    def hulul_home(self, **kw):
        return request.render('hulul_website.hulul_homepage', {'title': 'Hulul-IT Development'})

        