#!/usr/bin/python3
# -*- coding: utf-8 -*-

#######################################################################
#
# Chat screen
#
#######################################################################

import time
import random
import datetime

# lorem is only used for the purpose of demonstration
import lorem

from PyQt6.QtCore import QSize, Qt, QThread, pyqtSignal
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout, QWidget, QListWidget, QLineEdit, QSplitter, QPlainTextEdit, QListWidgetItem, QSizePolicy, QProgressBar, QMenu

from skymelchat import paths
from skymelchat.translation import _


class retrieve_conversations_thread(QThread):
    response = pyqtSignal(list)
    wallet = ''

    def run(self):
        if self.wallet:
            time.sleep(random.uniform(1, 2))
            for dummy_conversation in range(8):
                result = [
                    {
                        'wallet': ''.join(random.choice('0123456789ABCDEF') for i in range(16)),
                        'nickname': random.choice(lorem.sentence().split(' ')).capitalize(),
                        'chat_history': [],
                        'unread_messages': 0,
                        'status': 'active'
                    }
                ]
                time.sleep(random.uniform(.2, 1.2))
                self.response.emit(result)


class retrieve_chat_history_thread(QThread):
    response = pyqtSignal(list)
    status = pyqtSignal(float)
    wallet = ''

    def run(self):
        if self.wallet:
            for i in range(10):
                self.status.emit(i/10)
                time.sleep(random.uniform(.01, .2))

            self.response.emit(
                [
                    {
                        'wallet': self.wallet,
                        'id': 0,
                        'timestamp': datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
                        'status': 'alert',
                        'message': 'Chat started'
                    }
                ]
            )

class chat_listener_thread(QThread):
    response = pyqtSignal(dict)
    wallets = []

    def run(self):
        while self.wallets:
            wallet = random.choice(self.wallets)
            time.sleep(random.uniform(2, 3))
            self.response.emit(
                {
                    'wallet': wallet,
                    'id': 0,
                    'timestamp': datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
                    'status': 'received',
                    'message': lorem.sentence()
                }
            )


class chat_sender_thread(QThread):
    response = pyqtSignal(dict)
    progress = pyqtSignal(float)
    sent = pyqtSignal(bool)
    message = ''
    wallet = ''

    def run(self):
        if self.message and self.wallet:
            for i in range(10):
                self.progress.emit(i/10)
                time.sleep(random.uniform(.01, .2))

            self.sent.emit(True)

            self.response.emit(
                {
                    'wallet': self.wallet,
                    'id': 0,
                    'timestamp': datetime.datetime.now().strftime('%Y%m%d%H%M%S'),
                    'status': random.choice(['sent', 'readed', 'error']),
                    'message': self.message
                }
            )




def add_widgets(self):
    self.chat_screen_widget = QWidget()
    self.chat_screen_widget.setObjectName('chat_screen_widget')
    self.chat_screen_widget.setLayout(QHBoxLayout())
    self.chat_screen_widget.layout().setContentsMargins(0, 0, 0, 0)

    self.chat_screen_widget_splitter = QSplitter()

    self.chat_screen_list_frame = QWidget()
    self.chat_screen_list_frame.setObjectName('chat_screen_list_frame')
    self.chat_screen_list_frame.setLayout(QVBoxLayout())
    self.chat_screen_list_frame.layout().setContentsMargins(0, 0, 0, 0)
    self.chat_screen_list_frame.layout().setSpacing(0)

    self.chat_screen_list_frame_avatar_line = QWidget()
    self.chat_screen_list_frame_avatar_line.setObjectName('chat_screen_list_frame_avatar_line')
    self.chat_screen_list_frame_avatar_line.setLayout(QHBoxLayout())
    self.chat_screen_list_frame_avatar_line.layout().setContentsMargins(10, 10, 10, 10)
    self.chat_screen_list_frame_avatar_line.layout().setSpacing(10)

    self.chat_screen_list_frame_avatar_line_icon = QLabel()
    self.chat_screen_list_frame_avatar_line_icon.setObjectName('chat_screen_list_frame_avatar_line_icon')
    self.chat_screen_list_frame_avatar_line_icon.setFixedSize(QSize(64, 64))
    self.chat_screen_list_frame_avatar_line_icon.setPixmap(QPixmap(paths.get_graphics_path('generic_avatar.svg')).scaled(QSize(64, 64), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
    self.chat_screen_list_frame_avatar_line.layout().addWidget(self.chat_screen_list_frame_avatar_line_icon)

    self.chat_screen_list_frame_avatar_line_name = QLabel()
    self.chat_screen_list_frame_avatar_line_name.setObjectName('chat_screen_list    _frame_avatar_line_name')
    self.chat_screen_list_frame_avatar_line_name.setWordWrap(True)
    self.chat_screen_list_frame_avatar_line.layout().addWidget(self.chat_screen_list_frame_avatar_line_name)

    self.chat_screen_list_frame.layout().addWidget(self.chat_screen_list_frame_avatar_line)

    self.chat_screen_list_frame_conversations_list = QListWidget()
    self.chat_screen_list_frame_conversations_list.setObjectName('chat_screen_list_frame_conversations_list')
    self.chat_screen_list_frame_conversations_list.activated.connect(lambda: chat_screen_list_frame_conversations_list_activated(self))
    self.chat_screen_list_frame_conversations_list.currentItemChanged.connect(lambda: chat_screen_list_frame_conversations_list_currentitemchanged(self))
    self.chat_screen_list_frame_conversations_list.horizontalScrollBar().setEnabled(False)
    self.chat_screen_list_frame.layout().addWidget(self.chat_screen_list_frame_conversations_list, 1)

    self.chat_screen_list_frame_conversations_list_menu = QMenu()
    self.chat_screen_list_frame_conversations_list_menu_remove_action = self.chat_screen_list_frame_conversations_list_menu.addAction(_('chat_screen.remove_action'))
    self.chat_screen_list_frame_conversations_list_menu_remove_action.triggered.connect(lambda: chat_screen_list_frame_conversations_list_menu_remove_action_clicked(self))

    self.chat_screen_list_frame_conversations_list_menu_block_action = self.chat_screen_list_frame_conversations_list_menu.addAction(_('chat_screen.block_action'))
    self.chat_screen_list_frame_conversations_list_menu_block_action.triggered.connect(lambda: chat_screen_list_frame_conversations_list_menu_block_action_clicked(self))

    self.chat_screen_list_frame_conversations_list_menu_message_action = self.chat_screen_list_frame_conversations_list_menu.addAction(_('chat_screen.message_action'))
    self.chat_screen_list_frame_conversations_list_menu_message_action.triggered.connect(lambda: chat_screen_list_frame_conversations_list_menu_message_action_clicked(self))

    self.chat_screen_list_frame_conversations_list.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
    self.chat_screen_list_frame_conversations_list.addActions([self.chat_screen_list_frame_conversations_list_menu_remove_action, self.chat_screen_list_frame_conversations_list_menu_block_action, self.chat_screen_list_frame_conversations_list_menu_message_action])

    self.chat_screen_list_frame_conversations_bottom_line = QWidget()
    self.chat_screen_list_frame_conversations_bottom_line.setLayout(QHBoxLayout())
    self.chat_screen_list_frame_conversations_bottom_line.layout().setContentsMargins(10, 10, 10, 10)
    self.chat_screen_list_frame_conversations_bottom_line.layout().setSpacing(10)
    self.chat_screen_list_frame_conversations_bottom_line.layout().addStretch()

    self.chat_screen_list_frame_conversations_bottom_line_remove_button = QPushButton('-')
    self.chat_screen_list_frame_conversations_bottom_line_remove_button.setObjectName('chat_screen_list_frame_conversations_bottom_line_remove_button')
    self.chat_screen_list_frame_conversations_bottom_line_remove_button.setProperty('class', 'secondary')
    self.chat_screen_list_frame_conversations_bottom_line_remove_button.clicked.connect(lambda: chat_screen_list_frame_conversations_bottom_line_remove_button_clicked(self))
    self.chat_screen_list_frame_conversations_bottom_line.layout().addWidget(self.chat_screen_list_frame_conversations_bottom_line_remove_button)

    self.chat_screen_list_frame_conversations_bottom_line_add_button = QPushButton('+')
    self.chat_screen_list_frame_conversations_bottom_line_add_button.setObjectName('chat_screen_list_frame_conversations_bottom_line_add_button')
    self.chat_screen_list_frame_conversations_bottom_line_add_button.clicked.connect(lambda: chat_screen_list_frame_conversations_bottom_line_add_button_clicked(self))
    self.chat_screen_list_frame_conversations_bottom_line.layout().addWidget(self.chat_screen_list_frame_conversations_bottom_line_add_button)

    self.chat_screen_list_frame_conversations_bottom_line.layout().addStretch()
    self.chat_screen_list_frame.layout().addWidget(self.chat_screen_list_frame_conversations_bottom_line)

    self.chat_screen_list_add_frame = QWidget()
    self.chat_screen_list_add_frame.setVisible(False)
    self.chat_screen_list_add_frame.setObjectName('chat_screen_list_add_frame')
    self.chat_screen_list_add_frame.setLayout(QVBoxLayout())
    self.chat_screen_list_add_frame.layout().setContentsMargins(20, 20, 20, 20)
    self.chat_screen_list_add_frame.layout().addStretch()

    self.chat_screen_list_add_nickname_label = QLabel()
    self.chat_screen_list_add_nickname_label.setObjectName('chat_screen_list_add_nickname_label')
    self.chat_screen_list_add_frame.layout().addWidget(self.chat_screen_list_add_nickname_label, 0, Qt.AlignmentFlag.AlignCenter)

    self.chat_screen_list_add_nickname_lineedit = QLineEdit()
    self.chat_screen_list_add_nickname_lineedit.setObjectName('chat_screen_list_add_nickname_lineedit')
    self.chat_screen_list_add_nickname_lineedit.textChanged.connect(lambda: chat_screen_list_add_textedited(self))
    self.chat_screen_list_add_frame.layout().addWidget(self.chat_screen_list_add_nickname_lineedit, 1)

    self.chat_screen_list_add_wallet_label = QLabel()
    self.chat_screen_list_add_wallet_label.setObjectName('chat_screen_list_add_wallet_label')
    self.chat_screen_list_add_frame.layout().addWidget(self.chat_screen_list_add_wallet_label, 0, Qt.AlignmentFlag.AlignCenter)

    self.chat_screen_list_add_wallet_lineedit = QPlainTextEdit()
    self.chat_screen_list_add_wallet_lineedit.setObjectName('chat_screen_list_add_wallet_lineedit')
    self.chat_screen_list_add_wallet_lineedit.textChanged.connect(lambda: chat_screen_list_add_textedited(self))
    self.chat_screen_list_add_frame.layout().addWidget(self.chat_screen_list_add_wallet_lineedit, 1)

    self.chat_screen_list_add_cancel_confirm_line = QWidget()
    self.chat_screen_list_add_cancel_confirm_line.setObjectName('chat_screen_list_add_cancel_confirm_line')
    self.chat_screen_list_add_cancel_confirm_line.setLayout(QHBoxLayout())
    self.chat_screen_list_add_cancel_confirm_line.layout().addStretch()

    self.chat_screen_list_add_cancel_button = QPushButton('Cancel')
    self.chat_screen_list_add_cancel_button.setProperty('class', 'secondary')
    self.chat_screen_list_add_cancel_button.setObjectName('chat_screen_list_add_cancel_button')
    self.chat_screen_list_add_cancel_button.clicked.connect(lambda: chat_screen_list_add_cancel_button_clicked(self))
    self.chat_screen_list_add_cancel_confirm_line.layout().addWidget(self.chat_screen_list_add_cancel_button)

    self.chat_screen_list_add_confirm_button = QPushButton('Confirm')
    self.chat_screen_list_add_confirm_button.setObjectName('chat_screen_list_add_confirm_button')
    self.chat_screen_list_add_confirm_button.clicked.connect(lambda: chat_screen_list_add_confirm_button_clicked(self))
    self.chat_screen_list_add_cancel_confirm_line.layout().addWidget(self.chat_screen_list_add_confirm_button)
    # chat_screen_list_add_lineedit_check(self)

    self.chat_screen_list_add_cancel_confirm_line.layout().addStretch()
    self.chat_screen_list_add_frame.layout().addWidget(self.chat_screen_list_add_cancel_confirm_line)

    self.chat_screen_list_add_frame.layout().addStretch()

    self.chat_screen_list_frame.layout().addWidget(self.chat_screen_list_add_frame, 1)

    self.chat_screen_list_frame_conversations_loading_message = QLabel()
    self.chat_screen_list_frame_conversations_loading_message.setObjectName('chat_screen_list_frame_conversations_loading_message')
    self.chat_screen_list_frame_conversations_loading_message.setWordWrap(True)
    self.chat_screen_list_frame_conversations_loading_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.chat_screen_list_frame.layout().addWidget(self.chat_screen_list_frame_conversations_loading_message, 1)

    self.chat_screen_widget_splitter.addWidget(self.chat_screen_list_frame)

    self.chat_screen_conversation_frame = QWidget()
    self.chat_screen_conversation_frame.setObjectName('chat_screen_conversation_frame')
    self.chat_screen_conversation_frame.setLayout(QVBoxLayout())
    self.chat_screen_conversation_frame.layout().setContentsMargins(0, 0, 0, 0)

    self.chat_screen_conversation_frame_chat = QListWidget()
    self.chat_screen_conversation_frame_chat.setObjectName('chat_screen_conversation_frame_chat')
    self.chat_screen_conversation_frame_chat.setAutoScroll(True)
    self.chat_screen_conversation_frame.layout().addWidget(self.chat_screen_conversation_frame_chat, 1)

    self.chat_screen_conversation_frame_connecting_message_line = QWidget()
    self.chat_screen_conversation_frame_connecting_message_line.setObjectName('chat_screen_conversation_frame_connecting_message_line')
    self.chat_screen_conversation_frame_connecting_message_line.setLayout(QVBoxLayout())
    self.chat_screen_conversation_frame_connecting_message_line.layout().setContentsMargins(10, 10, 10, 10)
    self.chat_screen_conversation_frame_connecting_message_line.layout().setSpacing(10)
    self.chat_screen_conversation_frame_connecting_message_line.layout().addStretch()

    self.chat_screen_conversation_frame_connecting_message_label = QLabel()
    self.chat_screen_conversation_frame_connecting_message_label.setObjectName('chat_screen_conversation_frame_connecting_message_label')
    self.chat_screen_conversation_frame_connecting_message_label.setWordWrap(True)
    self.chat_screen_conversation_frame_connecting_message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.chat_screen_conversation_frame_connecting_message_line.layout().addWidget(self.chat_screen_conversation_frame_connecting_message_label)

    self.chat_screen_conversation_frame_connecting_message_progressbar = QProgressBar()
    self.chat_screen_conversation_frame_connecting_message_progressbar.setObjectName('chat_screen_conversation_frame_connecting_message_progressbar')
    self.chat_screen_conversation_frame_connecting_message_progressbar.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.chat_screen_conversation_frame_connecting_message_line.layout().addWidget(self.chat_screen_conversation_frame_connecting_message_progressbar)
    self.chat_screen_conversation_frame_connecting_message_line.layout().addStretch()

    self.chat_screen_conversation_frame.layout().addWidget(self.chat_screen_conversation_frame_connecting_message_line)
    self.chat_screen_conversation_frame_connecting_message_line.layout().addStretch()

    self.chat_screen_conversation_frame_sending_message_progressbar = QProgressBar()
    self.chat_screen_conversation_frame_sending_message_progressbar.setLayout(QVBoxLayout())
    self.chat_screen_conversation_frame_sending_message_progressbar.layout().setContentsMargins(0, 0, 0, 0)
    self.chat_screen_conversation_frame_sending_message_progressbar.setObjectName('chat_screen_conversation_frame_sending_message_progressbar')
    self.chat_screen_conversation_frame_sending_message_progressbar.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.chat_screen_conversation_frame_sending_message_progressbar.setTextVisible(False)

    self.chat_screen_conversation_frame_sending_message_progressbar_label = QLabel()
    self.chat_screen_conversation_frame_sending_message_progressbar_label.setObjectName('chat_screen_conversation_frame_sending_message_progressbar_label')
    self.chat_screen_conversation_frame_sending_message_progressbar.layout().addWidget(self.chat_screen_conversation_frame_sending_message_progressbar_label, 0, Qt.AlignmentFlag.AlignCenter)

    self.chat_screen_conversation_frame.layout().addWidget(self.chat_screen_conversation_frame_sending_message_progressbar)

    self.chat_screen_conversation_frame_message_line = QWidget()
    self.chat_screen_conversation_frame_message_line.setObjectName('chat_screen_conversation_frame_message_line')
    self.chat_screen_conversation_frame_message_line.setLayout(QHBoxLayout())
    self.chat_screen_conversation_frame_message_line.layout().setContentsMargins(10, 10, 10, 10)
    self.chat_screen_conversation_frame_message_line.layout().setSpacing(10)

    self.chat_screen_conversation_frame_message_textedit = QPlainTextEdit()
    self.chat_screen_conversation_frame_message_textedit.setObjectName('chat_screen_conversation_frame_message_textedit')
    self.chat_screen_conversation_frame_message_textedit.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum))
    self.chat_screen_conversation_frame_message_textedit.textChanged.connect(lambda: chat_screen_conversation_frame_message_textedit_textchanged(self))
    self.chat_screen_conversation_frame_message_line.layout().addWidget(self.chat_screen_conversation_frame_message_textedit, 1)

    self.chat_screen_conversation_frame_message_send_button = QPushButton()
    self.chat_screen_conversation_frame_message_send_button.setObjectName('chat_screen_conversation_frame_message_send_button')
    self.chat_screen_conversation_frame_message_send_button.clicked.connect(lambda: chat_screen_conversation_frame_message_send_button_clicked(self))
    self.chat_screen_conversation_frame_message_line.layout().addWidget(self.chat_screen_conversation_frame_message_send_button)

    self.chat_screen_conversation_frame.layout().addWidget(self.chat_screen_conversation_frame_message_line)

    self.chat_screen_conversation_frame_select_chat_alert = QLabel()
    self.chat_screen_conversation_frame_select_chat_alert.setObjectName('chat_screen_conversation_frame_select_chat_alert')
    self.chat_screen_conversation_frame_select_chat_alert.setWordWrap(True)
    self.chat_screen_conversation_frame_select_chat_alert.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.chat_screen_conversation_frame.layout().addWidget(self.chat_screen_conversation_frame_select_chat_alert, 1)

    self.chat_screen_widget_splitter.addWidget(self.chat_screen_conversation_frame)
    self.chat_screen_widget_splitter.setSizes([200, 400])

    self.chat_screen_widget.layout().addWidget(self.chat_screen_widget_splitter)

    self.main_widget.addWidget(self.chat_screen_widget)

    def retrieve_conversations_thread_response(response):
        for conv in response:
            if not conv['wallet'] in paths.SESSION['conversations']:
                paths.SESSION['conversations'][conv['wallet']] = conv
        update_widgets(self)

    self.retrieve_conversations_thread = retrieve_conversations_thread()
    self.retrieve_conversations_thread.response.connect(retrieve_conversations_thread_response)

    def retrieve_chat_history_thread_status(response):
        self.chat_screen_conversation_frame_connecting_message_progressbar.setValue(int(response * 100))

    def retrieve_chat_history_thread_response(response):
        for conv in paths.SESSION['conversations']:
            for resp_conv in response:
                if conv == resp_conv['wallet']:
                    paths.SESSION['conversations'][conv]['chat_history'] += [resp_conv]
        update_widgets(self)

        if not paths.SESSION['selected_conversation'] in self.chat_listener_thread.wallets:
            self.chat_listener_thread.wallets.append(paths.SESSION['selected_conversation']['wallet'])

        if self.chat_listener_thread.wallets and not self.chat_listener_thread.isRunning():
            self.chat_listener_thread.start()

    self.retrieve_chat_history_thread = retrieve_chat_history_thread()
    self.retrieve_chat_history_thread.status.connect(retrieve_chat_history_thread_status)
    self.retrieve_chat_history_thread.response.connect(retrieve_chat_history_thread_response)

    def chat_listener_thread_response(response):
        for conv in paths.SESSION['conversations']:
            if conv == response['wallet']:
                paths.SESSION['conversations'][conv]['chat_history'] += [response]

        if paths.SESSION['selected_conversation'] and paths.SESSION['selected_conversation']['wallet'] == response['wallet']:
            chat_screen_conversation_frame_chat_update(self, message=response)
        elif response['wallet'] in paths.SESSION['conversations']:
            paths.SESSION['conversations'][response['wallet']]['unread_messages'] += 1
            update_widgets(self)

    self.chat_listener_thread = chat_listener_thread()
    self.chat_listener_thread.response.connect(chat_listener_thread_response)

    def chat_sender_thread_response(response):
        chat_listener_thread_response(response)

    def chat_sender_thread_progress(response):
        self.chat_screen_conversation_frame_sending_message_progressbar.setValue(int(response * 100))
        self.chat_screen_conversation_frame_sending_message_progressbar_label.setText(_('chat_screen.sending_message'))

    def chat_sender_thread_sent(response):
        self.chat_screen_conversation_frame_sending_message_progressbar.setValue(0)
        self.chat_screen_conversation_frame_sending_message_progressbar_label.setText(_('chat_screen.sending_message_ready') if response else _('chat_screen.sending_message_error'))
        self.chat_screen_conversation_frame_message_textedit.setEnabled(True)
        if response:
            chat_screen_conversation_frame_message_clear(self)

    self.chat_sender_thread = chat_sender_thread()
    self.chat_sender_thread.response.connect(chat_sender_thread_response)
    self.chat_sender_thread.progress.connect(chat_sender_thread_progress)
    self.chat_sender_thread.sent.connect(chat_sender_thread_sent)


def update_widgets(self):
    self.chat_screen_list_frame_avatar_line_name.setText(paths.SESSION['selected_wallet'])
    self.chat_screen_list_frame_conversations_list.setVisible(bool(paths.SESSION.get('conversations', {})) and not self.chat_screen_list_add_frame.isVisible())
    self.chat_screen_list_frame_conversations_bottom_line.setVisible(bool(paths.SESSION.get('conversations', {})) and not self.chat_screen_list_add_frame.isVisible())
    self.chat_screen_list_frame_conversations_loading_message.setVisible(not bool(paths.SESSION.get('conversations', {})))
    self.chat_screen_conversation_frame_chat.setVisible(bool(paths.SESSION.get('selected_conversation', False)) and bool(paths.SESSION.get('selected_conversation', {}).get('chat_history', [])))
    self.chat_screen_conversation_frame_connecting_message_line.setVisible(bool(paths.SESSION.get('selected_conversation', False)) and not bool(paths.SESSION.get('selected_conversation', {}).get('chat_history', [])))
    self.chat_screen_conversation_frame_message_line.setVisible(bool(paths.SESSION.get('selected_conversation', False)))
    self.chat_screen_conversation_frame_sending_message_progressbar.setVisible(bool(paths.SESSION.get('selected_conversation', False)))
    self.chat_screen_conversation_frame_select_chat_alert.setVisible(not bool(paths.SESSION.get('selected_conversation', False)))
    self.chat_screen_conversation_frame_message_textedit.setEnabled(self.chat_screen_conversation_frame_chat.isVisible())
    chat_screen_list_frame_conversations_list_update(self)


def chat_screen_list_frame_conversations_list_update(self):
    current_wallet_selected = list(paths.SESSION['conversations'].keys())[self.chat_screen_list_frame_conversations_list.currentRow()] if self.chat_screen_list_frame_conversations_list.currentRow() >= 0 else ''
    self.chat_screen_list_frame_conversations_list.clear()
    for wallet_id in paths.SESSION.get('conversations', {}):
        conv = paths.SESSION.get('conversations', {})[wallet_id]
        item = QListWidgetItem()

        self.chat_screen_list_frame_conversations_list.addItem(item)

        item_widget = QWidget()
        item_widget.setFixedHeight(48)
        item_widget.setLayout(QHBoxLayout())
        item_widget.layout().setContentsMargins(0, 0, 0, 0)
        item_widget.layout().setSpacing(10)
        item_widget_avatar = QLabel()
        item_widget_avatar.setPixmap(QPixmap(paths.get_graphics_path('wallet_icon.svg')).scaled(QSize(48, 48), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        item_widget_avatar.setFixedSize(48, 48)
        item_widget.layout().addWidget(item_widget_avatar)
        item_widget_label_text = conv['wallet'] if not conv['nickname'] else str('<big>' + str('<b>{nickname} ({unr})</b>'.format(nickname=conv['nickname'], unr=conv['unread_messages']) if conv['unread_messages'] else '{nickname}'.format(nickname=conv['nickname'])) + '</big><br><small>{id}</small>'.format(id=conv['wallet']))
        item_widget_label = QLabel(item_widget_label_text)
        if conv['status'] in ['blocked']:
            item_widget_label.setStyleSheet('QLabel { color: silver }')
        item_widget_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        item_widget.layout().addWidget(item_widget_label, 1)

        self.chat_screen_list_frame_conversations_list.setItemWidget(item, item_widget)

        if current_wallet_selected == conv['wallet']:
            self.chat_screen_list_frame_conversations_list.setCurrentItem(item)
    chat_screen_list_frame_conversations_list_currentitemchanged(self)

def show_screen(self):
    self.main_widget.setCurrentWidget(self.chat_screen_widget)
    self.retrieve_conversations_thread.wallet = paths.SESSION['selected_wallet']
    self.retrieve_conversations_thread.start()
    update_widgets(self)

def chat_screen_conversation_frame_message_clear(self):
    self.chat_screen_conversation_frame_message_textedit.document().setPlainText('')
    chat_screen_conversation_frame_message_textedit_textchanged(self)


def chat_screen_conversation_frame_message_textedit_textchanged(self):
    self.chat_screen_conversation_frame_message_send_button.setEnabled(bool(self.chat_screen_conversation_frame_message_textedit.toPlainText().strip()) and self.chat_screen_conversation_frame_chat.isVisible())


def chat_screen_list_frame_conversations_list_activated(self):
    paths.SESSION['selected_conversation'] = paths.SESSION['conversations'][list(paths.SESSION['conversations'].keys())[self.chat_screen_list_frame_conversations_list.currentRow()]]
    paths.SESSION['selected_conversation']['unread_messages'] = 0
    chat_screen_conversation_frame_message_clear(self)
    if not paths.SESSION['selected_conversation']['wallet'] in self.chat_listener_thread.wallets:
        self.retrieve_chat_history_thread.wallet = paths.SESSION['selected_conversation']['wallet']
        self.retrieve_chat_history_thread.start()
    chat_screen_conversation_frame_chat_update(self, clear=True)
    update_widgets(self)


def chat_screen_conversation_frame_chat_get_itemwidget(message):
    item_widget = QWidget()
    item_widget.setLayout(QVBoxLayout())
    item_widget.layout().setContentsMargins(0, 0, 0, 0)
    item_widget.layout().setSpacing(2)

    # if message['status'] in ['sent']:
    #     item_widget.layout().addStretch()

    text_message = message['message']

    if message['status'] in ['alert']:
        text_message += ' - {date}'.format(date=datetime.datetime.strptime(message['timestamp'], '%Y%m%d%H%M%S').strftime('%H:%M:%S, %d/%m/%Y'))

    item_widget_message = QLabel(text_message)

    if message['status'] in ['alert']:
        item_widget_message_stylesheet = '''
            QLabel {
                background-color: #F8F8F8;
                border-radius: 5px;
                color: silver;
                font-size: 10px;
                padding: 12px;
                font-style: italic;
            }
        '''
    else:
        item_widget_message_stylesheet = '''
            QLabel {
                background-color: #E8E8E8;
                border-radius: 5px;
                color: black;
                font-size: 14px;
                padding: 12px;
            }
        '''

        if message['status'] in ['sent', 'readed', 'error']:
            item_widget_message_stylesheet += '''
                QLabel {
                    background-color: #cfe0df;
                    border-bottom-right-radius: 0;
                }
            '''
        else:
            item_widget_message_stylesheet += '''
                QLabel {
                    border-top-left-radius: 0;
                }
            '''

    item_widget_message.setStyleSheet(item_widget_message_stylesheet)

    item_widget_timestamp_text = ''
    if message['status'] in ['sent']:
        item_widget_timestamp_text += '… '
    elif message['status'] in ['readed']:
        item_widget_timestamp_text += '✓ '
    elif message['status'] in ['error']:
        item_widget_timestamp_text += '⚠️ '
    item_widget_timestamp_text += '{date}'.format(date=datetime.datetime.strptime(message['timestamp'], '%Y%m%d%H%M%S').strftime('%H:%M:%S, %d/%m/%Y'))

    item_widget_timestamp = QLabel(item_widget_timestamp_text)
    item_widget_timestamp.setStyleSheet('''
        QLabel {
            color: silver;
            font-style: italic;
            font-size: 9px;
            padding-left: 4px;
        }
    ''')

    if message['status'] in ['received']:
        item_widget_message.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        item_widget.layout().addWidget(item_widget_message, 0, Qt.AlignmentFlag.AlignLeft)
        item_widget.layout().addWidget(item_widget_timestamp, 0, Qt.AlignmentFlag.AlignLeft)
    elif message['status'] in ['sent', 'readed', 'error']:
        item_widget_message.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
        item_widget.layout().addWidget(item_widget_message, 0, Qt.AlignmentFlag.AlignRight)
        item_widget.layout().addWidget(item_widget_timestamp, 0, Qt.AlignmentFlag.AlignRight)
    elif message['status'] in ['alert']:
        item_widget_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        item_widget.layout().addWidget(item_widget_message, 0, Qt.AlignmentFlag.AlignCenter)

    return item_widget


def chat_screen_conversation_frame_chat_update(self, clear=False, message={}):
    if clear:
        self.chat_screen_conversation_frame_chat.clear()
        for msg in paths.SESSION['selected_conversation']['chat_history']:
            item = QListWidgetItem()
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable)
            item_widget = chat_screen_conversation_frame_chat_get_itemwidget(msg)
            item.setSizeHint(QSize(item_widget.sizeHint().width(), item_widget.sizeHint().height() + 20))
            self.chat_screen_conversation_frame_chat.addItem(item)
            self.chat_screen_conversation_frame_chat.setItemWidget(item, item_widget)
        self.chat_screen_conversation_frame_sending_message_progressbar_label.setText(_('chat_screen.sending_message_ready'))

    if message:
        item = QListWidgetItem()
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsSelectable)
        item_widget = chat_screen_conversation_frame_chat_get_itemwidget(message)
        item.setSizeHint(QSize(item_widget.sizeHint().width(), item_widget.sizeHint().height() + 20))
        self.chat_screen_conversation_frame_chat.addItem(item)
        self.chat_screen_conversation_frame_chat.setItemWidget(item, item_widget)
    self.chat_screen_conversation_frame_chat.scrollToBottom()


def chat_screen_conversation_frame_message_send_button_clicked(self):
    self.chat_sender_thread.message = self.chat_screen_conversation_frame_message_textedit.toPlainText()
    self.chat_sender_thread.wallet = paths.SESSION['selected_conversation']['wallet']
    self.chat_sender_thread.start()
    self.chat_screen_conversation_frame_message_send_button.setEnabled(False)
    self.chat_screen_conversation_frame_message_textedit.setEnabled(False)



def chat_screen_list_frame_conversations_bottom_line_remove_button_clicked(self):
    wallet_to_remove = list(paths.SESSION['conversations'].keys())[self.chat_screen_list_frame_conversations_list.currentRow()]
    if wallet_to_remove == paths.SESSION['selected_conversation']['wallet']:
        paths.SESSION['selected_conversation'] = False
    del paths.SESSION['conversations'][wallet_to_remove]
    update_widgets(self)

def chat_screen_list_frame_conversations_bottom_line_add_button_clicked(self):
    self.chat_screen_list_add_nickname_lineedit.setText('')
    self.chat_screen_list_add_wallet_lineedit.document().setPlainText('')
    chat_screen_list_add_textedited(self)
    self.chat_screen_list_frame_conversations_bottom_line.setVisible(False)
    self.chat_screen_list_frame_conversations_list.setVisible(False)
    self.chat_screen_list_add_frame.setVisible(True)


def chat_screen_list_frame_conversations_list_currentitemchanged(self):
    self.chat_screen_list_frame_conversations_bottom_line_remove_button.setVisible(bool(self.chat_screen_list_frame_conversations_list.currentItem()))


def chat_screen_list_add_textedited(self):
    self.chat_screen_list_add_confirm_button.setEnabled(bool(self.chat_screen_list_add_wallet_lineedit.toPlainText().strip()))

def chat_screen_list_add_cancel_button_clicked(self):
    self.chat_screen_list_add_frame.setVisible(False)
    update_widgets(self)

def chat_screen_list_add_confirm_button_clicked(self):
    paths.SESSION['conversations'][self.chat_screen_list_add_wallet_lineedit.toPlainText()] = {
        'wallet': self.chat_screen_list_add_wallet_lineedit.toPlainText(),
        'nickname': self.chat_screen_list_add_nickname_lineedit.text(),
        'chat_history': [],
        'unread_messages': 0
    }
    chat_screen_list_add_cancel_button_clicked(self)

def chat_screen_list_frame_conversations_list_menu_remove_action_clicked(self):
    chat_screen_list_frame_conversations_bottom_line_remove_button_clicked(self)

def chat_screen_list_frame_conversations_list_menu_block_action_clicked(self):
    wallet_to_block = list(paths.SESSION['conversations'].keys())[self.chat_screen_list_frame_conversations_list.currentRow()]
    if wallet_to_block in self.chat_listener_thread.wallets:
        self.chat_listener_thread.wallets.remove(wallet_to_block)
    paths.SESSION['conversations'][wallet_to_block]['status'] = 'blocked'
    update_widgets(self)

def chat_screen_list_frame_conversations_list_menu_message_action_clicked(self):
    chat_screen_list_frame_conversations_list_activated(self)


def translate_widgets(self):
    self.chat_screen_list_frame_conversations_loading_message.setText(_('chat_screen.loading_message'))
    self.chat_screen_conversation_frame_select_chat_alert.setText(_('chat_screen.select_chat_alert'))
    self.chat_screen_conversation_frame_message_send_button.setText(_('chat_screen.send_button'))
    self.chat_screen_conversation_frame_connecting_message_label.setText(_('chat_screen.connecting_message'))
    self.chat_screen_conversation_frame_sending_message_progressbar_label.setText(_('chat_screen.sending_message_ready'))
    self.chat_screen_list_add_wallet_label.setText(_('chat_screen.add_wallet_contact'))
    self.chat_screen_list_add_nickname_label.setText(_('chat_screen.add_wallet_nickname'))
