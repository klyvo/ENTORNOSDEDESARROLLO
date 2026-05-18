#!/usr/bin/env python3
"""
Script de configuració i setup inicial per a Prototip 4
Instala les dependències i testa la connexió a la BBDD
"""

import subprocess
import sys
import os
from DaoLogin import DaoLogin


def install_requirements():
    """Instala els requisits del projecte"""
    print("=" * 60)
    print("Instalant dependències...")
    print("=" * 60)
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✓ Dependències instalades correctament")
        return True
    except subprocess.CalledProcessError:
        print("✗ Error instalant dependències")
        return False


def test_database_connection():
    """Testa la connexió a la base de dades"""
    print("\n" + "=" * 60)
    print("Testejant connexió a la base de dades...")
    print("=" * 60)
    
    dao = DaoLogin()
    con = dao.connectBBDD()
    
    if con:
        print("✓ Connexió exitosa a la BBDD")
        con.close()
        return True
    else:
        print("✗ Error en la connexió a la BBDD")
        print("  Assegurar-se que:")
        print("  - MySQL està executant-se a localhost:3306")
        print("  - Existeix la base de dades 'Tapatapp'")
        print("  - L'usuari 'root' existeix amb contrasenya 'root'")
        return False


def show_instructions():
    """Mostra les instruccions per executar el projecte"""
    print("\n" + "=" * 60)
    print("INSTRUCCIONS D'EXECUCIÓ")
    print("=" * 60)
    print("\n1. Executar el servidor Flask:")
    print("   cd server")
    print("   python server.py")
    print("\n2. En altra terminal, executar els tests:")
    print("   cd client")
    print("   python client_test.py")
    print("\n3. O accedir als endpoints directament:")
    print("   curl -X POST http://localhost:5000/login \\")
    print("     -H 'Content-Type: application/json' \\")
    print("     -d '{\"username\": \"mare\", \"password\": \"mare\"}'")
    print("\n" + "=" * 60)


def main():
    """Executa el setup inicial"""
    print("\n")
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║        PROTOTIP 4 - SETUP INICIAL                         ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    
    # Canviar al directori del server per accedir a DaoLogin
    script_dir = os.path.dirname(os.path.abspath(__file__))
    server_dir = os.path.join(script_dir, "server")
    
    # Instalar dependències
    if not install_requirements():
        print("\n✗ Setup fallat - No es van poder instalar les dependències")
        sys.exit(1)
    
    # Testejar connexió a BBDD
    os.chdir(server_dir)
    if not test_database_connection():
        print("\n⚠ Setup parcial - Dependències instalades però connexió a BBDD faillida")
        print("  Verifica la configuració de la BBDD i torna a provar")
        sys.exit(1)
    
    # Mostrar instruccions
    show_instructions()
    
    print("\n✓ Setup completat correctament!")
    print("  Els endpoints estan llists per usar!")


if __name__ == "__main__":
    main()
