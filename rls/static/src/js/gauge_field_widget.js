odoo.define('rls.gauge_field', function (require) {
    "use strict";

    var field_registry = require('web.field_registry');
    var FieldGauge = require('web.basic_fields').FieldGauge;

    var GaugeField = FieldGauge.extend({
        _render: function () {
            this.max_value = this.recordData.max_value || 100;
            return this._super.apply(this, arguments);
        },
    });

    field_registry.add('gauge_field', GaugeField);

    return {
        GaugeField: GaugeField,
    };
});
