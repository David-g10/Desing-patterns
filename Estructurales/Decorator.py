from abc import ABC, abstractmethod

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

# Decorador
class NotificationType(Notifier):
    def __init__(self, base) -> None:
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
    

if __name__ == '__main__':

    notifier_base = EmailNotifier()
    sms_notifier = SMSDecorator(notifier_base)
    wpp_notifier = WPPDecorator(sms_notifier)
    wpp_notifier.sendMessage()