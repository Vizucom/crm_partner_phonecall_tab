# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.osv.osv import except_osv
from openerp.tools.translate import _


class res_partner(osv.Model):

    _inherit = 'res.partner'

    def _get_descendant_phonecall_ids(self, cr, uid, ids, field_names, arg=None, context=None):
        res = {}
        for partner in self.browse(cr, uid, ids, context):
            matching_partner_ids = self.search(cr, uid, args=[('id', 'child_of', partner.id)], context=context)
            phonecall_ids = self.pool.get('crm.phonecall').search(cr, uid, args=[('partner_id', 'in', matching_partner_ids)], context=context)
            res[partner.id] = phonecall_ids
        return res

    _columns = {
        'descendant_phonecall_ids': fields.function(_get_descendant_phonecall_ids, string='Phone calls', type='one2many', relation='crm.phonecall'),
    }
