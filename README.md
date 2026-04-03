------------------------------------------------------------------------------------------------------
ATELIER API-DRIVEN INFRASTRUCTURE
------------------------------------------------------------------------------------------------------
L’idée en 30 secondes : **Orchestration de services AWS via API Gateway et Lambda dans un environnement émulé**.  
Cet atelier propose de concevoir une architecture **API-driven** dans laquelle une requête HTTP déclenche, via **API Gateway** et une **fonction Lambda**, des actions d’infrastructure sur des **instances EC2**, le tout dans un **environnement AWS simulé avec LocalStack** et exécuté dans **GitHub Codespaces**. L’objectif est de comprendre comment des services cloud serverless peuvent piloter dynamiquement des ressources d’infrastructure, indépendamment de toute console graphique.Cet atelier propose de concevoir une architecture API-driven dans laquelle une requête HTTP déclenche, via API Gateway et une fonction Lambda, des actions d’infrastructure sur des instances EC2, le tout dans un environnement AWS simulé avec LocalStack et exécuté dans GitHub Codespaces. L’objectif est de comprendre comment des services cloud serverless peuvent piloter dynamiquement des ressources d’infrastructure, indépendamment de toute console graphique.
  
-------------------------------------------------------------------------------------------------------
Séquence 1 : Codespace de Github
-------------------------------------------------------------------------------------------------------
Objectif : Création d'un Codespace Github  
Difficulté : Très facile (~5 minutes)
-------------------------------------------------------------------------------------------------------
RDV sur Codespace de Github : <a href="https://github.com/features/codespaces" target="_blank">Codespace</a> **(click droit ouvrir dans un nouvel onglet)** puis créer un nouveau Codespace qui sera connecté à votre Repository API-Driven.
  
---------------------------------------------------
Séquence 2 : Création de l'environnement AWS (LocalStack)
---------------------------------------------------
Objectif : Créer l'environnement AWS simulé avec LocalStack  
Difficulté : Simple (~5 minutes)
---------------------------------------------------

Dans le terminal du Codespace copier/coller les codes ci-dessous etape par étape :  

**Installation de l'émulateur LocalStack**  
```
sudo -i mkdir rep_localstack
```
```
sudo -i python3 -m venv ./rep_localstack
```
```
sudo -i pip install --upgrade pip && python3 -m pip install localstack && export S3_SKIP_SIGNATURE_VALIDATION=0
```
```
localstack start -d
```
**vérification des services disponibles**  
```
localstack status services
```
**Réccupération de l'API AWS Localstack** 
Votre environnement AWS (LocalStack) est prêt. Pour obtenir votre AWS_ENDPOINT cliquez sur l'onglet **[PORTS]** dans votre Codespace et rendez public votre port **4566** (Visibilité du port).
Réccupérer l'URL de ce port dans votre navigateur qui sera votre ENDPOINT AWS (c'est à dire votre environnement AWS).
Conservez bien cette URL car vous en aurez besoin par la suite.  

Pour information : IL n'y a rien dans votre navigateur et c'est normal car il s'agit d'une API AWS (Pas un développement Web type UX).

---------------------------------------------------
Séquence 3 : Exercice
---------------------------------------------------
Objectif : Piloter une instance EC2 via API Gateway
Difficulté : Moyen/Difficile (~2h)
---------------------------------------------------  
Votre mission (si vous l'acceptez) : Concevoir une architecture **API-driven** dans laquelle une requête HTTP déclenche, via **API Gateway** et une **fonction Lambda**, lancera ou stopera une **instance EC2** déposée dans **environnement AWS simulé avec LocalStack** et qui sera exécuté dans **GitHub Codespaces**. [Option] Remplacez l'instance EC2 par l'arrêt ou le lancement d'un Docker.  

**Architecture cible :** Ci-dessous, l'architecture cible souhaitée.   
  
![Screenshot Actions](API_Driven.png)   
  
---------------------------------------------------  
## Processus de travail (résumé)

1. Installation de l'environnement Localstack (Séquence 2)
2. Création de l'instance EC2
3. Création des API (+ fonction Lambda)
4. Ouverture des ports et vérification du fonctionnement

---------------------------------------------------
Séquence 4 : Documentation  
Difficulté : Facile (~30 minutes)
---------------------------------------------------
**Complétez et documentez ce fichier README.md** pour nous expliquer comment utiliser votre solution.  
Faites preuve de pédagogie et soyez clair dans vos expliquations et processus de travail.  
   
---------------------------------------------------
Evaluation
---------------------------------------------------
Cet atelier, **noté sur 20 points**, est évalué sur la base du barème suivant :  
- Repository exécutable sans erreur majeure (4 points)
- Fonctionnement conforme au scénario annoncé (4 points)
- Degré d'automatisation du projet (utilisation de Makefile ? script ? ...) (4 points)
- Qualité du Readme (lisibilité, erreur, ...) (4 points)
- Processus travail (quantité de commits, cohérence globale, interventions externes, ...) (4 points) 




🚀 API-Driven Infrastructure : Pilotage EC2 via AWS Lambda & LocalStack
📝 Présentation du projet
Cet atelier porte sur la conception d'une architecture API-driven permettant de piloter des ressources d'infrastructure (instances EC2) sans passer par une interface graphique.

L'objectif est d'utiliser une requête HTTP pour déclencher une fonction Lambda via API Gateway, laquelle interagit avec l'environnement AWS simulé par LocalStack au sein de GitHub Codespaces.

⚙️ Séquence 1 & 2 : Configuration de l'environnement
Pour garantir un environnement reproductible et éviter les conflits de dépendances, j'ai mis en place un environnement virtuel Python et installé les outils nécessaires (CLI AWS et LocalStack).

Automatisation du Setup
J'ai créé un script setup.sh (ou intégré au Makefile) pour automatiser ces étapes :

Initialisation : Création d'un venv pour isoler les bibliothèques.

Installation : pip install localstack awscli-local awscli boto3.

Lancement : Démarrage de LocalStack en mode détaché (-d) et attente de la disponibilité des services.

Note technique : J'ai configuré le port 4566 en mode Public dans l'onglet Ports de Codespaces pour exposer l'endpoint AWS vers l'extérieur.

🏗️ Séquence 3 : Architecture & Déploiement
1. Instance EC2 Cible
J'ai initialisé une instance EC2 simulée pour servir de cible à nos commandes :

ID de l'instance : i-e62181aebb22abbb7

Image : ami-03cf127a (générique LocalStack)

2. Logique de la Fonction Lambda
Le cœur du projet réside dans lambda_function.py. La fonction a été conçue pour être résiliente :

Elle détecte l'action souhaitée en analysant le chemin de la requête (/start ou /stop).

Elle récupère l'ID de l'instance via les Query String Parameters.

Elle retourne une réponse textuelle claire avec des Emojis pour un feedback visuel immédiat.

3. Routage API Gateway
Plutôt que d'utiliser une URL générique, j'ai exposé deux points d'entrée distincts pour améliorer l'expérience utilisateur :

Endpoint Start : /prod/start

Endpoint Stop : /prod/stop

🧪 Séquence 4 : Utilisation & Validation
Comment tester la solution ?
Une fois l'infrastructure déployée, le pilotage se fait directement via le navigateur ou une commande curl.

Pour démarrer l'instance :
https://shiny-funicular-x7j6vqq57x9f657v-4566.app.github.dev/restapis/y8dvirlymk/prod/_user_request_/start?instance_id=i-e62181aebb22abbb7

Pour arrêter l'instance :
https://shiny-funicular-x7j6vqq57x9f657v-4566.app.github.dev/restapis/y8dvirlymk/prod/_user_request_/stop?instance_id=i-e62181aebb22abbb7

Pour le Status de l'instance:
https://shiny-funicular-x7j6vqq57x9f657v-4566.app.github.dev/restapis/y8dvirlymk/prod/_user_request_/status?instance_id=i-e62181aebb22abbb7

Résultat attendu
Le navigateur (ou le terminal) affichera un message de succès formaté :

🛑 Succès : L'instance i-e62181aebb22abbb7 a été ARRÊTÉE avec succès.

🛠️ Degré d'automatisation (Bonus)
Pour simplifier la maintenance du projet, j'ai centralisé les commandes dans un Makefile.

make setup : Prépare l'environnement virtuel et installe les outils.

make deploy : Package la Lambda et met à jour le code sur LocalStack.

make status : Vérifie l'état actuel des instances EC2.

🧠 Difficultés rencontrées & Solutions
Problème de Command Not Found : Résolu en activant systématiquement le source venv/bin/activate et en installant awscli directement dans l'environnement virtuel.

Parsing des paramètres : Lors de l'invocation directe, les paramètres d'URL n'étaient pas toujours transmis. J'ai modifié le handler Lambda pour qu'il soit capable de chercher l'action directement dans le path de l'événement, rendant le routage via API Gateway plus robuste.

Encodage Unicode : J'ai ajouté des headers HTTP (Content-Type: text/plain; charset=utf-8) à la réponse Lambda pour que les caractères accentués s'affichent correctement dans le navigateur.
