odoo.define('pos.ReceiptScreen', function(require) {
    'use strict';

    const ReceiptScreen = require('point_of_sale.ReceiptScreen');
    const Registries = require('point_of_sale.Registries');

    const PosReceiptScreen = (ReceiptScreen) =>
        class extends ReceiptScreen {
            async mounted() {
               super.mounted();
               if(this.currentOrder.get_client()){
                   this.onSendEmail()
               }
            }
        };

    Registries.Component.extend(ReceiptScreen, PosReceiptScreen);

    return ReceiptScreen;
});