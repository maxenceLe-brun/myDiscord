# myDiscord
Hey!
Here you can find my project on making a discord-like app  
you can log-in, chat with other people, interact with them etc etc  
It's not finished yet, but feel free to check and report me any bugs!  
i've started working on this very early, but i'm proud of what i made in a short amount of time  

# French informations about the dev state

"Développer votre version de Discord sur un thème choisi,  
avec l’interface graphique de votre choix."  
interface faite main  

"Le programme doit permettre à plusieurs personnes de communiquer, grâce à des canaux textuelles et vocales, publique et privée."  
la communication a commencé, mais pas dev  
Pour essayer le vocal, voir avec "main.py" et "myDiscord_Server.py", mettre son ip dans ces deux fichiers  
Le vocal marche, mais il n'est pa implémenté  

"À chaque connexion, l’utilisateur récupère l’ensemble des messages déjà postés. Chaque message doit posséder l’heure de publication et son auteur."  
tous est enregistré dans une base sql qui porte le nom de "userN" ou N est l'ID de l'utilisateur  
l'auteur du message est affiché par son ID de compte  
l'heure est l'heure actuelle sans les ":"  
nous avons donc une base de donnée par utilisateur qui stoque chaque message qu'il reçoit  

"Plusieurs channels doivent être mis à dispositions des utilisateurs."  
Il y en a un, mais vide  
cliquer sur le cercle en haut a gauche nour permet d'y "acceder" mais presque rien est fait  

"Un utilisateur doit pouvoir se connecter ou se créer son compte afin d’avoir accès au channel principale."  
Tout bon  
Lors du chargement du programme, on arrive sur la page pour log-in, avec 2 boutons  
a gauche pour l'inscription, a droite pour se connecter a son compte  
il suffit de cliquer sur une case blanche pour y écrire dedans  

"Les informations nécessaires à l’inscription sont : un nom, prénom, mail et mot de passe."  
Tout bon  
Pour créer un compte, le nom de famille doit comporter un caractère au minimum, le prénom deux,  
l'email doit en avoir 12 avec un "@" dedans, le mot de passe doit avoir 6 caractères min, et confirmer celui ci  
  
"Un bouton déconnexion doit être implémenté, renvoyant l’utilisateur sur la page de connexion."  
Tout bon  
le bouton est peut être un peu petit  

"Dans ce projet, vous devez utiliser les classes (une classe par fichier) et une base de données nommée “myDiscord.sql” avec plusieurs tables."  
j'ai utilisé des classes, mais pas que  
base de donnée ok  
    
# Patch history


patch note 0.1: 4/18/23 5:50 AM
* App still under development  
* you can register and login  
* the VC is ready but not implemented  
* you can't log out without closing the window  
* you can only create one account by email  
* your password need a minimum of 6 characters  
* nothing is hosted, so actually it's only local  
  
patch note 0.2: 4/18/23 11:03 AM
* You can now log-out from your account
* Your ID is now shown on the left corner
* The "Friend" button can only be triggered, nothing will really happen
* each account will have his own SQL table for each messages he receives
* added the slot for the vocal button, but still in development

patch note 0.3: 4/19/23 4:55 AM
* You can now see your friends on the left
* SQL Database don't work when host on plesk, can't put it online
* Vocal has encountered a prolem : only local vc work
* The debogage system will be removed next time
* The SQL Database will update soon!

patch note 0.4: 4/19/23 5:44 AM 
* You can now write to your friends, but they won't see it
* Press enter to send the message, no button to click on!
* New target system to messages
* Time module imported
* Debug mode still there for upcomming changes
* The SQL Database encountered problems with plesk, not comming soon as we would
* The friend request and list is being in rework!
