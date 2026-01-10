ELia Loeb, 15639517

opdracht 1:

Ik heb als eerst een wachtwoord op Snellius ingesteld. Ik zat niet in die eerste 12 uur dus heb het via wachtwoord vergeten gedaan en dit ging heel makkelijk. hierna ben ik via mijn terminal met het commando ssh -v scur2328@snellius.surf.nl en hierna mijn wachtwoord snellius binnengegaan. ik zit op node int4. Ik heb via voorgaande vakken zoals webtech al ervaring met ssh.

ss van welkom:
![Welkomstbericht Snellius](assets/welkom.png)

ss van node:
![node](assets/node.png)


opdracht 2:

Eerst deed ik module load 2025. Hierna module load Python/3.11.3 maar dit gaf deze error: Lmod has detected the following error:  The following module(s) are
unknown: "Python/3.11.3".  
Ik denk dat dit komt omdat dit niet de goede Python versie is dus om te checken welke ik wel nodig heb heb ik dit commando gebruikt: module spider Python. Hier kwamen verschillende Python versies uit die ik kon gebruiken en ik heb deze gekozen: Python/3.13.1-GCCcore-14.2.0. nu deed ik de command: module load Python/3.13.1-GCCcore-14.2.0. Hierna deed ik de command module spider matplotlib en heb versie matplotlib/3.10.3-gfbf-2025a van matplotlib gekozen dus deed ik het command: matplotlib/3.10.3-gfbf-2025a. module load matplotlib/3.10.3-gfbf-2025a.

Hierna ging ik door met het instellen van de venv. Eest wilde ik in mijn map gaan met dit commando cd ~/MLOps/assignment_1 maar ik kreeg deze  error: -bash: cd: /home/scur2328/MLOps/assignment_1: No such file or directory.
Hierna heb ik de map aangemaakt met mkdir -p ~/MLOps/assignment_1 en ben ik weer de map ingegaan met het commando hiervoor en dit lukte. HIerna heb ik de venv aangemaakt met dit commando python -m venv venv en heb hem geactiveerd met dit commando source venv/bin/activate. Hierna runde ik pip install pytorch en dit duurde ongerveer 3 minuten. ook kreeg ik aan het einde deze melding: [notice] A new release of pip is available: 24.3.1 -> 25.3. Mijn volgende command was python en hierna import torch en import matplolib en daarna exit(). bij de laatste gegeven command kreeg ik output: 
PyTorch: 2.9.1+cu128
CUDA available: False
aangezien ik op een login node zit had ik inderdaad al verwacht dat dit False was.


Opdracht 3:
