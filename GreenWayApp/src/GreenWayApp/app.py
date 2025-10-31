"""
O projeto Green Way tem como finalidade apoiar a preservação ambiental de forma efetiva, por meio do desenvolvimento de uma aplicação web no modelo SaaS (Software as a Service). A proposta busca estimular a adoção de hábitos sustentáveis no cotidiano dos usuários através de estratégias de gamificação, que despertam a competitividade saudável e favorecem a formação de novos comportamentos ecológicos. Além de incentivar mudanças pessoais, o software apresenta flexibilidade para atender diferentes contextos, educacionais, comunitários e corporativos, ampliando seu alcance como ferramenta de transformação socioambiental. Dessa forma, o Green Way se posiciona como uma solução inovadora, tecnológica e educativa no enfrentamento dos desafios da sustentabilidade contemporânea. 
"""

import toga
from toga.style.pack import COLUMN, ROW


class GreenWay(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return GreenWay()
