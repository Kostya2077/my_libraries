from libraries.ContactFinder.ContactFinder import ContactFinder
from libraries.ContactFinder.Finders.PhoneFinder import PhoneFinder
from libraries.ContactFinder.Finders.EmailFinder import EmailFinder
from libraries.ContactFinder.Finders.TelegramFinder import TelegramFinder
from libraries.ContactFinder.Finders.LinkedinFinder import LinkedinFinder
from libraries.ContactFinder.Finders.GithubFinder import GithubFinder
from libraries.ContactFinder.Finders.ViberFinder import ViberFinder
from libraries.ContactFinder.Finders.FacebookFinder import FacebookFinder
from libraries.ContactFinder.Finders.WhatsappFinder import WhatsappFinder
from libraries.ContactFinder.Finders.IcqFinder import IcqFinder
from libraries.ContactFinder.Finders.SkypeFinder import SkypeFinder
from libraries.ContactFinder.Finders.VkontakteFinder import VkontakteFinder
from libraries.ContactFinder.Finders.ResumeFinder import ResumeFinder
from libraries.ContactFinder.Finders.BenahceFinder import BehanceFinder
from libraries.ContactFinder.Finders.TwitterFinder import TwitterFinder
from libraries.ContactFinder.Finders.YoutubeFinder import YoutubeFinder
from libraries.ContactFinder.Finders.CareerHabrFinder import CareerhabrFinder
from libraries.ContactFinder.Finders.DribbbleFinder import DribbbleFinder
from libraries.ContactFinder.Finders.FreelanceFinder import FreelanceFinder
from libraries.ContactFinder.Finders.HabrFinder import HabrFinder
from libraries.ContactFinder.Finders.InstagramFinder import InstagramFinder
from libraries.ContactFinder.Finders.QnahabrFinder import QnahabrFinder
from libraries.ContactFinder.Finders.StackoverflowFinder import StackoverflowFinder
from libraries.ContactFinder.Finders.GitlabFinder import GitlabFinder
from libraries.ContactFinder.Finders.Common.Constants import CONTACT_FORMAT, SEARCH_CONTACTS
import re



class TextContactFinder(ContactFinder):

    def __init__(self, data):
        super().__init__(data)
        self.data = self.__clear_data(data)

    def get_telephone(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return PhoneFinder().find(self.data, correct_format, search_contacts)

    def get_email(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return EmailFinder().find(self.data, correct_format, search_contacts)

    def get_telegram(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.LAX):
        return TelegramFinder().find(self.data, correct_format, search_contacts)

    def get_viber(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return ViberFinder().find(self.data, correct_format, search_contacts)

    def get_linkedin(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return LinkedinFinder().find(self.data, correct_format, search_contacts)

    def get_github(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return GithubFinder().find(self.data, correct_format, search_contacts)

    def get_facebook(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return FacebookFinder().find(self.data, correct_format, search_contacts)

    def get_whatsapp(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return WhatsappFinder().find(self.data, correct_format, search_contacts)

    def get_icq(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return IcqFinder().find(self.data, correct_format, search_contacts)

    def get_skype(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return SkypeFinder().find(self.data, correct_format, search_contacts)

    def get_vkontakte(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return VkontakteFinder().find(self.data, correct_format, search_contacts)

    def get_resume(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return ResumeFinder().find(self.data, correct_format, search_contacts)

    def get_habr(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return HabrFinder().find(self.data, correct_format, search_contacts)

    def get_dribbble(self,  correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return DribbbleFinder().find(self.data, correct_format, search_contacts)

    def get_instagram(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return InstagramFinder().find(self.data, correct_format, search_contacts)

    def get_behance(self,  correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return BehanceFinder().find(self.data, correct_format, search_contacts)

    def get_freelance(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return FreelanceFinder().find(self.data, correct_format, search_contacts)

    def get_qnahabr(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return QnahabrFinder().find(self.data, correct_format, search_contacts)

    def get_twitter(self,  correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return TwitterFinder().find(self.data, correct_format, search_contacts)

    def get_youtube(self,  correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return YoutubeFinder().find(self.data, correct_format, search_contacts)

    def get_careerhabr(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return CareerhabrFinder().find(self.data, correct_format, search_contacts)

    def get_stackoverflow(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return StackoverflowFinder().find(self.data, correct_format, search_contacts)

    def get_gitlab(self, correct_format = CONTACT_FORMAT.CORRECT, search_contacts = SEARCH_CONTACTS.STRICT):
        return GitlabFinder().find(self.data, correct_format, search_contacts)

    def __clear_data(self, data):
        try:
            copy_data = data
            for delete_long_word in re.findall('\S{300,}', copy_data):
                copy_data = copy_data.replace(delete_long_word, '')
            return copy_data
        except:
            return data