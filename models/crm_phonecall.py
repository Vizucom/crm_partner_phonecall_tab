# -*- coding: utf-8 -*-
from openerp.osv import osv
from openerp.osv.osv import except_osv
from openerp.tools.translate import _


class crm_phonecall(osv.Model):

    _inherit = 'crm.phonecall'

    def jump_to_details(self, cr, uid, ids, context=None):

        clicked_call = self.browse(cr, uid, ids[0], context)

        return {
            'type': 'ir.actions.act_window',
            'name': _('Phone call'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'crm.phonecall',
            'res_id': clicked_call.id,
            'target': 'current',
            'context': context,
         }
