# -*- coding: utf-8 -*-
from odoo import api, models
from odoo.osv import expression

class CrmLead(models.Model):
    _inherit = "crm.lead"

    @api.model
    def _stage_domain_for_team(self, team_id):
        tid = team_id.id if hasattr(team_id, "id") else team_id or False
        if tid:
            return ['|', ('team_id', '=', False), '|', ('team_id', '=', tid), ('team_ids', 'in', [tid])]
        else:
            return ['|', ('team_id', '=', False), ('team_ids', '=', False)]

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        ctx_team_id = self._context.get('default_team_id') or self._context.get('team_id')
        base_domain = domain or []
        team_domain = self._stage_domain_for_team(ctx_team_id)
        full_domain = expression.AND([base_domain, team_domain])
        stage_ids = self.env['crm.stage'].search(full_domain, order=order).ids
        return stage_ids, {}

    def _stage_find(self, team_id=False, domain=None, order='sequence'):
        domain = domain or []
        team_domain = self._stage_domain_for_team(team_id or self.team_id.id)
        full_domain = expression.AND([domain, team_domain])
        return self.env['crm.stage'].search(full_domain, order=order, limit=1)
