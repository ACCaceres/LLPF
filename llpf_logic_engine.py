
class LLPFLogicEngine:
    def __init__(self):
        self.axiomas = []
        self.hechos = set()
        self.nuevos = set()
        self.variables = ["A", "B", "C", "D"]

    def agregar_axioma(self, premisa, conclusion):
        self.axiomas.append((premisa, conclusion))

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def ejecutar_inferencia(self):
        self.nuevos = set()
        for premisa, conclusion in self.axiomas:
            condiciones = [cond.strip() for cond in premisa.split("and")]
            for var in self.variables:
                valido = True
                for cond in condiciones:
                    negado = cond.startswith("not ")
                    texto = cond[4:] if negado else cond
                    evaluado = texto.replace("x", var)
                    evaluado_neg = f"not {evaluado}"
                    if (not negado and evaluado not in self.hechos) or (negado and evaluado_neg not in self.hechos and evaluado in self.hechos):
                        valido = False
                        break
                if valido:
                    nuevo = conclusion.replace("x", var)
                    self.nuevos.add(nuevo)
        self.hechos.update(self.nuevos)

    def ver_resultados(self):
        return self.hechos
