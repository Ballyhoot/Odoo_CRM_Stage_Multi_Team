# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID

def post_init_hook(cr, registry):
    """On install: migrate any existing single team assignment to the new many2many."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    stages = env["crm.stage"].search([("team_id", "!=", False)])
    for st in stages:
        st.write({"team_ids": [(4, st.team_id.id)]})
