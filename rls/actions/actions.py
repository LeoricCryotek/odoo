from odoo import api, models, fields
from datetime import datetime, timedelta


class RequestLegalServicesActions(models.Model):
    _inherit = 'request.legal.services'

    @api.depends('start_date', 'end_date')
    def _compute_weekly_requests(self):
        for record in self:
            if record.start_date and record.end_date:
                start_date = fields.Date.from_string(record.start_date)
                end_date = fields.Date.from_string(record.end_date)
                date_diff = (end_date - start_date).days + 1
                weeks = (date_diff + start_date.weekday()) // 7

                if (date_diff % 7 + start_date.weekday()) % 7:
                    weeks += 1

                record.weekly_requests = weeks
            else:
                record.weekly_requests = 0
