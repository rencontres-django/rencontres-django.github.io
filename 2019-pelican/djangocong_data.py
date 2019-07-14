from dataclasses import dataclass
from typing import Optional


@dataclass
class Sponsor:
    logo: str
    link: str = "#"


SPONSORS = []


@dataclass
class Talk:
    title: str
    author: str
    description: str
    # Social links
    home_page: Optional[str] = None
    github: Optional[str] = None
    twitter: Optional[str] = None
    linkedin: Optional[str] = None


TALKS = []

CONTACT_EMAIL = "j-mad@j-mad.com"


@dataclass
class PreviousEvent:
    link: str
    title: str


PREVIOUS_EVENTS = [
    PreviousEvent(link="/2018/", title="Lille 2018"),
    PreviousEvent(link="/2017/", title="Toulon 2017"),
    PreviousEvent(link="/2016/", title="Rennes 2016"),
    PreviousEvent(link="/2015/", title="Clermont-Ferrand 2015"),
    PreviousEvent(link="/2013/", title="Belfort 2013"),
    PreviousEvent(link="/2012/tolosa/", title="Toulouse 2012"),
    PreviousEvent(link="/2012/", title="Montpellier 2012"),
    PreviousEvent(link="/2011/", title="Marseille 2011"),
    PreviousEvent(link="/2010/", title="Marseille 2010"),
]


@dataclass
class Link:
    link: str
    title: str
    new_tab: bool = False


LINKS = [
    Link(link="/2019/code-de-conduite", title="Code de conduite"),
    Link(link="/2019/mentions-legales", title="Mentions légales"),
    Link(
        link="https://www.django-fr.org/", new_tab=True, title="Association django-fr"
    ),
    Link(
        link="https://twitter.com/djangocong",
        new_tab=True,
        title="DjangoCong sur twitter",
    ),
    Link(link="https://djangoproject.com", new_tab=True, title="Django"),
    Link(link="https://afpy.org", new_tab=True, title="Afpy"),
]
