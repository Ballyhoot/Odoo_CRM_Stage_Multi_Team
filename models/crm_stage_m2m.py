# -*- coding: utf-8 -*-
from odoo import api, fields, models

class CrmStage(models.Model):
    _inherit = "crm.stage"

    team_ids = fields.Many2many(
        "crm.team",
        "crm_stage_team_rel",
        "stage_id",
        "team_id",
        string="Sales Teams",
        help="If set, this stage is available only for the selected Sales Teams. "
             "If left empty (and single 'Sales Team' is also empty), the stage is shared for all teams."
    )

    team_id = fields.Many2one(
        "crm.team",
        string="(Legacy) Sales Team",
        help="Original single-team field. Selecting a team here will automatically add it in 'Sales Teams'."
    )

    @api.onchange("team_id")
    def _onchange_team_id_sync(self):
        if self.team_id:
            if self.team_ids:
                if self.team_id not in self.team_ids:
                    self.team_ids = [(4, self.team_id.id)]
            else:
                self.team_ids = [(6, 0, [self.team_id.id])]
