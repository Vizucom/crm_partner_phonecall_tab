# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2016- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Partner phonecalls tab',
    'category': 'CRM',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'depends': ['crm'],
    'description': """
Partner phonecalls tab
----------------------
* Show partner's phonecalls inside a new notebook page on the partner form
* The list also contains the partner's descendants' calls (i.e. when viewing the company's form, you also see the calls belonging to the company's contacts)

""",
    'data': [
        'view/res_partner.xml',

    ],
}
