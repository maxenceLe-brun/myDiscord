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

"À chaque connexion, l’utilisateur récupère l’ensemble des messages déjà postés. Chaque message doit posséder l’heure de publication et son auteur."
tous est enregistré dans une base sql qui porte le nom de "userN" ou N est l'ID de l'utilisateur

"Plusieurs channels doivent être mis à dispositions des utilisateurs."
Il y en a un, mais vide

"Un utilisateur doit pouvoir se connecter ou se créer son compte afin d’avoir accès au channel principale."
All good

"Les informations nécessaires à l’inscription sont : un nom, prénom, mail et mot de passe."
All good

"Un bouton déconnexion doit être implémenté, renvoyant l’utilisateur sur la page de connexion."
All good

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
