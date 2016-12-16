from fanstatic import Library, Resource, Group
from js.bootstrap import bootstrap
from js.jquery import jquery

library = Library('bootstrap_typeahead', 'resources')

ajax_typeahead = Resource(library, 'bootstrap-typeahead.js',
                        minified='bootstrap-typeahead.min.js',
                        bottom=True,
                        depends=[bootstrap, jquery,])