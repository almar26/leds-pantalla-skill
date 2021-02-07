from mycroft import MycroftSkill, intent_file_handler


class LedsPantalla(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pantalla.leds.intent')
    def handle_pantalla_leds(self, message):
        self.speak_dialog('pantalla.leds')


def create_skill():
    return LedsPantalla()

