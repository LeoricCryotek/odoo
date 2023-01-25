odoo.define('documents_portal_management.kanban_ribbon', function (require) {
    'use strict';

    var widgetRegistry = require('web.widget_registry');
    var Widget = require('web.Widget');

    var KanbanRibbonWidget = Widget.extend({
        template: 'documents_portal_management.kanban_ribbon',
        xmlDependencies: ['/documents_portal_management/static/src/xml/kanban_ribbon.xml'],
        init: function (parent, data, options) {
            this._super.apply(this, arguments);
            this.text = options.attrs.title || options.attrs.text;
            this.classBgColor = options.attrs.bg_color ? options.attrs.bg_color : 'bg-success';
            this.icon = options.attrs.icon;
            this.classText ='';

            if (this.text && this.text.length > 5) {
                this.classText += ' o_small';
            } 
            else if (this.text && this.text.length > 3) {
                this.classText += ' o_medium';
            }
        },
    });
    widgetRegistry.add('kanban_ribbon', KanbanRibbonWidget);
    return KanbanRibbonWidget;
});