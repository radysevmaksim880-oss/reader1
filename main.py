from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

# Устанавливаем темный фон приложения, как в крутых читалках
Window.clearcolor = (0.12, 0.12, 0.12, 1)

class CoolReaderApp(App):
    def build(self):
        # Главный экран
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Верхняя панель с заголовком и кнопками размера шрифта
        top_bar = BoxLayout(size_hint=(1, 0.1), spacing=10)
        
        self.title_label = Label(
            text='Cool Reader Pro — Ваша книга', 
            color=(0.9, 0.9, 0.9, 1), 
            font_size=18,
            halign='left'
        )
        self.title_label.bind(size=self.title_label.setter('text_size'))
        
        btn_minus = Button(text='A-', size_hint=(0.15, 1))
        btn_plus = Button(text='A+', size_hint=(0.15, 1))
        
        btn_minus.bind(on_press=self.decrease_font)
        btn_plus.bind(on_press=self.increase_font)
        
        top_bar.add_widget(self.title_label)
        top_bar.add_widget(btn_minus)
        top_bar.add_widget(btn_plus)
        
        root.add_widget(top_bar)
        
        # Область для текста книги с прокруткой
        scroll = ScrollView(size_hint=(1, 0.85))
        
        sample_text = (
            "Добро пожаловать в вашу собственную читалку!\n\n"
            "Здесь вы сможете комфортно читать любые книги. "
            "Интерфейс сделан максимально простым и темным, чтобы глаза не уставали в темноте.\n\n"
            "В будущем сюда можно будет легко добавить загрузку файлов с телефона, "
            "сохранение страниц и настройки тем оформления.\n\n"
            "Пользуйтесь с удовольствием, Макс!"
        )
        
        self.text_label = Label(
            text=sample_text,
            color=(0.85, 0.85, 0.85, 1),
            font_size=18,
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        # Автоматическая подгонка высоты текста под размер экрана
        self.text_label.bind(width=lambda *x: self.text_label.setter('text_size')(self.text_label, (scroll.width - 20, None)))
        self.text_label.bind(texture_size=lambda *x: setattr(self.text_label, 'height', self.text_label.texture_size[1]))
        
        scroll.add_widget(self.text_label)
        root.add_widget(scroll)
        
        return root

    def increase_font(self, instance):
        if self.text_label.font_size < 32:
            self.text_label.font_size += 2

    def decrease_font(self, instance):
        if self.text_label.font_size > 12:
            self.text_label.font_size -= 2

if __name__ == '__main__':
    CoolReaderApp().run()
