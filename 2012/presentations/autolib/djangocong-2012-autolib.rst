========================================
Autolib’, un SI d'entreprise avec Django
========================================

**Service, architecture, organisation et outils**

.. image:: img/avenue-foch.jpg
    :width: 72%

----

Le service Autolib’
===================

Location de véhicules électriques :

- de courte durée
- en libre service 24/7
- en trace directe

.. image:: img/autolib-et-borne-abonnement.jpg

Presenter Notes
===============

Et si nous utilisions Django pour concevoir le SI d'entreprise, c'est le pari de
Polyconseil sur le projet Autolib’. Je vais lors de cette présentation vous
présenter les défis techniques du service, l'architecture que nous avons mise en
place, l'organisation et les outils pour y parvenir


----

Le service Autolib’
===================

.. image:: img/suivez-le-guide_1_jeMabonne_1.jpg

À la borne d'abonnement, en visioconférence.

(ou bien sur le site Web)



Presenter Notes
===============

Peut être certain d'entre vous connaissent le service. C'est un service de
location de voiture unique dans son mode de fonctionnement.


----

Le service Autolib’
===================

.. image:: img/suivez-le-guide_2_jeLoue_1.jpg

À la borne de location, avec mon badge RFID.

----

Le service Autolib’
===================

.. image:: img/suivez-le-guide_3_jeRoule_1.jpg

La voiture me connaît, et je peux appeler le centre opérationnel.

----

Le service Autolib’
===================

.. image:: img/suivez-le-guide_4_jePasse_1.jpg

À la borne de charge, avec mon badge RFID.

----

Feuille de route
================

- 16/12/10 : Bolloré remporte l'appel d'offres pour Autolib’
- 01/02/11 : début des travaux sur le service
- 01/03/11 : 2 développeurs
- 01/04/11 : 4 développeurs
- 01/06/11 : 10 développeurs
- 26/06/11 : proof-of-concept
- 02/10/11 : beta test
- 05/12/11 : ouverture au grand public
- ??/04/12 : ouverture aux entreprises
- et beaucoup de projets à venir !

----

Rôle de Polyconseil
===================

- Cadrage stratégique, définition et spécification du service
- Développement du système d'information métier et du site web
- Télécoms, hébergement, exploitation, supervision, déploiement, etc.

.. image:: img/role_de_polyconseil.png
    :width: 70%

----

Architecture technique générale
===============================

.. image:: img/schema_si_autolib.png
    :width: 70%


----

Architecture du SI métier
=========================

.. image:: img/applis_si_autolib.png

----

Librairies
==========

- Django, PostGIS, South
- django-cms, django-cms-search, haystack, whoosh
- piston
- soaplib, suds
- django-resto, django-xworkflows, django-ajax-selects
- django_compressor
- Google Maps
- etc.

----

Outils
======

- Mercurial (15 000 commits)
- Trac (2 000 tickets)
- Jenkins (5 000 builds)
- unittest (1 800 tests), lettuce (1 200 tests)
- factory_boy, fudge
- pylint, coverage
- Sphinx (170 pages)
- Sentry

----

Organisation
============

Contact client
--------------

- Spécifications légères et travail itératif
- Ré-orientations fréquentes des priorités
- "Gardes du corps" : AMOA et helpdesk

Développement
-------------

- Une ou deux personnes par sujet
- Review des commits avant chaque release

Mise en production
------------------

- Une release par semaine
- Passage de dév en prod sans recette (!)

----

Pour la route
=============

Ne pas dériver sur :

- les *coding rules*,
- la couverture de tests,
- l'organisation du code,
- l'ambiance de l'équipe.

----

Questions ?
===========
