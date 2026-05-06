from DaoUserClient import DaoUserClient

class ViewConsole:
    daoClient = DaoUserClient()
    token_actual = None  # Guardamos el token aquí para las siguientes llamadas

    def show_taps_view(self, token):
        client = DaoUserClient()
        print("\n--- LISTADO DE TAPS ---")
        
        taps = client.get_taps(token)
        
        if not taps:
            print("No se encontraron registros o token inválido.")
            return

        # Formateamos la salida para que quede profesional
        print(f"{'ID':<5} | {'Child ID':<10} | {'Status':<8} | {'Fecha (Init)':<25}")
        print("-" * 60)
        
        for t in taps:
            
            print(f"{t['id']:<5} | {t['child_id']:<10} | {t['status_id']:<8} | {t['init']}")


    def viewShowmenu(self):
        print("\n--- MENU PROTOTIPO 3 ---")
        print("1: Login (User/Pass)")
        print("2: Login por Token (Auto-login)")
        print("3: Ver mis Hijos (Childs)")
        print("4: Ver Taps")
        print("5: Saliendo...")
        while True:
            option = input("Selecciona una opción: ")
            if option.isdigit():
                opt = int(option)
                if 0 < opt < 6:
                    return opt
            print("ERROR: Opción no válida.")

    def viewGeneral(self):
        option = -1
        while option != 5:
            option = self.viewShowmenu()
            match option:
                case 1:
                    self.viewLogin()
                case 2:
                    self.viewLoginToken()
                case 3:
                    self.viewGetChilds()
                case 4:
                    if self.token_actual:
                        self.show_taps_view(self.token_actual)
                    else:
                        print("⚠️ Primero debes hacer login para obtener un token.")
                case 5:
                    print("Cerrando aplicación...")

    def viewLogin(self):
        print("\n[LOGIN TRADICIONAL]")
        username = input("Username o email: ")
        passwd = input("Password: ")
        
        res = self.daoClient.login(username, passwd)

        if res and res.get("status") == "success":
            user_data = res.get("user")
            self.token_actual = user_data.get("token") # Guardamos el token
            print(f"✅ Login OK. Bienvenido {user_data.get('username')}")
        else:
            print("❌ Error: Credenciales inválidas.")

    def viewLoginToken(self):
        print("\n[LOGIN POR TOKEN]")
        if not self.token_actual:
            self.token_actual = input("No hay token guardado. Introduce uno manualmente: ")

        # Llamamos al mismo endpoint pero enviando el token en el header
        res = self.daoClient.login_con_token(self.token_actual)

        if res and res.get("status") == "success":
            print(f"✅ Re-autenticación exitosa para: {res.get('user_found')}")
        else:
            print("❌ Token no válido o expirado.")
            self.token_actual = None

    def viewGetChilds(self):
        print("\n[MIS HIJOS]")
        if not self.token_actual:
            print("⚠️ Primero debes hacer login para obtener un token.")
            return

        res = self.daoClient.get_childs(self.token_actual)

        if res and res.get("status") == "success":
            childs = res.get("childs")
            print(f"Tienes {len(childs)} hijos registrados:")
            for c in childs:
                print(f" - ID: {c['id']} | Nombre: {c['child_name']}")
        else:
            print(f"❌ Error: {res.get('error', 'No se pudieron cargar los hijos')}")

if __name__ == '__main__':
    viewConsole = ViewConsole()
    viewConsole.viewGeneral()