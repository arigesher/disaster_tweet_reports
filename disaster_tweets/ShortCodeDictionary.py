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

split_re = re.compile('/')

class ShortCodeDictionary(Decorator):

    def __init__(self, json_dictionary):
        Decorator.__init__(self)
        self.json_dictionary = json_dictionary
        self.alphabet = json.loads(json_dictionary)
        if not self.alphabet['fields']
        #TODO

    def decorate(self, trimmed_tweet, original_tweet):
        text = tweet[u'pretty_text']
        data = split_re.split(data)
        fields = self.alphabet[]
        expansion = []
        #TODO


    def output_cheat_sheet(path):
        raise NotImplementedError()