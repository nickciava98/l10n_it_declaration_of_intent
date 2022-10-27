from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class AccountFiscalPosition(models.Model):
    _inherit = "account.fiscal.position"

    valid_for_declaration_of_intent = fields.Boolean(
        "Valid for declaration of intent"
    )

    @api.constrains("valid_for_declaration_of_intent", "tax_ids")
    def _check_taxes_for_declaration_of_intent(self):
        for fiscal_position in self:
            if fiscal_position.valid_for_declaration_of_intent \
                and not fiscal_position.tax_ids:
                raise ValidationError(
                    _("Define taxes for fiscal position %s valid "
                      "for declaration of intent") % fiscal_position.name
                )
