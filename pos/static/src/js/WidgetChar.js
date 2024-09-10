odoo.define('pos.CustomFieldChar', function (require) {
    "use strict";

    const FieldChar = require('web.basic_fields').InputField;
    const FieldRegistry = require('web.field_registry');

    const customChar = FieldChar.extend({
        events: _.extend({}, FieldChar.prototype.events, {
            'focus': '_onFieldFocus',
        }),
        _onFieldFocus: function () {
            const $focusable = this.getFocusableElement();
            $focusable.attr('style', 'background-color: yellow !important');
        },
        _onBlur: function (){
          const $focusable = this.getFocusableElement();
          $focusable.removeAttr('style');
        },
        _applyChanges: function (ev, picker) {
            this.trigger_up('field_focus', {});
        }
    })


    FieldRegistry.add('customField', customChar);
    return customChar;

});