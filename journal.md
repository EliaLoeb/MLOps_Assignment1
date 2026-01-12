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
Ik denk dat dit komt omdat dit niet de goede Python versie is dus om te checken welke ik wel nodig heb heb ik dit commando gebruikt: module spider Python. Hier kwamen verschillende Python versies uit die ik kon gebruiken en ik heb deze gekozen: Python/3.13.1-GCCcore-14.2.0. nu deed ik de command: module load Python/3.13.1-GCCcore-14.2.0. Hierna deed ik de command module spider matplotlib en heb versie matplotlib/3.10.3-gfbf-2025a van matplotlib gekozen dus deed ik het command: module load matplotlib/3.10.3-gfbf-2025a.

Hierna ging ik door met het instellen van de venv. Eest wilde ik in mijn map gaan met dit commando cd ~/MLOps/assignment_1 maar ik kreeg deze  error: -bash: cd: /home/scur2328/MLOps/assignment_1: No such file or directory.
Hierna heb ik de map aangemaakt met mkdir -p ~/MLOps/assignment_1 en ben ik weer de map ingegaan met het commando hiervoor en dit lukte. HIerna heb ik de venv aangemaakt met dit commando python -m venv venv en heb hem geactiveerd met dit commando source venv/bin/activate. Hierna runde ik pip install pytorch en dit duurde ongerveer 3 minuten. ook kreeg ik aan het einde deze melding: [notice] A new release of pip is available: 24.3.1 -> 25.3. Mijn volgende command was python en hierna import torch en import matplolib en daarna exit(). bij de laatste gegeven command kreeg ik output: 
PyTorch: 2.9.1+cu128
CUDA available: False
aangezien ik op een login node zit had ik inderdaad al verwacht dat dit False was.


Opdracht 3:

URL: https://github.com/EliaLoeb/MLOps_Assignment1.git

Ik heb een HTTPS met een personal access token gebruikt. dit ging heel soepel eerst heb ik zelf een token gemaakt, deze apart opgeslagen en daarna gebruikt samen met de link als authenticatie. Ik heb geen errors gekregen.

venv/, __pycache__/, data/ en *.pt zijn belangrijk om in het gitignore bestand te zetten. Het is zeker handig de nodige informatie in het README bestand te zetten zodat iemand anders de dingen die ik gedaan heb goed kan herhalen en dezelfde modules etc. hiervoor gebruikt.

fe60859 (HEAD -> main) add readme
1b77ca0 (origin/main) Initial commit: setup journal and gitignore


Opdracht 4:

job script:

#!/bin/bash
#SBATCH --job-name=mijn_test_job
#SBATCH --output=resultaat_%j.txt
#SBATCH --partition=rome
#SBATCH --time=00:05:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

module load 2025
module load Python/3.13.1-GCCcore-14.2.0
source venv/bin/activate


echo "rekennode!"
python -c "import torch; print('Torch versie:', torch.__version__)"

output:
rekennode!
/gpfs/home6/scur2328/MLOps/assignment_1/venv/lib/python3.13/site-packages/torch>
  cpu = _conversion_method_template(device=torch.device("cpu"))
Torch versie: 2.9.1+cu128

De job ID is 18242083 en de job duurde minder dan een minuut.

Alles ging wel goed ik was alleen in mijn eerste script vergeten het haakje te sluiten. hier kwam ik nadat ik de job had gerund pas achter maar dit stond heel duidelijk aangegeven. Hierna heb ik hetzekfde script met het gesloten haakje gerund met nu als titel job2.sh in plaats van job.sh en dit gaf de gewenste output.

foutmelding:
rekennode
  File "<string>", line 1
    import torch; print('Torch versie:'
                       ^
SyntaxError: '(' was never closed

Door het te submitten als een batchjob eventjes toegang tot de gpu voor jezelf in plaats van dat je het met iedereen moet delen in de login node.

We gebruiken een cluster zodat iedereen wanneer het mogelijk is zijn job kan runnen en er niet tegelijkertijd heel veel grote jobs worden gerund. dit zorgt ervoor dat snellius niet overbelast wordt.


Opdracht 5:

Het direct laden en storen van al deze kleine files zorgt voor performance issues omdat snellius bij elk documentje moet kijken waar en van wie het bestand vandaan komt. dit kost bij zoveel kleien bestandjes heel veel tijd en energie.
Twee opties zijn alle data in een groot bestand zetten en de dataset aan het begin in een keer naar de node te sturen. Om version control op grote datasets te doen kan je DVC gebruiken.

verschillende python versie. dit kan voorkomen worden door in het readme bestand de versie die jij hebt gebruikt aan te geven.
andere random seed. Als je elke keer je random seed vastlegd verhelpt dit dat probleem.
andere CUDA versies. verhelp dit probleem door in de readme de cuda versie te noteren.

astral uv: astral uv is heel snel maar erg nieuw dus die is nog niet geimplementeerd in snellius.
python venv: onderstuend python modulesm maar die moet je wel zelf elke keer handmatig inladen.
conda: makkelijk te gebruiken maar werkt met heel veel kleine bestandjes wat niet handig is voor werk op snellius.


Opdracht 6:

Ik ben meerdere module not found errors tegenegekomen voor de modules h5py, tqdm, yaml en torchvision. Hierna heb ik welke keer weer gewoon deze modules ge pip installed en de test opnieuw uitgevoerd.

foutmelding:
=========================== short test summary info ============================
FAILED tests/test_imports.py::test_imports - ModuleNotFoundError: No module named 'h5py'
============================== 1 failed in 12.04s ==============================
(venv) [scur2328@int4 assignment_1]$ 

Het is beter omdat dit het makkelijker maakt bestanden en bestandsnamen te veranderen zonder de hele dataset aan te passen.

geslaagde test:
============================ test session starts ==============================
platform linux -- Python 3.13.1, pytest-8.3.5, pluggy-1.5.0
rootdir: /gpfs/home6/scur2328/MLOps/assignment_1
configfile: pyproject.toml
plugins: xdist-3.6.1
collected 1 item                                                               

tests/test_imports.py .                                                  [100%]

============================== 1 passed in 12.19s ==============================

Ik zie niks geks en denk niet dat ik iets aan moet passen.

Opdracht 7:

getitem omplementatie:

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        # TODO: Implement data retrieval
        # 1. Read data at idx
        # 2. Convert to uint8 (for PIL compatibility if using transforms)
        # 3. Apply transforms if they exist

        # 4. Return tensor image and label (as long)
        image = self.images[idx]
        label = self.labels[idx]
        image = np.clip(image, 0, 255).astype(np.uint8)

        if self.transform:
            image = self.transform(image)
        else:
            image = torch.from_numpy(image).float().permute(2, 0, 1) / 255.0

        label = torch.tensor(label).long().squeeze()
        return image, label

Omdat het bestand zo groot is heb ik gebruik gemaakt van h5py database zodat het bestand niet in zijn geheel wordt ingeladen.

![actions](assets/actionspage.png)

Eerst kreeg ik errors dat torch en np niet defined waren. om dit te verhelpen heb ik import torch en import numpy als no toegevoegd bovenaan. 
Daarbuiten kreeg ik de hele tijd deze error:
FAILED tests/test_data_loader.py::TestPCAMPipeline::test_numerical_stability - TypeError: PCAMDataset.__init__() got an unexpected keyword argument 'filte...
FAILED tests/test_data_loader.py::TestPCAMPipeline::test_heuristic_filtering - TypeError: PCAMDataset.__init__() got an unexpected keyword argument 'filte...
Deze error heeft iets met de innit te maken maar die heb ik niet zelf geschreven dus ik weet eigenlijk niet zo goed wat ik daarmee aan moet.

Aangezien de dataset imbaallanced is is het beter om een wieghted sampler te gebruiken zodat je bij elke test evenveel van de mogelijke gegevens hebt.

het is me zoals hierboven uitgelegd na lang proberen niet gelukt om alle tests goed te krijgen en dus ook niet om plots te maken.

Opdracht 8:

Ik heb de input diemnsie berekend door alle eerdere dimensies keer elkaar te doen.

Het is belangrijk om de test_backprop te testen omdat de loss waarde ook kan dalen door een error of een foutieve berekening.

test_mlp:

==================== test session starts =====================
platform linux -- Python 3.13.1, pytest-8.3.5, pluggy-1.5.0
rootdir: /gpfs/home6/scur2328/MLOps/assignment_1
configfile: pyproject.toml
plugins: xdist-3.6.1
collected 2 items                                            

tests/test_model_shapes.py ..                          [100%]

===================== 2 passed in 12.70s =====================

Opdracht 9:
Aangezien de tests bij zeven nog niet goed gingen en de innit nog niet goed is geimplementeerd lukt negen ook niet.
