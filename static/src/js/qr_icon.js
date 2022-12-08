/** @odoo-module **/
import SystrayMenu from 'web.SystrayMenu';
import Widget from 'web.Widget';
var ExampleWidget = Widget.extend({
   template: 'QRSystray',
   events: {
       'click #create_qr': '_onClick',
   },
   _onClick: function(){
       this.do_action({
            type: 'ir.actions.act_window',
            name: 'QR Generator',
            res_model: 'qr.generator',
            view_mode: 'form',
            views: [[false, 'form']],
            target: 'new'
       });
   },
});
SystrayMenu.Items.push(ExampleWidget);
export default ExampleWidget;