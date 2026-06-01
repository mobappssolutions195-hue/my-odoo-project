# from odoo import http
# from odoo.http import request

# class HululWebsite(http.Controller):
#     @http.route('/hulul-home', type='http', auth='public')
#     def hulul_home(self, **kw):
#         # return "Working"
#         return request.render('hulul_website.hulul_homepage')

# from odoo import http
# class HululWebsite(http.Controller):
#     @http.route('/hulul-home', type='http', auth='public')
#     def hulul_home(self, **kw):
#         return "Hulul Route Working"

# from odoo import http
# class HululWebsite(http.Controller):
#     @http.route('/hulul-home', type='http', auth='public', csrf=False)
#     def hulul_home(self, **kw):
#         return http.request.env['ir.ui.view']._render_template(
#             'hulul_website.hulul_homepage',
#             {}
#         )
from odoo import http
from odoo.http import request
class HululWebsite(http.Controller):
    @http.route('/hulul-it-development', type='http', auth='public', website=True)
    def hulul_home(self, **kw):
        return request.render('hulul_website.hulul_homepage', {'title': 'Hulul-IT Development'})