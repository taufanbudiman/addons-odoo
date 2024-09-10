odoo.define('pos.NumpadWidget', function (require) {
    'use strict';

    const NumpadWidget = require('point_of_sale.NumpadWidget');
    const Registries = require('point_of_sale.Registries');

    const PosNumpadWidget = (NumpadWidget) =>
        class extends NumpadWidget {
            get hasManualDiscount() {
                return false;
            }
            get hasPriceControlRights(){
                return false
            }
        };

    Registries.Component.extend(NumpadWidget, PosNumpadWidget);

    return NumpadWidget;
});
