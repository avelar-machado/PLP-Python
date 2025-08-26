# Classe base
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self._battery = 100  # atributo "privado" (encapsulamento)

    def call(self, number):
        print(f"{self.brand} {self.model} calling {number}...")

    def install_app(self, app):
        print(f"Installing {app} on {self.model}...")

    def battery_status(self):
        print(f"Battery at {self._battery}%")


# Classe derivada (herança)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    # Polimorfismo: redefinindo método
    def install_app(self, app):
        print(f"Installing {app} with GPU acceleration ({self.gpu}) 🎮")


# Testando
phone1 = Smartphone("Samsung", "Galaxy S23", "256GB")
phone1.call("923-555-111")
phone1.install_app("WhatsApp")
phone1.battery_status()

print("----")

gaming_phone = GamingPhone("Asus", "ROG Phone 7", "512GB", "Adreno 740")
gaming_phone.call("923-555-222")
gaming_phone.install_app("PUBG Mobile")
gaming_phone.battery_status()
