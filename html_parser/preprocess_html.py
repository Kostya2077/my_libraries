import re
from regex_requests.regex_requests import RegexRequests
import pickle
from os.path import abspath, dirname
from lxml import etree
import time
PATH_2_HTMl_TAGS = dirname(abspath(__file__)) + '/html_trie'


class TrieRegexPattern(object):


    def __init__(self):
        self.html_trie = dict()


    def add(self, word):
        ref = self.html_trie
        for char in word:
            ref[char] = char in ref and ref[char] or {}
            ref = ref[char]
        ref[''] = 1


    def _pattern(self, data):
        if "" in data and len(data.keys()) == 1:
            return None

        parent = []
        child = []
        leaves = 0
        for char in data.keys():
            if data[char] != 1:
                recurse = self._pattern(data[char])
                if recurse:
                    parent.append(re.escape(char)+recurse)
                else:
                    child.append(re.escape(char))
            else:
                leaves = 1

        if len(child) > 0:
            if len(child) == 1:
                parent.append(child[0])
            else:
                parent.append('[' + ''.join(child) + ']')
        if len(parent) == 1:
            result = parent[0]
        else:
            result = "(?:" + "|".join(parent) + ")"

        if leaves:
            if len(parent) == 0:
                result += "?"
            else:
                result = "(?:" + result + ")?"
        return result


    @property
    def pattern(self):
        return self._pattern(self.html_trie)

    @pattern.setter
    def pattern(self):
        return self.pattern()


def load_html_tags():
    with open(PATH_2_HTMl_TAGS, 'rb') as f:
        return pickle.load(f)


def save_html_tags():
    with open(PATH_2_HTMl_TAGS, 'wb') as f:
        pickle.dump(HTML_TAGS, f)


def __update_html_tags(html_tree, html_text, visited):
    tag = html_tree.tag
    if tag not in visited:
        visited[tag] = 0
        tag = re.search("<" + tag + "[ >]", html_text, flags=re.I).group()
        close_tag = re.search('</' + tag[1:-1] + ">", html_text)
        if close_tag:
            HTML_TAGS[tag[:-1]] = 0
            HTML_TAGS[close_tag.group()[:-1]] = 1
        else:
            HTML_TAGS[tag[:-1]] = 2

    for i in html_tree:
        __update_html_tags(i, html_text, visited)


def update_html_tags(html_text):
    global HTML_TAGS
    parser = etree.HTMLParser(recover=True, remove_comments=True, remove_pis=True, remove_blank_text=True)
    html_tree = etree.HTML(html_text, parser)
    __update_html_tags(html_tree, html_text, {})
    save_html_tags()
    HTML_TAGS = load_html_tags()


def get_pattern(data: str or list = None):
    try:
        trie = TrieRegexPattern()
        if data:
            if isinstance(data, str):
                data = data.split()
            for element in data:
                trie.add(element)
        else:
            for element in load_html_tags():
                trie.add(element)
        return trie.pattern
    except:
        return ''


def lower_bound_search(target, array):
    l, r = 0, len(array)-1
    while l <= r:
        mid = l + (r - l) // 2
        if array[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l


def upper_bound_search(target, array):
    l, r = 0, len(array)-1
    while l <= r:
        mid = l + (r - l) // 2
        if array[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return l


try:
    HTML_TAGS = load_html_tags()
except:
    HTML_TAGS = {}
TAG_FINDER = re.compile(get_pattern()+"[ >]")
COMMENTS_FINDER = re.compile("<!--|-->").finditer





class HTMLParser(object):


    def __init__(self, html_text, remove_comments=False):
        self.html_text = html_text
        if remove_comments:
            self.__remove_comments()
        self.__process_text()


    def __remove_comments(self):
        indexes = []
        comment = 0
        for it in COMMENTS_FINDER(self.html_text):
            if it.group() == "<!--":
                if not comment:
                    comment = 1
                    indexes.append(it.start())
                else:
                    indexes[-1] == it.start()
            elif comment:
                comment = 0
        for ind in range(len(indexes)-1, -1, 2):
            self.html_text = self.html_text.replace(self.html_text[indexes[ind - 1]:indexes[ind]], '')


    def __process_text(self):
        depth = 0
        self.__tree = {}
        self.__indexes = []
        for it in TAG_FINDER.finditer(self.html_text):
            tag = it.group()
            tag=tag[:-1]
            if HTML_TAGS[tag] == 0:
                try:
                    try:
                        self.__tree[depth][tag].append(it.start())
                    except:
                        self.__tree[depth][tag] = [it.start()]
                except:
                    self.__tree[depth] = {tag: [it.start()]}
                self.__indexes.append(it.start())
                depth += 1
            elif HTML_TAGS[tag] == 1:
                depth -= 1
                try:
                    try:
                        self.__tree[depth][tag].append(it.end())
                    except:
                        self.__tree[depth][tag] = [it.end()]
                except:
                    self.__tree[depth] = {tag: [it.end()]}
            else:
                try:
                    try:
                        self.__tree[depth][tag].append(it.start())
                    except:
                        self.__tree[depth][tag] = [it.start()]
                except:
                    self.__tree[depth] = {tag: [it.start()]}
                self.__indexes.append(it.start())


    def full_xpath(self, xpath):
        xpath = xpath.split('/')[1:]
        tag_index = lambda tag: int(re.findall('\d+', tag)[-1])-1 if ']' == tag[-1] else 0
        tag_name = lambda tag: '<' + (re.search("[^\[]+", tag).group() if re.search("[^\[]+", tag) else tag)
        start = -1
        end = len(self.html_text)
        for depth, tag in enumerate(xpath):
            ind = tag_index(tag)
            tag = tag_name(tag)
            try:
                ind_ = upper_bound_search(start, self.__tree[depth][tag]) + ind
                start = self.__tree[depth][tag][ind_]
                if HTML_TAGS[tag] == 0:
                    end = self.__tree[depth]["</"+tag[1:]][ind_]
                elif HTML_TAGS[tag] == 2:
                    end = start + re.search(">", self.html_text[start:]).end()
            except Exception as ex:
                raise ex
        return HTMLParser(self.html_text[start:end])


    def get_html_text(self):
        return self.html_text


    def find_element_by(self, key, value):
        index_tag = upper_bound_search(re.search(key+'="'+value+'"', self.html_text).start(), self.__indexes)-1
        tag = TAG_FINDER.match(self.html_text[self.__indexes[index_tag]:]).group()[:-1]
        if HTML_TAGS[tag] == 2:
            return HTMLParser(self.html_text[self.__indexes[index_tag]:self.__indexes[index_tag+1]])
        target = self.__indexes[index_tag]
        for depth in self.__tree:
            if tag in self.__tree[depth]:
                start = lower_bound_search(target, self.__tree[depth][tag])
                if self.__tree[depth][tag][start] == target:
                    return HTMLParser(self.html_text[target:self.__tree[depth]["</"+tag[1:]][start]])

        return None




