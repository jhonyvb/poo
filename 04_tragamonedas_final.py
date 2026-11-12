import random
class Tragamonedas:
    def __init__ (self,nombre,creditos,simbolos=None):
        self.nombre=nombre
        self._creditos=creditos
        self._total_apostado=0
        self._total_ganado=0
        self._jugadas=0
        if simbolos is None:
            simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣", "🍋"]
        self.simbolos=simbolos
    @property
    def creditos(self):
        return self._creditos   

    @property
    def total_apostado(self):
        return self._total_apostado

    @property
    def total_ganado(self):
        return self._total_ganado

    def mostrar(self):
        print(f"{self.nombre}- Creditos S/{self.creditos}")

    def girar(self):
        
        resultado=[]

        for i in range(3):
            resultado.append(random.choice(self.simbolos))
        print(f"{resultado[0]} {resultado[1]} {resultado[2]}")
        return resultado

    def _cobrar(self,apuesta):
        if apuesta<=0:
            print("La apuesta debe ser mayor que cero")
            return False
        if apuesta>self.creditos:
            print(f"No tienes suficientes creditos, solo tienes S/ {self._creditos}")
            return False
        self._creditos-=apuesta
        self._total_apostado+=apuesta
        self._jugadas+=1
        return True

    def _pagar(self, premio):
        self._creditos+=premio
        self._total_ganado+=premio


    def jugar(self,apuesta):

        if not self._cobrar(apuesta):
            return

        resultado =self.girar()
        premio=0

        if resultado[0]==resultado[1]==resultado[2]:
            premio = apuesta*10
            print(f"!Jackpot! Ganaste S/ {premio}")
            
        elif resultado[0]==resultado[1] or resultado[1]==resultado[2] or resultado[0]==resultado[2]:
            premio=apuesta*2
            print(f"!Dos iguales! ganaste S/ {premio}")
            
        else:
            print(f"Perdiste S/{apuesta}")

        if premio>0:
            self._pagar(premio)

    def mostrar_estadisticas(self):
        balance=self._total_ganado-self._total_apostado
        print(f"{self.nombre}")
        print(f" Jugadas: {self._jugadas}")
        print(f" Total apostado: S/{self._total_apostado}")
        print(f" Total ganado: S/{self._total_ganado}")
        print(f" Balance del jugador; S/ {balance}")

def bucle_de_juego(maquina):
       while True:
           if maquina.creditos<=0:
               print("Te quedaste sin credito,¡Fin del juego!")
               break
           print()
           maquina.mostrar()
           try:
               apuesta=int(input("¿Cuato vas a apostar? (0 para salir):"))
           except ValueError:
               print("Escribe un numero entero ")
               continue
           if apuesta==0:
               print(f"Saliste con S/ {maquina.creditos}, ¡Vuelve de nuevo")
               break
           maquina.jugar(apuesta)

def mostrar_menu(maquinas):
    print("\n CASINO ROYALE \n")
    for i, m in enumerate(maquinas, start=1):
        if m.creditos <= 0:
            print(f"{i}. {m.nombre} (SIN CRÉDITOS)")
        else:
            print(f"{i}. {m.nombre} (S/ {m.creditos})")
    print(f"{len(maquinas) + 1}. Mostrar estadísticas de todas")
    print(f"{len(maquinas) + 2}. Salir")


def resumen_general(maquinas):
    print("\n RESUMEN GENERAL DEL CASINO")
    total_apostado = 0
    total_ganado = 0
    for m in maquinas:
        m.mostrar_estadisticas()
        total_apostado += m.total_apostado
        total_ganado += m.total_ganado
    print(f"\n Total apostado en el casino: S/ {total_apostado}")
    print(f" Total pagado en premios:     S/ {total_ganado}")
    print(f" Ganancia del casino:         S/ {total_apostado - total_ganado}")


def main():
    maquinas = [
        TragamonedasFrutas("La Frutal", 200),
        TragamonedasClasico("La Clásica", 300),
        TragamonedasMundial("Mundial 2026", 150),
    ]
    opcion_stats = len(maquinas) + 1
    opcion_salir = len(maquinas) + 2

    while True:
        mostrar_menu(maquinas)
        try:
            opcion = int(input("\nElige una opción: "))
        except ValueError:
            print(" Escribe un número, por favor")
            continue

        if 1 <= opcion <= len(maquinas):
            maquina = maquinas[opcion - 1]
            if maquina.creditos <= 0:
                print("Esa máquina no tiene créditos")
            else:
                bucle_de_juego(maquina)
        elif opcion == opcion_stats:
            print()
            for m in maquinas:
                m.mostrar_estadisticas()
                print()
        elif opcion == opcion_salir:
            resumen_general(maquinas)
            print("\n ¡Gracias por jugar!")
            break
        else:
            print(" Opción no válida")


class TragamonedasFrutas(Tragamonedas):
    def __init__(self, nombre,creditos):
        super().__init__(nombre, creditos,["🍒", "🍋", "🍊"])

class TragamonedasClasico(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos, ["7️⃣", "💎", "🔔"])

class TragamonedasMundial(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre,creditos,["🇵🇪", "🇦🇷", "🇫🇷", "🇧🇷"])

    def jugar(self, apuesta):
        if not self._cobrar(apuesta):
            return
        resultado=self.girar()
        premio=0

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 15
            print(f"🏆 ¡CAMPEONES! Ganaste S/ {premio}")
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")
        elif "🇵🇪" in resultado:
            premio = apuesta
            print(f"🇵🇪 ¡Salió Perú! Te devolvemos tu apuesta: S/ {premio}")
        else:
            print(f"😢 Perdiste S/ {apuesta}")

        if premio>0:
            self._pagar(premio)

main()

