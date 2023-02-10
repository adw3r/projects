from module.apis.texts import Text

from unittest import TestCase


class TestTexts(TestCase):

    def test_get_text(self):
        lang = 'ru'
        link = 'google.com'
        project = 'Slottica'
        text: str = '🔥{Получи|Забери|Используй} $spins {фриспинов|FS|freespins|free spins|spins} за {Регистрацию в клубе|Вход в клуб|Вход в проект|принятие участия в проекте|игру} $project {переходя|перейдя|} по {следующей|} ссылке {ниже|} ➡️ $link ⬅️ {Поспеши|Поторопись|Торопись|Не задерживайся}, время действия {бонуса|приза|подарка} {ограничено|лимитировано}!🔥'
        spins = '60'
        text_instance = Text(lang=lang, link=link, project=project, text=text, spins=spins)

        text = text_instance.get_text(target='wezxasqw@gmail.com')
        print(text)
        self.assertTrue(link in text)
        self.assertTrue(project in text)
