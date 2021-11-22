
 
# регулярные выражения
# регулярные выражения
class REGEX_CONTACT:
    __dig_lett = '[^ `~!@#$%^&*()_+}{\":?><,./\';\[\]=№\\-\n\t\v\r\f\a\b]'
    # TELEPHONE = '(\d{10,14})|([(]?[ ]?[+]?[ ]?\d{1,4}[ ]?[-]?[ ]?[(]?[ ]?[-]?[ ]?\d{2,4}[ ]?[)]?[ ]?[-]?[ ]?\d{1,3}[ ]?[-]?[ ]?\d{1,3}[ ]?[-]?[ ]?\d{1,3}[ ]?[-]?[ ]?\d{1,3})'
    TELEPHONE = '([+]?[ ]?(7|8)[ ]?[-]?[ ]?[(]?[ ]?\d{3}[ ]?[)]?[ ]?[-]?[ ]?\d{3}[ ]?[-]?[ ]?\d{2}[ ]?[-]?[ ]?\d{2})|([+]?[ ]?380[ ]?[-]?[ ]?[(]?\d{2}[)]?[ ]?[-]?[ ]?\d{3}[ ]?[-]?[ ]?\d{2}[ ]?[-]?[ ]?\d{2})'
    EMAIL = '(\"[^\"]*\"|[^ /.@(),:;<>{}\[\]\"\n\t\v\r\f\a\b]+[^ /@(),:;<>{}\[\]\"`\n\t\v\r\f\a\b]*[^ /.@(),:;<>{}\[\]\"\n\t\v\r\f\a\b]+|[^ /.@(),:;<>{}\[\]\"\n\t\v\r\f\a\b]+)(@)(' + __dig_lett + '+)(' + __dig_lett + '*[-]*' + __dig_lett + '+|' + __dig_lett + '+)*(\.' + __dig_lett + '+)*' \
            '|(http[s]://)(cloud[.]mail)([a-z0-9A-Z./=_-]+)'
    SKYPE_LINK = '(http[s]?://)?([a-zA-Z0-9]+)([.][a-zA-Z0-9]+|[/][a-zA-Z0-9]+)+'
    SKYPE_USERNAME = '[(]?[ ]?[+]?[ ]?\d{1,4}[ ]?[-]?[ ]?[(]?[ ]?[-]?[ ]?\d{2,4}[ ]?[)]?[ ]?[-]?[ ]?\d{1,3}[ ]?[-]?[ ]?\d{1,3}[ ]?[-]?[ ]?\d{1,3}[ ]?[-]?[ ]?\d{1,3}|([a-z0-9._@-]+)'
    SKYPE_EMAIL = EMAIL
    FACEBOOK_LINK = '(http[s]?://)?(www[.])?(facebook[.]com/|fb[.]com/)([a-zA-Z0-9]+)(\.[a-zA-Z0-9.]+[a-zA-Z0-9])*'
    FACEBOOK_USERNAME = '([a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)*|([a-zA-Z0-9]+)([_][a-zA-Z0-9]+|[-][a-zA-Z0-9])*'
    GITHUB_LINK = '(http[s]?://)?([a-z0-9]+[.])*(github[.]com)([/][a-z0-9A-Z_=?-]+|[.][a-z0-9A-Z_=?-]+)+'
    GITHUB_USERNAME = '[a-zA-Z0-9-]+'
    ICQ = '\d+[ ]?[-]?[ ]?\d+[ ]?[-]?[ ]?\d+'
    LINKEDIN_LINK = '(http[s]?://)?([a-zA-Z0-9]+[.])*(linkedin)([.][a-z0-9]+)*(/[a-zA-Z0-9]+)([/.-]?[a-zA-Z0-9]+[/]?)*'
    LINKEDIN_EMAIL = EMAIL
    LINKEDIN_USERNAME = '([a-zA-Z0-9]+)([-]?[a-zA-Z0-9]+)*'
    TELEGRAM_LINK = '([@]+[ ]*)?(http[s]?://)?(t[.]me|telegram[.]me)([a-z0-9A-Z_/.]+)'
    TELEGRAM_NUMBER = '([@][ ]?)?([+]?[ ]?(7|8)[ ]?[-]?[ ]?[(]?[ ]?\d{3}[ ]?[)]?[ ]?[-]?[ ]?\d{3}[ ]?[-]?[ ]?\d{2}[ ]?[-]?[ ]?\d{2})|([@][ ]?)?([+]?[ ]?380[ ]?[-]?[ ]?[(]?\d{2}[)]?[ ]?[-]?[ ]?\d{3}[ ]?[-]?[ ]?\d{2}[ ]?[-]?[ ]?\d{2})'
    TELEGRAM_USERNAME = '([@]+[ ]?)?([a-zA-Z0-9]+)([_][a-zA-Z0-9]+)*'
    WHATSAPP = TELEPHONE
    VIBER = TELEPHONE
    VKONTAKTE_LINK = '(http[s]?://)?(vk[.]|vkontakte[.])(ru/|com/)([a-zA-Z0-9]+)([_.]?[a-zA-Z0-9]+)*'
    VKONTAKTE_USERNAME = '([a-zA-Z0-9]+)([._-]?[a-zA-Z0-9]+)*'
    RESUME_LINK = '(http[s]?://)?([/]?resume[s]?[.]io/)([a-z0-9A-Z_?%.=-]+|[/][a-zA-Z0-9]+)+'
    YOUTUBE_LINK = '(http[s]?://)?([a-z0-9A-Z.]+)?(youtu[.]be|youtube[.]com)([a-z0-9A-Z.?=_/&%$#:@-]+)'
    HH_LINK = '(http[s]?://)?([a-z0-9A-Z./?=-]+)?(hh[.]ru)([a-z0-9A-Z.?=_/&%$#:@-]+)'
    CAREER_HABR_LINK = '(http[s]://)?(career.habr.com)([.][a-z0-9A-Z?=_&%$#:@-]+|[/][a-z0-9A-Z?=_&%$#:@-]+)+|(/resumes[?]skills%)(\S+)'
    HABR_LINK = '(http[s]?://)?([a-z0-9A-Z.]+)?(habr[.])(ru|com)([.][a-z0-9A-Z?=_&%$#:@-]+|[/][a-z0-9A-Z?=_&%$#:@-]+)+'
    STACKOVERFLOW_LINK = '(http[s]?://)?([a-z0-9A-Z.]+)?(stackoverflow[.]com)([.][a-z0-9A-Z?=_&%$#:@-]+|[/][a-z0-9A-Z?=_&%$#:@-]+)+'
    INSTAGRAM_LINK = '(http[s]?://)?([a-z0-9A-Z.]+)?(instagram[.]com)([.][a-z0-9A-Z?=_&%$#:@-]+|[/][a-z0-9A-Z?=_&%$#:@-]+)+'
    FREELANCE_LINK = '(http[s]?://)?([a-z0-9A-Z.]+)?(free-lance[.]ru|fl[.]ru)([.][a-z0-9A-Z?=_&%$#:@-]+|[/][a-z0-9A-Z?=_&%$#:@-]+)+'
    BEHANCE_LINK = '(http[s]?://)?([a-z0-9A-Z.]+)?(behance[.]com)([.][a-z0-9A-Z?=_&%$#:@-]+|[/][a-z0-9A-Z?=_&%$#:@-]+)+'
    TWITTER_LINK = '(http[s]?://)?([a-z0-9A-Z.]+)?(twitter[.]com)([.][a-z0-9A-Z?=_&%$#:@-]+|[/][a-z0-9A-Z?=_&%$#:@-]+)+'
    QNAHABR_LINK = '(http[s]?://)?([a-z0-9A-Z.]+)?(qna[.]habr[.]com)([.][a-z0-9A-Z?=_&%$#:@-]+|[/][a-z0-9A-Z?=_&%$#:@-]+)+'
    DRIBBBLE_LINK = '(http[s]?://)?([a-z0-9A-Z.]+)?(dribbble[.]com)([.][a-z0-9A-Z?=_&%$#:@-]+|[/][a-z0-9A-Z?=_&%$#:@-]+)+'
    GITLAB_LINK = '(http[s]?://)?([a-z0-9A-Z.]+)?(gitlab[.]com)([a-z0-9A-Z/._=?-]+)'



class REGEX_KEYWORD:
    EMAIL = '[eEgG]?[-]?[mM][aA][iI][lL]|[пП][оО][чЧ][тТ][аАеЕуУыЫ]'
    GITHUB = '[gG][iI][tT][hH][uU][bB]|[гГ][иИ][тТ][хХ][аА][бБ][еЕуУаА]?'
    FACEBOOK = '[fF][aA][cC][eE][bB][oO][oO][kK]|[фФ][еЕ][йЙ][сС][бБ][уУ][кК][уУеЕаА]?'
    ICQ = '[iI][cC][qQ]|[аА][сС][ьЬ][кК][аАеЕуУиИ]?'
    LINKEDIN = '[lL][iI][nN][kK][eE][dD][iI][nN]|[лЛ][иИ][нН][кК][еЕ][дД][иИ]?[нН]?[уУаА]?'
    TELEPHONE = '[tT][eE][lL][eE][pP][hH][oO][nN][eE]|[pP][hH][oO][nN][eE]|[mM][oO][bB][iI][lL][eE]|[nN][uU][mM][bB][eE][rR]|[тТ][еЕ][лЛ][еЕ][фФ][оО][нН][уУаА]?|[сС][оО][тТ][оО][вВ][ыЫ][йЙ]|[нН][оО][мМ][еЕ][рР][уУаА]?'
    SKYPE = '[сС][кК][аА][йЙ][пП][уУеЕаА]?|[sS][kK][yY][pP][eE]'
    TELEGRAM = '[tT][eE][lL][eE][gG][rR][aA][mM]+|[tT][eE][lL][eE][gG][aA]|[тТ][еЕ][лЛ][еЕ][гГ][аА]|[тТ][еЕ][лЛ][еЕ][гГ][рР][аА][мМ][мМ]?[уУаАеЕ]?|[тТ][еЕ][лЛ][еЕ][гГ][рР][аА][мМ][уУаАеЕ]?'
    WHATSAPP = '[wW][hH][aA][tT][sS][\']?[ ]?[aA][pP][pP]?|[wW][hH][aA][tT][sS][\']?[ ]?[uU][pP][pP]?|[вВ][аА][тТ][сС][аА][пП][уУаА]?|[вВ][оО][тТ][сС][аА][пП][уУаА]?'
    VKONTAKTE = '[вВ][ ]?[кК][оО][нН][тТ][аА][кК][тТ][еЕ]|[vV][ ]?[kK][oO][nN][tT][aA][kK][tT][eE]|[vV][kK]|[вВ][кК]'
    VIBER = '[vV][iI][bB][eE][rR]|[вВ][аА][йЙ][бБ][еЕ][рР][уУаА]?'
    YOUTUBE = '[yY][oO][uU][tT][uU][bB][eE]|[юЮ][тТ][уУ][бБ][уУеЕаА]?'
    HABR = '[hH][aA][bB][rR]|[cC][aA][rR][eE][eE][rR][ ]?[hH][aA][bB][rR]|[хХ][аА][бБ][рР][еЕуУаА]?|[кК][аА][рР][ьЬ][еЕ][рР][ ]?[хХ][аА][бБ][рР][еЕуУаА]?'
    RESUME = '[rR][eE][sS][uU][mM][eE]|[рР][еЕ][зЗ][юЮ][мМ][еЕэЭ]'
    STACKOVERFLOW = '[sS][tT][aA][cC][kK][oO][vV][eE][rR][fF][lL][oO][wW]|[сС][тТ][еЕ][кК][оО][вВ][еЕ][рР][фФ][лЛ][оО][уУ]'
    INSTAGRAM = '[iI][nN][sS][tT][aA][gG][rR][aA][mM]|[иИ][нН][сС][тТ][аА][гГ][рР][аА][мМ][еЕуУаАыЫ]?'
    FREELANCE = '[fF][rR][eE][eE][lL][aA][nN][cC][eE]|[фФ][рР][иИ][лЛ][аА][нН][сС][еЕуУыЫаА]?'
    BEHANCE = '[bB][eE][hH][aA][nN][cC][eE]|[бБ][иИ][хХ][аэЭ][нН][сС][еЕаАыЫуУ]?'
    TWITTER = '[tT][wW][iI][tT][tT][eE][rR]|[тТ][вВ][иИ][тТ]{1,2}[еЕ][рР][еЕуУыЫаА]?'
    QNAHABR = '[qQ][nN][aA][hH][aA][bB][rR]|[кК][ъЪ]?[юЮ][нН][аА][хХ][аА][бБ][рР][еЕыЫаАуУ]?'
    DRIBBBLE = '[dD][rR][iI][bB]{1,3}[lL][eE]|[дД][рР][иИ][бБ]{1,3}[лЛ][ееуУаАыЫ]?'
    GITLAB = '[gG][iI][tT][lL][aA][bB]|[гГ][иИ][тТ][лЛ][аА][бБ][еЕуУыЫаА]?'


class FIND:
    TELEPHONE = REGEX_CONTACT.TELEPHONE
    EMAIL = REGEX_CONTACT.EMAIL
    SKYPE_LINK = REGEX_CONTACT.SKYPE_LINK
    SKYPE_USERNAME = REGEX_CONTACT.SKYPE_USERNAME
    SKYPE_EMAIL = REGEX_CONTACT.SKYPE_EMAIL
    FACEBOOK_USERNAME = REGEX_CONTACT.FACEBOOK_USERNAME
    FACEBOOK_LINK = REGEX_CONTACT.FACEBOOK_LINK
    GITHUB_LINK = REGEX_CONTACT.GITHUB_LINK
    GITHUB_USERNAME = REGEX_CONTACT.GITHUB_USERNAME
    ICQ = REGEX_CONTACT.ICQ
    LINKEDIN_LINK = REGEX_CONTACT.LINKEDIN_LINK
    LINKEDIN_EMAIL = REGEX_CONTACT.LINKEDIN_EMAIL
    LINKEDIN_USERNAME = REGEX_CONTACT.LINKEDIN_USERNAME
    TELEGRAM_LINK = REGEX_CONTACT.TELEGRAM_LINK
    TELEGRAM_NUMBER = REGEX_CONTACT.TELEGRAM_NUMBER
    TELEGRAM_USERNAME = REGEX_CONTACT.TELEGRAM_USERNAME
    WHATSAPP = REGEX_CONTACT.WHATSAPP
    VIBER = REGEX_CONTACT.VIBER
    VKONTAKTE_LINK = REGEX_CONTACT.VKONTAKTE_LINK
    VKONTAKTE_USERNAME = REGEX_CONTACT.VKONTAKTE_USERNAME
    RESUME_LINK = REGEX_CONTACT.RESUME_LINK
    YOUTUBE_LINK = REGEX_CONTACT.YOUTUBE_LINK
    CAREER_HABR_LINK = REGEX_CONTACT.CAREER_HABR_LINK
    HABR_LINK = REGEX_CONTACT.HABR_LINK
    STACKOVERFLOW_LINK = REGEX_CONTACT.STACKOVERFLOW_LINK
    INSTAGRAM_LINK = REGEX_CONTACT.INSTAGRAM_LINK
    FREELANCE_LINK = REGEX_CONTACT.FREELANCE_LINK
    BEHANCE_LINK = REGEX_CONTACT.BEHANCE_LINK
    TWITTER_LINK = REGEX_CONTACT.TWITTER_LINK
    QNAHABR_LINK = REGEX_CONTACT.QNAHABR_LINK
    DRIBBBLE_LINK = REGEX_CONTACT.DRIBBBLE_LINK
    GITLAB_LINK = REGEX_CONTACT.GITLAB_LINK


    KEYWORD_GITHUB = REGEX_KEYWORD.GITHUB
    KEYWORD_VKONTAKTE = REGEX_KEYWORD.VKONTAKTE
    KEYWORD_ICQ = REGEX_KEYWORD.ICQ
    KEYWORD_FACEBOOK = REGEX_KEYWORD.FACEBOOK
    KEYWORD_VIBER = REGEX_KEYWORD.VIBER
    KEYWORD_WHATSAPP = REGEX_KEYWORD.WHATSAPP
    KEYWORD_TELEGRAM = REGEX_KEYWORD.TELEGRAM
    KEYWORD_SKYPE = REGEX_KEYWORD.SKYPE
    KEYWORD_TELEPHONE = REGEX_KEYWORD.TELEPHONE
    KEYWORD_LINKEDIN = REGEX_KEYWORD.LINKEDIN
    KEYWORD_HABR = REGEX_KEYWORD.HABR
    KEYWORD_YOUTUBE = REGEX_KEYWORD.YOUTUBE
    KEYWORD_RESUME = REGEX_KEYWORD.RESUME
    KEYWORD_STACKOVERFLOW = REGEX_KEYWORD.STACKOVERFLOW
    KEYWORD_INSTAGRAM = REGEX_KEYWORD.INSTAGRAM
    KEYWORD_BEHANCE = REGEX_KEYWORD.BEHANCE
    KEYWORD_FREELANCE = REGEX_KEYWORD.FREELANCE
    KEYWORD_TWITTER = REGEX_KEYWORD.TWITTER
    KEYWORD_DRIBBBLE = REGEX_KEYWORD.DRIBBBLE
    KEYWORD_QNAHABR = REGEX_KEYWORD.QNAHABR


class WORD_POSITION:
    BEFORE = 'before'
    AFTER = 'after'
    NONE = ''


class ERROR:
    KEYWORDS = ['viber', 'telegram', 'vibr', 'telega', 'skype', 'linkedin', 'icq',
               'whatsapp', 'whats app', 'gmail', 'mail', 'telegram', 'join',
               'skype', 'mobile', 'cell', 'telegram', 'yahoo', 'telephone',
               'whatsupp', 'whatsapp', 'whats', 'facebook', 'github', 'www', 'instagram',
               'habr', 'viber', 'twitter', 'site', 'jabber', 'live_messenger',
               'google_talk', 'mail_ru_agent', 'im_online', 'google_plus', 'hubr_qna',
               'stackoverflow', 'livejournal', 'wechat', 'freelance', 'bitbucket', 'dribbble',
               'behance', 'quora', 'moikrug', 'rambler', 'career_habr', 'address', 'youtube',
               'tumblr', 'google', 'https', 'http', 'vkontakte', 'slack', 'telephone']


class VALIDITY_LENGTH:
    # длина контакта от минимума до максимума
    # TELEPHONE = [9, 14] todo для всех номеров
    TELEPHONE = [10,12]
    LINK = [10, 256]
    USERNAME = [3,80]
    ICQ = [3,20]
    # длина юзернейма(минимум, максимум) и домена(минимум,максимум)
    EMAIL = [[1,64], [1,255]]


class KIND_CONTACT:
    TELEPHONE = 'telephone'
    EMAIL = 'email'
    LINK = 'link'
    USERNAME = 'username'
    ICQ = 'icq'
    NONE = ''


class CONTACT_FORMAT:
    CORRECT = 1
    INCORRECT = 0


class SEARCH_CONTACTS:
    STRICT = 0
    LAX = 1


