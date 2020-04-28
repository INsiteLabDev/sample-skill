from mycroft import MycroftSkill, intent_file_handler


class Sample(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sample.intent')
    def handle_sample(self, message):
        self.speak_dialog('sample')


def create_skill():
    return Sample()

