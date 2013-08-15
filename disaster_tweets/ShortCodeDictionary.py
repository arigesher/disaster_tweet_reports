#   Copyright 2013 Palantir Technologies
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.from transform import Decorator
import json
import re
from transform import Decorator

split_re = re.compile('/')


class ShortCodeDictionary(Decorator):

    def __init__(self, json_dictionary):
        Decorator.__init__(self)
        self.json_dictionary = json_dictionary
        self.alphabet = json.loads(json_dictionary)

        # make sure we have field definitions
        if not self.alphabet['fields']:
            alphabet_dump = json.dumps(self.alphabet, indent=3)
            raise ValueError('Can\'t find field definitions in short code alphabet:\n%s' % (alphabet_dump))
        else:
            # build up field expanders
            self.expanders = []
            for field in self.alphabet['fields']:
                self.expanders.append(FieldExpander(field))

    def decorate(self, trimmed_tweet, original_tweet):
        text = trimmed_tweet[u'pretty_text']
        # preserve the unexpanded text
        trimmed_tweet[u'unexpanded_text'] = text
        data = split_re.split(text)
        fields = self.alphabet
        for i in len(fields):
            expander = self.expanders[i]
            datum = data[i]
            (expanded_text, expanded_json) = expander.expand(datum)
        #TODO

    def output_cheat_sheet(path):
        raise NotImplementedError()


class FieldExpander:

    def __init__(self, json_field_definition):
        self.field_definition = json_field_definition

    def expand(self, expansion_text):
        expanded_json = {}

        # start with the label
        label = self.field_definition[u'label']
        field_type = self.field_definition[u'type']

        if field_type == 'shortcode':
            expander = self.expand_shortcode
        elif field_type == 'text':
            expander = self.expand_text
        elif field_type == "magic text":
            expander = self.expand_magic_text

        expanded_text = expander(expansion_text)
        expanded_json[label] = expanded_text

        expanded_text = '%s: %s' % (label, expanded_text)

        return (expanded_text, expanded_json)

    def expand_text(expansion_text):
        return self.field_definition[u'label'] + " " expansion_text 
    def expand_shortcode(expansion_text):
        scodes = self.field_definition[u'shortcodes']
        newText = scodes[expansion_text]
        newText = self.field_definition[u'label'] + " " + newText        
        return newText
    def expand_magic_text(expansion_text):
        scodes = self.field_definition[u'shortcodes']
        newText = scodes[expansion_text]
        newText = self.field_definition[u'label'] + " " + newText        
        return newText
    def expand_magic_list(expansion_text):
        scodes = self.field_definition[u'shortcodes']
        newText = scodes[expansion_text]
        newText = self.field_definition[u'label'] + " " + newText        
        return newText
