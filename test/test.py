import subprocess
import requests


# Vérification de la santé des conteneurs Docker
def test_sante_conteneurs():
    conteneurs = ["microservice_implement_stockmanagement-flask-frontend-1"]

    for conteneur in conteneurs:
        try:
            subprocess.check_output(["docker", "ps", "--filter", f"name={conteneur}"])
            print(f"Le conteneur {conteneur} est en cours d'exécution.")
        except subprocess.CalledProcessError:
            print(f"Le conteneur {conteneur} n'est pas en cours d'exécution.")


# Vérification du bon fonctionnement de l'application Flask
def test_bon_fonctionnement_application():
    url = "http://127.0.0.1:5000/"
    response = requests.get(url)
    if response.status_code == 200:
        print("L'application Flask fonctionne correctement.")
    else:
        print("Problème avec l'application Flask.")

# Exécution des tests
if __name__ == "__main__":
    test_sante_conteneurs()
    test_bon_fonctionnement_application()
    # test_bon_fonctionnement_base_de_donnees()