from abc import ABC, abstractmethod
from typing import TypeVar

# La interfaz de componente: define operaciones que los
# decoradores pueden alterar.

class Notifier(ABC):
    _name = None

    @abstractmethod
    def sendMessage(self):
        pass


# Componente Concreto
class EmailNotifier(Notifier):
    _name = "Notificacion"

    def sendMessage(self):
        print("se envia notificacion")
        return "Default notificacion"

# Variable de tipo para representar el tipo base (puede ser cualquier subclase de Notifier)
BaseNotifier = TypeVar('BaseNotifier', bound=Notifier)

# Decorador
class NotificationType(Notifier):
    def __init__(self, base: BaseNotifier) -> None:
        # Verificación de tipo del objeto base usando isinstance
        if not isinstance(base, Notifier):
            raise TypeError("El objeto base debe ser una subclase de Notifier")
        self.base = base


# Decoradores Concretos 
class SMSDecorator(NotificationType):
    _name = "SMS_Decorator"

    def sendMessage(self):
        print("Se envia SMS")
        return self.base.sendMessage()
    
class WPPDecorator(NotificationType):
    _name = "WPP_Decorator"
    
    def sendMessage(self):
        print("Se envia WPP")
        return self.base.sendMessage()
    
class NoisyClass():
    pass
    

if __name__ == '__main__':

    noisy_obj = NoisyClass()
    notifier_base = EmailNotifier()
    # wpp_notifier = SMSDecorator(noisy_obj)
    sms_notifier = SMSDecorator(notifier_base)
    wpp_notifier = WPPDecorator(sms_notifier)
    wpp_notifier.sendMessage()
    # wpp_notifier = WPPDecorator(noisy_obj)