#!/usr/bin/python3
# -*- coding: utf-8 -*-
#

#######################################################################
#
# Initial home screen
#
#######################################################################


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QListWidget, QLineEdit, QListWidgetItem, QPlainTextEdit

from skymelchat import paths, chat_screen
from skymelchat.translation import _


def add_widgets(self):
    self.home_screen_widget = QWidget()
    self.home_screen_widget.setLayout(QVBoxLayout())
    self.home_screen_widget.layout().setContentsMargins(0, 0, 0, 0)

    self.home_screen_logo_line = QWidget()
    self.home_screen_logo_line.setObjectName('home_screen_logo_line')
    self.home_screen_logo_line.setLayout(QHBoxLayout())
    self.home_screen_logo_line.layout().addStretch()

    self.home_screen_logo = QLabel()
    self.home_screen_logo.setObjectName('home_screen_logo')
    self.home_screen_logo.setPixmap(QPixmap(paths.get_graphics_path('skymel_logo.svg')).scaled(QSize(150, 70), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
    self.home_screen_logo.setScaledContents(True)
    self.home_screen_logo_line.layout().addWidget(self.home_screen_logo, 0, Qt.AlignmentFlag.AlignCenter)

    self.home_screen_logo_line.layout().addStretch()
    self.home_screen_widget.layout().addWidget(self.home_screen_logo_line)

    self.home_screen_wallet_list_frame = QWidget()
    self.home_screen_wallet_list_frame.setVisible(False)
    self.home_screen_wallet_list_frame.setObjectName('home_screen_wallet_list_frame')
    self.home_screen_wallet_list_frame.setLayout(QVBoxLayout())
    self.home_screen_wallet_list_frame.layout().setContentsMargins(0, 0, 0, 0)

    self.home_screen_select_wallet_label = QLabel()
    self.home_screen_select_wallet_label.setObjectName('home_screen_select_wallet_label')
    self.home_screen_wallet_list_frame.layout().addWidget(self.home_screen_select_wallet_label, 0, Qt.AlignmentFlag.AlignCenter)

    self.home_screen_wallets_list = QListWidget()
    self.home_screen_wallets_list.currentItemChanged.connect(lambda: home_screen_wallets_list_currentitemchanged(self))
    self.home_screen_wallets_list.activated.connect(lambda: home_screen_wallets_list_activated(self))
    self.home_screen_wallet_list_frame.layout().addWidget(self.home_screen_wallets_list, 1)

    self.home_screen_wallets_list_bottom_line = QWidget()
    self.home_screen_wallets_list_bottom_line.setLayout(QHBoxLayout())
    self.home_screen_wallets_list_bottom_line.layout().setContentsMargins(10, 10, 10, 10)
    self.home_screen_wallets_list_bottom_line.layout().setSpacing(10)
    self.home_screen_wallets_list_bottom_line.layout().addStretch()

    self.home_screen_wallets_list_bottom_line_remove_button = QPushButton('-')
    self.home_screen_wallets_list_bottom_line_remove_button.setObjectName('home_screen_wallets_list_bottom_line_remove_button')
    self.home_screen_wallets_list_bottom_line_remove_button.setProperty('class', 'secondary')
    self.home_screen_wallets_list_bottom_line_remove_button.clicked.connect(lambda: home_screen_wallets_list_bottom_line_remove_button_clicked(self))
    self.home_screen_wallets_list_bottom_line.layout().addWidget(self.home_screen_wallets_list_bottom_line_remove_button)

    self.home_screen_wallets_list_bottom_line_add_button = QPushButton('+')
    self.home_screen_wallets_list_bottom_line_add_button.setObjectName('home_screen_wallets_list_bottom_line_add_button')
    self.home_screen_wallets_list_bottom_line_add_button.clicked.connect(lambda: home_screen_wallets_list_bottom_line_add_button_clicked(self))
    self.home_screen_wallets_list_bottom_line.layout().addWidget(self.home_screen_wallets_list_bottom_line_add_button)

    self.home_screen_wallets_list_bottom_line.layout().addStretch()
    self.home_screen_wallet_list_frame.layout().addWidget(self.home_screen_wallets_list_bottom_line)

    self.home_screen_widget.layout().addWidget(self.home_screen_wallet_list_frame, 1)

    self.home_screen_wallet_add_frame = QWidget()
    self.home_screen_wallet_add_frame.setVisible(False)
    self.home_screen_wallet_add_frame.setObjectName('home_screen_wallet_add_frame')
    self.home_screen_wallet_add_frame.setLayout(QVBoxLayout())
    self.home_screen_wallet_add_frame.layout().setContentsMargins(20, 20, 20, 20)
    self.home_screen_wallet_add_frame.layout().addStretch()

    self.home_screen_wallet_add_label = QLabel()
    self.home_screen_wallet_add_label.setObjectName('home_screen_wallet_add_label')
    self.home_screen_wallet_add_frame.layout().addWidget(self.home_screen_wallet_add_label, 0, Qt.AlignmentFlag.AlignCenter)

    self.home_screen_wallets_add_lineedit = QPlainTextEdit()
    self.home_screen_wallets_add_lineedit.setObjectName('home_screen_wallets_add_lineedit')
    self.home_screen_wallets_add_lineedit.textChanged.connect(lambda: home_screen_wallets_add_lineedit_textedited(self))
    self.home_screen_wallet_add_frame.layout().addWidget(self.home_screen_wallets_add_lineedit, 1)

    self.home_screen_wallets_add_cancel_confirm_line = QWidget()
    self.home_screen_wallets_add_cancel_confirm_line.setObjectName('home_screen_wallets_add_cancel_confirm_line')
    self.home_screen_wallets_add_cancel_confirm_line.setLayout(QHBoxLayout())
    self.home_screen_wallets_add_cancel_confirm_line.layout().addStretch()

    self.home_screen_wallets_add_cancel_button = QPushButton('Cancel')
    self.home_screen_wallets_add_cancel_button.setProperty('class', 'secondary')
    self.home_screen_wallets_add_cancel_button.setObjectName('home_screen_wallets_add_cancel_button')
    self.home_screen_wallets_add_cancel_button.clicked.connect(lambda: home_screen_wallets_add_cancel_button_clicked(self))
    self.home_screen_wallets_add_cancel_confirm_line.layout().addWidget(self.home_screen_wallets_add_cancel_button)

    self.home_screen_wallets_add_confirm_button = QPushButton('Confirm')
    self.home_screen_wallets_add_confirm_button.setObjectName('home_screen_wallets_add_confirm_button')
    self.home_screen_wallets_add_confirm_button.clicked.connect(lambda: home_screen_wallets_add_confirm_button_clicked(self))
    self.home_screen_wallets_add_cancel_confirm_line.layout().addWidget(self.home_screen_wallets_add_confirm_button)
    home_screen_wallets_add_lineedit_check(self)

    self.home_screen_wallets_add_cancel_confirm_line.layout().addStretch()
    self.home_screen_wallet_add_frame.layout().addWidget(self.home_screen_wallets_add_cancel_confirm_line)

    self.home_screen_wallet_add_frame.layout().addStretch()

    self.home_screen_widget.layout().addWidget(self.home_screen_wallet_add_frame, 1)

    self.main_widget.addWidget(self.home_screen_widget)


def update_widgets(self):
    self.home_screen_wallet_list_frame.setVisible(bool(paths.SETTINGS['available_wallets']))
    self.home_screen_wallet_add_frame.setVisible(not bool(paths.SETTINGS['available_wallets']))
    self.home_screen_wallets_add_cancel_button.setVisible(bool(paths.SETTINGS['available_wallets']))
    update_wallets_list(self)


def update_wallets_list(self):
    self.home_screen_wallets_list.clear()
    for wallet in paths.SETTINGS['available_wallets']:
        self.home_screen_wallets_list.addItem(QListWidgetItem(QIcon(paths.get_graphics_path('wallet_icon.svg')), wallet))


def show_screen(self):
    self.main_widget.setCurrentWidget(self.home_screen_widget)
    update_widgets(self)


def home_screen_wallets_add_cancel_button_clicked(self):
    update_widgets(self)


def home_screen_wallets_add_confirm_button_clicked(self):
    paths.SETTINGS['available_wallets'].append(self.home_screen_wallets_add_lineedit.toPlainText())
    update_widgets(self)


def home_screen_wallets_add_lineedit_check(self):
    self.home_screen_wallets_add_confirm_button.setEnabled(bool(self.home_screen_wallets_add_lineedit.toPlainText()))


def home_screen_wallets_add_lineedit_textedited(self):
    home_screen_wallets_add_lineedit_check(self)


def home_screen_wallets_list_bottom_line_remove_button_clicked(self):
    paths.SETTINGS['available_wallets'].remove(self.home_screen_wallets_list.currentItem().text())
    update_widgets(self)


def home_screen_wallets_list_bottom_line_add_button_clicked(self):
    self.home_screen_wallet_list_frame.setVisible(False)
    self.home_screen_wallet_add_frame.setVisible(True)


def home_screen_wallets_list_currentitemchanged(self):
    self.home_screen_wallets_list_bottom_line_remove_button.setVisible(bool(self.home_screen_wallets_list.currentItem()))


def home_screen_wallets_list_activated(self):
    paths.SESSION['selected_wallet'] = self.home_screen_wallets_list.currentItem().text()
    chat_screen.show_screen(self)


def translate_widgets(self):
    self.home_screen_select_wallet_label.setText(_('home_screen.select_wallet'))
    self.home_screen_wallet_add_label.setText(_('home_screen.add_wallet'))
    self.home_screen_wallets_add_cancel_button.setText(_('home_screen.cancel'))
    self.home_screen_wallets_add_confirm_button.setText(_('home_screen.confirm'))