# Le fix me

## Installation

- Un peu de readme, bel effort mais c'est pas super clair..
- Bleeding edge Django? Alors qu'il y a deux mises à jour corrigeant des CVE.
- Plein de dépendences non listées
- Pas sûr que gevent, gunicorn et boto soient nécessaire en production.

## Python

- Avoir créé une application users, c'est bien.
- Avoir refait toutes les vues de django-friendship c'est du travail pour beurre.
- Vous déclenchez des requêtes SQL depuis les templates ce qui crée des doublons inutiles.
- Problème du SELECT N+1

## HTML

- H2 + H5 c'est mal pour la table des matières du document.

## UX

- Étant connecté, il me propose d'inscrire.
- L'upload est multiple mais il n'y a qu'un seul champ nom??
- en mode mobile, l'image source est plus grande que la vue modale, peu utile.
- Gros mélange de franglais.
- AJAX:

  - Vous avez bataillé comme des diables pour placer deux actions en AJAX. Pas sûr que ce temps ait été investi de la meilleure manière qui soit. Commencez simplement!
  - L'upload par drag'n'drop avec django ne manque pas d'exemple et aurait été bien plus intéressant.
  - HTML5 propose plein d'API pour traiter des images, des uploads asynchrônes etc.

- L'application devrait être un gros upload + gestion des fichiers envoyés et un affichage responsive (srcset).
