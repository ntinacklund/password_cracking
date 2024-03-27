import requests

# URL till inloggningssidan på Flask-applikationen
URL = "http://127.0.0.1:5000/"

def try_login(username, password):
    """
    Försöker logga in på webbsidan med angivet användarnamn och lösenord.
    Returnerar True om inloggningen lyckades, annars False.
    """
    # Data som ska skickas med POST-begäran
    data = {
        'username': username,
        'password': password
    }
    
    # Skicka POST-begäran till servern
    response = requests.post(URL, data=data)
    
    # Kontrollera om inloggningen lyckades
    if "Login successful!" in response.text:
        return True
    else:
        return False

# Lägg din kod här.
if try_login("user1", "short"):
    print("Inloggning lyckades för user1 med lösenord 'short'.")
else:
    print("Inloggning misslyckades för user1.")
