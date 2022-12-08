try:
    import qrcode
except ImportError:
    qrcode = None
try:
    import base64
except ImportError:
    base64 = None
from io import BytesIO
from odoo.exceptions import UserError
from odoo import fields, models, _


class QRGenerator(models.Model):
    _name = "qr.generator"
    _description = "QR Generator"

    text = fields.Text(string="Text")
    boolean = fields.Boolean(string="Boolean", default=False)
    qr_code = fields.Binary('QR Code')
    qr_download = fields.Binary('Download Your QR', compute="action_generate_qr")

    def action_reset_qr(self):
        self.text = ""
        self.boolean = False
        print("aa", self.boolean)
        return {
            "type": "ir.actions.act_window",
            "view_mode": 'form',
            "res_model": 'qr.generator',
            "target": 'new',
        }

    def action_generate_qr(self):
        self.boolean = True
        for rec in self:
            if qrcode and base64:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=3,
                    border=4,
                )
                qr.add_data("Text : ")
                qr.add_data(rec.text)
                qr.make(fit=True)
                img = qr.make_image()
                temp = BytesIO()
                img.save(temp, format="PNG")
                qr_image = base64.b64encode(temp.getvalue())
                print(qr_image)
                rec.update({'qr_code': qr_image})
                rec.update({'qr_download': qr_image})

            else:
                raise UserError(_('Necessary Requirements To Run This Operation Is Not Satisfied'))
            return {
                "type": "ir.actions.act_window",
                "view_mode": 'form',
                "res_model": 'qr.generator',
                "target": 'new',
                "res_id": self.id
            }
