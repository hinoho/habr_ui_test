import io
import time

import allure
from PIL.Image import Resampling
from allure_commons.types import AttachmentType
from PIL import Image



class BasePage:
    img_index = 1
    page_element = ""  # Уникальный элемент на странице (css селектор), который присутствует на ней и только на ней
    parent_element = None  # Родительский элемент, содержащий данный (пример: страница заказов для формы поиска)
    base_url = 'https://habr.com/'

    def __init__(self, page):
        self.page = page
        self.check_page()

    def set_parent(self, parent):
        self.parent_element = parent
        return self

    def check_page(self, screen=True):
        with allure.step(f"Базовая проверка элемента {type(self).__name__}"):
            if self.page_element != '':
                with allure.step(f"Проверка наличия элемента {self.page_element}"):
                    try:
                        self.page.wait_for_selector(self.page_element, state='attached')
                    except Exception as ex:
                        self.screenshot('error_check_page_element')
                        raise Exception(
                            f"Функция check_element недождалась элемента {self.page_element}:\n{ex}") from ex

            if screen:
                self.screenshot(type(self).__name__ + '_opened')

        return self

    def screenshot(self, name=None, full_page=False, locator=None):
        if name is None:
            path = f"images/{BasePage.img_index.__str__()}_img_.png"
        else:
            path = f"images/{BasePage.img_index}_img_{name}.png"

        if locator is None:
            try:
                img = self.page.screenshot(path=path, full_page=full_page)
            except Exception:
                time.sleep(1)
                img = self.page.screenshot(path=path, full_page=full_page)
        else:
            try:
                img = self.page.locator(locator).screenshot(path=path)
            except Exception as ex:
                self.screenshot('error_locator_screenshot')
                raise Exception(f'Невозможно создать скриншот элемента с локатором "{locator}":\n{ex}') from ex

        with open(path, "wb") as fh:
            fh.write(img)

        img_tmp = Image.open(path)
        basewidth = 1000
        if int(img_tmp.size[0]) > int(basewidth):
            wpercent = (basewidth / float(img_tmp.size[0]))
            hsize = int(float(img_tmp.size[1]) * float(wpercent))
            img_tmp = img_tmp.resize((basewidth, hsize),  Resampling.LANCZOS )
            img_tmp.save(path)

        bytes_io = io.BytesIO()
        img_tmp.save(bytes_io, format='PNG')
        img = bytes_io.getvalue()

        allure.attach(img, path, attachment_type=AttachmentType.PNG)
        BasePage.img_index = BasePage.img_index + 1

        return path

    def wait_for_selector(self, css, state='visible', timeout=None):
        try:
            self.page.wait_for_selector(css, state=state, timeout=timeout)
        except Exception as ex:
            self.screenshot('error_wait_for_selector')
            raise Exception(f"Невозможно дождаться элемент по селектору = {css}:\n{ex}") from ex

        return self

    def click(self, css, el_name=None, force=True, position=None, button='left'):
        mess = f"Нажать элемент, css = {css}" if el_name is None else f"Нажать [{el_name}], css = {css}"
        with allure.step(mess):
            if not force:
                self.wait_for_selector(css)
            try:
                self.page.click(css, force=force, position=position, button=button)
            except Exception as ex:
                self.screenshot('error_click')
                raise Exception(f"Невозможно нажать элемент по селектору = {css}:\n{ex}") from ex

        return self

    def expect_request_finished(self, url_or_predicate):
        return self.page.expect_request_finished(url_or_predicate)