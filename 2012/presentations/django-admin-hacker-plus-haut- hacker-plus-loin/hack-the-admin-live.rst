Admin: hacker plus haut, hacker plus loin
=============================================

.fx: frontpage

(un back-office complexe mais convivial à partir de l'admin django pour Libération)

- Rencontres django-fr, Montpellier, 14-15 avril 2012

.. image:: img/logo-liberation.png

------------------

A propos
========

- Bonjour!

- Souen Boniface @youpitagada

- dev web depuis 4 ans (à Libération.fr)

---------------------------------------------------------------------------------------------------------

Introduction
============

- Disclaimer
- Migration de Libération.fr de PHP vers django: "front" puis "back"
- Avant: un CMS proprio en PHP, très customisé
- Objectifs:
    - Faire un vrai back-office en django
    - Rendre les gens heureux

.notes: front en août 2011, back le 8 avril 2012 (oui la semaine dernière)

.notes: vieux back à base de copier-coller

----

L'admin django (index)
======================

.fx: admin-native-index

.. image:: img/admin-native-index.png

----

L'admin django (article)
========================

.. image:: img/admin-native-article-lol.png

----

L'admin django après 6 mois (article)
=====================================

.. image:: img/quai-article-change.png

----

Comment ?
=========

----

Tiens oui, comment ?
====================

----

Le "back" de Libé en deux mots
==============================

- Deux missions:
    - site web Libération.fr
    - archives (800 000 articles depuis 1994)
- Utilisateurs *très* différents

.notes: Gestion des homepages, Rédaction des articles, Catégorisation des articles, Consultation des archives

----

Ce qui nous manquait de base dans l'admin
=========================================

- Interface qui s'adapte aux différents métiers
- Recherche multi-objets et multi-critères
- Gestion du concurrency control ("Qui a écrasé mes modifs ?!")
- Gestion ergonomique des relations entre objets (chasse aux clics!)

.notes: inlines: 1. empty form 2. popup changelist puis raw id fields

.notes: réactivité, bonheur

---------------------------------------------------------------------------------------------------------

Stratégie
=========

- Admin non utilisable telle quelle pour nos besoins
- On refait tout de zéro ou on part de l'admin ?

- Sprint de 15 jours à 4 devs pour tenter un proto à partir de l'admin
- A la fin du sprint:
    - On passe en Rails (ça va on peut plaisanter)
    - On part de l'admin (ouf!)

.notes: refaire tout avec des ModelForms

---------------------------------------------------------------------------------------------------------

Pourquoi garder l'admin
=======================

- Beaucoup de choses déjà codées (actions de masse, register, etc.)
- Prévue pour être étendue (lire le code!)
    - Possibilité d'avoir un ou plusieurs AdminSite custom
    - Nombreuses possibilités d'extension
        - ModelAdmin.get_changelist()
        - ChangeList.get_query_set()
        - ModelAdmin.get_fieldsets()
        - ModelAdmin.change|add_view()
        - ModelAdmin.save_model()
        - ModelAdmin.get_urls()
        - etc.
- Rester standard
- Compatibilité avec applis/snippets (dans les deux sens!)

----

En résumé
=========

- 2 AdminSite
- 1 ChangeList custom
- 31 ModelAdmin
- 39 ModelForm
- 13 InlineModelAdmin
- 5 InlineFormset
- 11 widgets
- 12 kms de JS, 7 kms de CSS, 119 templates
- 1 bonne idée ergonomique: popin!
- 6 applis fonctionnelles spécifiques

----

Merci les applis
================

.fx: thanks-applis

- (check chrono, 7 minutes 47)

----

django-admin-tools
==================

.. image:: img/quai-menu.png

.notes: très pratique/flexible

.notes: menu/page accueil dédiée pour chaque groupes d'utilisateurs

.notes: un peu de refactorisation à faire (DRYification, récupérer l'AdminSite dans le context, pas dans l'URL)

- https://bitbucket.org/izi/django-admin-tools/

-----------------

django-admin-tabs
=================

.. image:: img/quai-article-change.png

.notes: Organiser son change form en colonne + tabs, Change form != par groupe d'utilisateurs

.notes: Appli presque plug'n'play

- https://github.com/liberation/django-admin-tabs

-----------------

django-locking
==============

.. image:: img/quai-locked.png

.notes: django-locking: concurrency control

.notes: Plusieurs forks

- https://github.com/RobCombs/django-locking (fork le plus abouti)
- https://github.com/liberation/django-locking (plus intrusif, moins de requêtes HTTP)

-----------------

D'autres applis
===============

- django-tinymce
    - http://github.com/aljosa/django-tinymce
    - attention si STATIC sur un domaine à part: crossdomain problem!
- django-massadmin
    - https://github.com/liberation/django-massadmin
    - édition multiple, very dangerous!
- django-ajax-select
    - autocompletion pour les foreign key
- sesql
    - https://bitbucket.org/liberation/sesql/
- django-admin-basket
    - pas encore libéré

----

Limites de l'admin
==================

    - ModelAdmin: quelques points d'entrées manquants
        - change_view => un seul gros block
        - propriétés statiques => mieux avec la 1.4
    - JS
        - intrusif (onclick="")
        - vieux JS spaghetti fait alla mano
        - jquery pas à jour
        - manque d'API pour les widgets fournis
    - templates:
        - pas assez de points d'entrées {% block %}
        - obliger de redéclarer les inclusion_tag qu'on veut spécifique à un AdminSite (ex: {% submit_row %})
        - indentation

    - A nos patchs!

----

Questions ?
===========