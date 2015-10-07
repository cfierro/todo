var Backbone = require('backbone');
var $ = require('jquery');
var _ = require('underscore');

var ItemView = Backbone.View.extend({
    tagName: 'li',

    initialize: function() {
        _.bindAll(this, 'render');
    },

    render: function() {
        $(this.el).html('<span>' + this.model.get('part1') + ' ' +
                this.model.get('part2') + '</span>');
        return this;
    }
});

module.exports = ItemView;
