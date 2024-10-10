class Cafetera:
    def __init__(self, cafe=50, vasos_pequenos=10, vasos_medianos=10, vasos_grandes=10):
        self.cafe = cafe
        self.vasos_pequenos = vasos_pequenos
        self.vasos_medianos = vasos_medianos
        self.vasos_grandes = vasos_grandes

    def servir_cafe(self, tipo_vaso, cantidad_cafe):
        if not self.hay_vasos(tipo_vaso):
            return f"No hay vasos de tipo {tipo_vaso}"
        if not self.hay_cafe(cantidad_cafe):
            return "No hay suficiente café"
        
        self.restar_vaso(tipo_vaso)
        self.restar_cafe(cantidad_cafe)
        return f"Café servido en vaso {tipo_vaso}"

    def hay_vasos(self, tipo_vaso):
        if tipo_vaso == "pequeño":
            return self.vasos_pequenos > 0
        elif tipo_vaso == "mediano":
            return self.vasos_medianos > 0
        elif tipo_vaso == "grande":
            return self.vasos_grandes > 0
        return False

    def hay_cafe(self, cantidad_cafe):
        return self.cafe >= cantidad_cafe

    def restar_vaso(self, tipo_vaso):
        if tipo_vaso == "pequeño":
            self.vasos_pequenos -= 1
        elif tipo_vaso == "mediano":
            self.vasos_medianos -= 1
        elif tipo_vaso == "grande":
            self.vasos_grandes -= 1

    def restar_cafe(self, cantidad_cafe):
        self.cafe -= cantidad_cafe

    def reiniciar_cafetera(self):
        self.cafe = 50
        self.vasos_pequenos = 10
        self.vasos_medianos = 10
        self.vasos_grandes = 10
