from check_word import check_word


class Table:
    def __init__(self):
        self.prefixes = ['']
        self.suffixes = ['']
        self.set_suffixes = set()
        self.extended_prefixes = dict()
        self.eq_classes = set()
        self.string_values = dict()  # table, key - prefix, value - string
        self.pointer = 0  # point to prefix that has not been extended with L and R yet

        self.string_values[''] = self.check_word('ε')

    def get_table(self):
        main_prefixes = ' '.join(self.prefixes)
        main_prefixes = 'ε' + main_prefixes
        non_main_prefixes = ' '.join(self.extended_prefixes.keys())
        non_main_prefixes = 'ε' + non_main_prefixes
        suffixes = ' '.join(self.suffixes)
        suffixes = 'ε' + suffixes
        table = ''
        for prefix in self.prefixes + list(self.extended_prefixes.keys()):
            table += self.string_values[prefix]
        table = table.strip()
        d = {'main_prefixes': main_prefixes, 'non_main_prefixes': non_main_prefixes,
             'suffixes': suffixes, 'table': table}
        return d

    def check_word(self, word):
        return check_word(word) + ' '

    def closure(self):
        extended_copy = list(self.extended_prefixes.keys()).copy()
        for prefix in extended_copy:
            if self.string_values[prefix] not in self.eq_classes:
                self.prefixes.append(prefix)
                del self.extended_prefixes[prefix]
        self.extend()

    def add_contr_example(self, word):
        index = len(self.suffixes)
        self.eq_classes.clear()
        for i in range(len(word)):
            suffix = word[i:]
            if suffix in self.set_suffixes:
                break
            self.suffixes.append(suffix)
            self.set_suffixes.add(suffix)

        for prefix in self.prefixes:
            self.update_membership(prefix, self.suffixes[index:])
            self.eq_classes.add(self.string_values[prefix])
        for prefix in self.extended_prefixes.keys():
            self.update_membership(prefix, self.suffixes[index:])

        self.closure()

    def extend(self):
        while self.pointer < len(self.prefixes):
            prefix = self.prefixes[self.pointer]
            for way in 'LR':
                string = self.fill_membership(prefix + way)
                self.closure_by_string(string, prefix + way)
            self.pointer += 1

    def closure_by_string(self, string, prefix):
        if string not in self.eq_classes:
            # move to main prefixes
            self.prefixes.append(prefix)
            self.eq_classes.add(string)
        else:
            self.extended_prefixes[prefix] = ''

    def fill_membership(self, prefix):
        string = ''
        for suffix in self.suffixes:
            string += self.check_word(prefix + suffix)
        self.string_values[prefix] = string
        return string

    def update_membership(self, prefix, suffixes):
        string = ''
        for suffix in suffixes:
            string += self.check_word(prefix + suffix)
        self.string_values[prefix] += string
