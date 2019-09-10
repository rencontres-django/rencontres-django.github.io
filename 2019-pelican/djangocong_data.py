from dataclasses import dataclass
from typing import Optional


@dataclass
class Sponsor:
    logo: str
    link: str = "#"
    name: str = ""


SPONSORS = [
    Sponsor(
        name="Hybird", link="https://hybird.org/", logo="images/friends/hybird.png"
    ),
    Sponsor(
        name="Isshub", link="https://www.isshub.io/", logo="images/friends/isshub.png"
    ),
    Sponsor(
        name="PeopleDoc",
        link="https://www.people-doc.fr/",
        logo="images/friends/peopledoc.png",
    ),
    Sponsor(
        name="Providenz",
        link="http://providenz.fr/",
        logo="images/friends/providenz.png",
    ),
    Sponsor(
        name="YourLabs",
        link="https://www.yourlabs.biz/",
        logo="images/friends/yourlabs.png",
    ),
    Sponsor(
        name="Evolix",
        link="https://evolix.com/",
        logo="images/friends/evolix.png",
    ),
]


DEFAULT_AVATAR = "https://avatars.githubusercontent.com/{}"


@dataclass
class Talk:
    title: str
    author: str
    description: str
    time: str
    avatar: Optional[str] = None
    # Social links
    home_page: Optional[str] = None
    github: Optional[str] = None
    twitter: Optional[str] = None
    linkedin: Optional[str] = None

    @property
    def image(self):
        return self.avatar or DEFAULT_AVATAR.format(self.github or "__TBD__")


TALKS = [
    Talk(
        author="Eliot Berriot",
        title="Tester son application django avec Factory-boy",
        time="Samedi 14 septembre",
        description="""Comment utiliser Factory-Boy pour générer très facilement des données pour tester son application
""",
    ),
    Talk(
        author="Lucien Deleu",
        title="Un CMS conçu pour la performance écologique",
        time="Samedi 14 septembre",
        description="""Les CMS sont parmis les types de site les plus demandés,
            souvent déployés pour de simples sites vitrines. Le compromis entre
            légèreté et personnalisation n'est pas simple. Avec ces compromis,
            la page d'accueil d'un site vitrine va contenir des centaines de requêtes,
            du javascript venant de tous les horizons, celui-là même qui vous permettra
            d'observer une animation de chargement.
            Nous avons travaillé sur une solution pour mettre fin à tout ça,
            pour le découvrir, venez voir notre présentation.""",
    ),
    Talk(
        author="Sarah Diot-Girard",
        time="Samedi 14 septembre",
        title="""De la polysémie en milieu hybride (ou comment faire communiquer
            data scientists et développeurs Web)""",
        description="""Du vocabulaire utilisé à la fois en Data Science et en
            développement Web, mais avec des sens radicalement différents. Et du
            coup les stand-ups deviennent comiques. Et les roadmaps embrouillées.""",
        github="SdgJlbl",
    ),
    Talk(
        author="Anouk HELLO",
        time="Samedi 14 septembre",
        title="""Streaming XLSX from Django to JS: the right way""",
        description="""Je parlerai de la problématique concernant la place de
            certaines chaînes traduites: dans l'application client ? Service par
            l'API ? Dans quels cas et contextes est-ce nécessaire ?
            Je parlerai de la solution permettant, via un "pipe" JavaScript natif,
            de streamer le flux HTTP directement dans un fichier sans passer par
            un objet en mémoire.""",
    ),
    Talk(
        author="Joachim Jablon",
        time="Samedi 14 septembre",
        title="""async def django()""",
        description="""DEP0009 : La proposition d’Andrew Godwin d’ajouter le support
            asynchrone à Python a été acceptée en Juillet. En quoi consiste-t-elle ?
            Que va-t-elle changer ? Et comment participer à la transition ?""",
        github="ewjoachim",
        twitter="ewjoachim",
        linkedin="ewjoachim",
        home_page="https://ewjoach.im",
    ),
    Talk(
        author="Jérémy Lecour & Grégory Colpart",
        time="Samedi 14 septembre",
        title="""Ansible pour automatiser le déploiement et la configuration""",
        description="""On posera les concepts de base d'Ansible et on présentera différents cas d'usage possibles pour une équipe de dev/devops, le plus possible sous forme de démo afin de rendre ça dynamique et pratique.""",
    ),
    Talk(
        author="Damien Marié",
        time="Samedi 14 septembre",
        title="""Et si Django tournait dans votre navigateur, serait-ce la fin de
            Javascript ?""",
        description="""Description à venir""",
    ),
Talk(
    author="Thomas Mignot",
    title="Data binding et components isomorphique avec Django",
    time="Samedi 14 septembre",
    description="""Comment synchroniser des clients web, ne plus écrire une ligne de HTML ni recharger une page grace à Ryzom
""",
),    
    Talk(
        author="Mehdi Raddadi - Eclar",
        time="Samedi 14 septembre",
        title="""Déployer Django avec compose""",
        description="""Explication de la construction d'un squelette de projet déployé
            avec docker-compose ainsi que le processus de développement associé.
            Tests en local et sur gitlab-ci puis déploiement.""",
    ),
    Talk(
        author="Arthur Vuillard et Samira Rabaâoui",
        time="Samedi 14 septembre",
        title="""Surveiller le bon fonctionnement de son appli Django""",
        description="""Nous développons des applis web avec Django, mais pas
            seulement : nous les installons sur un serveur, et devons les faire évoluer
            au fil du temps.
            Dans cette présentation, nous allons montrer comment automatiser la
            surveillance du bon fonctionnement d'une appli Django, et comment être
            alerté·e·s lors d'une défaillance. Nous présenterons quels sont les
            éléments à surveiller et comment le faire sans se prendre la tête !""",
    ),
    Talk(
        author="Laurent Paoletti",
        time="Samedi 14 septembre",
        title="""Des équipes et des briques: introduction à la méthode Lego Serious Play""",
        description="""À la fin des années 90, les chercheurs du centre de développement 
        de Lego ont eu l'idée d'utiliser leurs propres briques pour favoriser la 
        créativité et favoriser une démarche d'intelligence collective. 
        Cette méthode alors émergente a permis à Lego de repenser totalement sa stratégie,
         et de devenir un des premiers fabricants de jeu au monde.""",
        github="providenz",
        twitter="providenz",
        linkedin="laurentpaoletti",
        home_page="https://providenz.fr",
    ),
]

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
