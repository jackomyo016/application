[![Push de l'image Docker automatisée !!](https://github.com/jackomyo016/application/actions/workflows/prod.yml/badge.svg)](https://github.com/jackomyo016/application/actions/workflows/prod.yml)

# Probabilité de survie sur le Titanic

Pour pouvoir utiliser ce projet, il
est recommandé de créer un fichier `config.yaml`
ayant la structure suivante:

```yaml
jeton_api: ####
data_path: https://minio.lab.sspcloud.fr/lgaliana/ensae-reproductibilite/data/raw/data.csv
```

Pour installer les dépendances

```bash
pip install -r requirements.txt
```

Le déploiement de l'application est contrôlé par un autre dépôt : [lien Github](https://github.com/jackomyo016/application-deployment)

[Lien vers l'API : ](https://api-titanic-test.lab.sspcloud.fr/)

[Lien vers le site web : ](https://jackomyo016.github.io/application/)


