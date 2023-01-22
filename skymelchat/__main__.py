#!/usr/bin/python3
# -*- coding: utf-8 -*-

#######################################################################
#
# Main interface, calling all necessary modules
#
#######################################################################


import os
import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow
from PyQt6.QtGui import QFontDatabase, QIcon

import skymelchat
from skymelchat import home_screen, settings, paths, translation, chat_screen


class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle(skymelchat.__appname__)
        self.setWindowIcon(QIcon(paths.get_graphics_path('icons/scalable/{}'.format(skymelchat.__desktopid__))))
        # # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.WindowFullScreen)

        # # Defining some "global" variables
        settings.load_settings()
        translation.load_translation_files()
        # self.selected_language = self.settings.get('language', 'en')
        translation.set_language('en')

        # # Initializing camera settings and camera image grab function
        # self.camera_dict_of_devices = camera.get_list_of_devices(self.settings)
        # self.camera_thread = camera.camera_thread(parent=self)

        # def camera_thread_pixmap_changed(image):
        #     if self.calibration_screen_widget.isVisible():
        #         calibration_screen.camera_pixmap_changed(self, image)
        #     elif self.inspection_screen_widget.isVisible():
        #         inspection_screen.camera_pixmap_changed(self, image)
        #     elif self.integrate_new_product_widget.isVisible():
        #         integrate_new_product_screen.camera_pixmap_changed(self, image)

        # self.camera_thread.change_pixmap.connect(camera_thread_pixmap_changed)

        # # Reseting values for selected camera if camera is not connected
        # if self.settings.get('camera', False) == "genicam" and not self.settings.get('camera_genicam_device', '') in [device_name._property_dict.get('display_name', '') for device_name in self.camera_dict_of_devices['GenICam']]:
        #     del self.settings['camera']
        #     del self.settings['camera_genicam_device']
        # elif self.settings.get('camera', False) and not self.settings.get('camera', False) == "genicam" and not self.settings.get('camera', '') in self.camera_dict_of_devices.values():
        #     del self.settings['camera']

        # if 'camera' in self.settings:
        #     camera.start_webcam(self.camera_thread, self.settings)
        #     self.camera_thread.is_live = True
        #     self.camera_thread.start()
        # # else:
        # #     print('alert')
        # # End of camera calls on startup

        # if args.debug:
        #     self.api_instance = DummyAPI.instance(server=self.settings.get('api_server', 'localhost'), port=self.settings.get('api_port', 12345), station_id=self.settings.get('station_id', 1), secret=self.settings.get('api_key', 'dev'))
        # else:
        #     self.api_instance = RealAPI.instance(server=self.settings.get('api_server', 'localhost'), port=self.settings.get('api_port', 12345), station_id=self.settings.get('station_id', 1), secret=self.settings.get('api_key', 'dev'))

        # self.api_server = ApiServer(self.settings)
        # self.api_server.set_product_id_triggered.connect(lambda new_name: self.handle_set_product_id(new_name))

        for font in os.listdir(paths.PATH_SKYMELCHAT_GRAPHICS):
            if font.lower().endswith(('.ttf')):
                QFontDatabase.addApplicationFont(os.path.join(paths.PATH_SKYMELCHAT_GRAPHICS, font))

        with open(os.path.join(paths.PATH_SKYMELCHAT_GRAPHICS, 'stylesheet.qss')) as stylesheet_file:
            self.setStyleSheet(stylesheet_file.read().replace('PATH_SKYMELCHAT_GRAPHICS/', paths.get_graphics_path('_')[:-1]))

        self.main_widget = QStackedWidget(self)
        self.main_widget.setObjectName(u"main_widget")
        self.setCentralWidget(self.main_widget)

        home_screen.add_widgets(self)
        chat_screen.add_widgets(self)

        home_screen.show_screen(self)


        self.main_widget.adjustSize()

        self.translate_widgets()

        # if self.settings.get('fullscreen', False):
        #     self.showFullScreen()
        # else:
        #     self.setMinimumSize(QSize(800, 480))
        #     self.show()
        self.show()

    def closeEvent(self, event):
        settings.save_settings(paths.SETTINGS)
        event.accept()

    def translate_widgets(self):
        home_screen.translate_widgets(self)
        chat_screen.translate_widgets(self)


def main():
    for k, v in os.environ.items():
        if k.startswith("QT_") and "cv2" in v:
            del os.environ[k]

    app = QApplication(sys.argv)
    # app.setApplicationName(skymelchat.__appname__)
    # app.setApplicationVersion(skymelchat.__version__)
    # app.setDesktopFileName(skymelchat.__desktopid__)
    # app.setOrganizationDomain(skymelchat.__domain__)
    app.setQuitOnLastWindowClosed(True)
    app.setStyle("Fusion")

    win = mainWindow()
    win.stylename = app.style().objectName().lower()

    exit_code = app.exec()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
