from libraries.regex_constructor.regex_constructor_interface import RegexConstructorInterface
from libraries.regex_constructor.constants import *
import re


class RegexConstructor(RegexConstructorInterface):


    def create_regex(self, text, regex_type=REGEXTYPE.STRICT):
        if regex_type:
            self.__regex_str = self.__create_strict_regex(text)
        else:
            self.__regex_str = self.__create_lax_regex(text)
        self.__regex_compiler = re.compile(self.__regex_str)
        return self.__regex_compiler

    @property
    def re_str(self):
        return self.__regex_str

    @property
    def re(self):
        return self.__regex_compiler


    def __create_strict_regex(self, text):
        result = ''
        if isinstance(text, str):
            for symbol in text:
                if symbol in REGEXSYMBOLS.SYMBOLS_ALPHABET:
                    result += '['+REGEXSYMBOLS.SYMBOLS_ALPHABET[symbol] + ']'
                elif symbol in REGEXSYMBOLS.SYMBOLS_STRICT:
                    result += '['+REGEXSYMBOLS.SYMBOLS_STRICT[symbol] + ']'
                else:
                    result += '['+'\\'+symbol+']'
        elif isinstance(text, list):
            for word in sorted(text)[::-1]:
                for symbol in word:
                    if symbol in REGEXSYMBOLS.SYMBOLS_ALPHABET:
                        result += '[' + REGEXSYMBOLS.SYMBOLS_ALPHABET[symbol] + ']'
                    elif symbol in REGEXSYMBOLS.SYMBOLS_STRICT:
                        result += '[' + REGEXSYMBOLS.SYMBOLS_STRICT[symbol] + ']'
                    else:
                        result += '[' + '\\' + symbol + ']'
                result += '|'
            result = result.rstrip('|')
        return result


    def __create_lax_regex(self, text):
        result = ''
        if isinstance(text, str):
            for symbol in text:
                if symbol in REGEXSYMBOLS.SYMBOLS_ALPHABET:
                    result += '['+REGEXSYMBOLS.SYMBOLS_ALPHABET[symbol] + ']'
                elif symbol in REGEXSYMBOLS.SYMBOLS_LAX:
                    result += '['+REGEXSYMBOLS.SYMBOLS_LAX[symbol]+']'
                else:
                    result += '[ ]?'+REGEXSYMBOLS.SYMBOLS_LAX['UNK']+'[ ]?'
        elif isinstance(text, list):
            for word in sorted(text)[::-1]:
                for symbol in word:
                    if symbol in REGEXSYMBOLS.SYMBOLS_ALPHABET:
                        result += '[' + REGEXSYMBOLS.SYMBOLS_ALPHABET[symbol] + ']'
                    elif symbol in REGEXSYMBOLS.SYMBOLS_LAX:
                        result += '[' + REGEXSYMBOLS.SYMBOLS_LAX[symbol] + ']'
                    else:
                        result += '[ ]?' + REGEXSYMBOLS.SYMBOLS_LAX['UNK'] + '[ ]?'
                result += '|'
            result = result.rstrip('|')
        return result


